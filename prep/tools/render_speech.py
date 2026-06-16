#!/usr/bin/env python3
"""Render dual-voice TTS audio per slide from speaker-script.md.

Parses short/speaker-script.md, finds each `## Slide N - title` heading,
collects the `**SP1:**` and `**SP2:**` turns under it, builds SSML alternating
between two Azure Neural voices, and synthesizes one WAV per slide.

Auth: DefaultAzureCredential (same identity as `az login`).
Backend: Azure Speech REST endpoint on the AIServices account in eastus2.

Usage:
    python render_speech.py                       # render all missing slides
    python render_speech.py --slides 1 4 7        # only those slides
    python render_speech.py --force               # re-render even if WAV exists
    python render_speech.py --dry-run             # print SSML, don't call API
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import xml.sax.saxutils as xml_utils
from pathlib import Path

import requests
from azure.identity import AzureCliCredential

REGION = "eastus2"
ACCOUNT_HOST = "aif-agentops-experimentation.cognitiveservices.azure.com"
TENANT_ID = "16b3c013-d300-468d-ac64-7eda0820b6d3"
TTS_ENDPOINT = f"https://{REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
ISSUE_TOKEN_URL = f"https://{ACCOUNT_HOST}/sts/v1.0/issuetoken"
SCOPE = "https://cognitiveservices.azure.com/.default"

VOICE_SP1 = "en-US-AvaMultilingualNeural"
VOICE_SP2 = "en-US-AndrewMultilingualNeural"

REPO = Path(__file__).resolve().parent.parent.parent
SCRIPT_PATH = REPO / "short" / "speaker-script.md"
AUDIO_DIR = REPO / "prep" / "short" / "audio"

# Inter-turn pause and inter-paragraph natural rhythm
INTER_TURN_BREAK_MS = 350
PARAGRAPH_BREAK_MS = 150


def parse_script(script_text: str) -> dict[int, list[tuple[str, str]]]:
    """Return {slide_number: [(speaker, text), ...]} in document order.

    Speaker is 'SP1' or 'SP2'. Text is the raw turn content (markdown emphasis
    still present; stripped later before SSML build). Speaker turns can span
    multiple Markdown paragraphs so the rendered script stays easy to read.
    """
    slides: dict[int, list[tuple[str, str]]] = {}
    current_slide: int | None = None
    current_speaker: str | None = None
    current_parts: list[str] = []

    slide_re = re.compile(r"^##\s+Slide\s+(\d+)\s*[-–—]")
    turn_re = re.compile(r"^\*\*(SP1|SP2):\*\*\s*(.*)$")

    def flush_turn() -> None:
        nonlocal current_speaker, current_parts
        if current_slide is not None and current_speaker and current_parts:
            text = " ".join(part.strip() for part in current_parts if part.strip())
            if text:
                slides.setdefault(current_slide, []).append((current_speaker, text))
        current_speaker = None
        current_parts = []

    for raw_line in script_text.splitlines():
        line = raw_line.strip()

        m = slide_re.match(line)
        if m:
            flush_turn()
            current_slide = int(m.group(1))
            slides.setdefault(current_slide, [])
            continue

        if current_slide is None:
            continue

        if line == "---":
            flush_turn()
            continue

        tm = turn_re.match(line)
        if tm:
            flush_turn()
            current_speaker = tm.group(1)
            first_text = tm.group(2).strip()
            if first_text:
                current_parts.append(first_text)
            continue

        if current_speaker and line:
            current_parts.append(line)

    flush_turn()
    return slides


def clean_text_for_tts(text: str) -> str:
    """Strip markdown emphasis and normalize for natural speech."""
    # Remove bold markers (shouldn't appear inside a turn, but be safe)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    # Italics: *word* -> word  (single asterisks)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\1", text)
    # Backtick code -> plain
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Smart-quote some apostrophes commonly mangled by markdown
    # (Neural voices handle straight quotes fine, leave them.)
    return text.strip()


def build_ssml(turns: list[tuple[str, str]]) -> str:
    """Build an SSML <speak> with alternating voices and inter-turn breaks.

    Breaks are placed INSIDE the preceding `<voice>` element (a sibling of the
    text), not between `<voice>` elements. The Azure TTS REST endpoint
    rejects `<break>` as a direct child of `<speak>` with HTTP 400.
    """
    parts = [
        "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' "
        "xml:lang='en-US'>"
    ]
    for i, (speaker, raw) in enumerate(turns):
        voice = VOICE_SP1 if speaker == "SP1" else VOICE_SP2
        text = clean_text_for_tts(raw)
        safe = xml_utils.escape(text)
        parts.append(f"<voice name='{voice}'>")
        # A subtle prosody rate keeps things conversational without rushing
        parts.append(f"<prosody rate='-2%'>{safe}</prosody>")
        # Trailing break for natural pause before the other speaker
        if i < len(turns) - 1:
            parts.append(f"<break time='{INTER_TURN_BREAK_MS}ms'/>")
        parts.append("</voice>")
    parts.append("</speak>")
    return "".join(parts)


def get_token() -> str:
    """Exchange an AAD token for a short-lived Speech-service JWT.

    The TTS REST endpoint accepts only Speech-issued tokens (or subscription
    keys). The issuetoken endpoint on the AIServices custom-domain accepts an
    AAD Bearer and returns a JWT good for ~10 minutes.

    We pin AzureCliCredential to the resource's tenant because
    DefaultAzureCredential can otherwise return a Microsoft Corp token that
    the resource rejects with a tenant-mismatch error. The CLI process can be
    slow on Windows so we give it a generous timeout.
    """
    cred = AzureCliCredential(tenant_id=TENANT_ID, process_timeout=60)
    aad = cred.get_token(SCOPE).token
    r = requests.post(
        ISSUE_TOKEN_URL,
        headers={"Authorization": f"Bearer {aad}", "Content-Length": "0"},
        timeout=30,
    )
    if r.status_code != 200:
        print(f"issuetoken HTTP {r.status_code}: {r.text[:500]}", file=sys.stderr)
        raise SystemExit(2)
    return r.text.strip()


def synthesize(ssml: str, out_path: Path, token: str) -> None:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
        "User-Agent": "agentops-workshop-render",
    }
    t0 = time.time()
    r = requests.post(TTS_ENDPOINT, headers=headers, data=ssml.encode("utf-8"),
                      timeout=300)
    elapsed = time.time() - t0
    if r.status_code != 200:
        print(f"  HTTP {r.status_code} in {elapsed:.1f}s")
        print("  Headers:", dict(r.headers))
        print("  Body:", r.text[:4000])
        print("  SSML:", ssml[:1500])
        raise SystemExit(2)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(r.content)
    kb = len(r.content) / 1024
    print(f"  -> {out_path.name}  ({kb:,.0f} KB, {elapsed:.1f}s)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slides", type=int, nargs="*",
                   help="Only render these slide numbers (default: all).")
    p.add_argument("--force", action="store_true",
                   help="Re-render even if the output WAV exists.")
    p.add_argument("--dry-run", action="store_true",
                   help="Print SSML for each slide without calling the API.")
    args = p.parse_args()

    if not SCRIPT_PATH.exists():
        print(f"Script not found: {SCRIPT_PATH}", file=sys.stderr)
        sys.exit(1)

    script_text = SCRIPT_PATH.read_text(encoding="utf-8")
    slides = parse_script(script_text)
    if not slides:
        print("No slides parsed - check the markdown format.", file=sys.stderr)
        sys.exit(1)

    nums = sorted(slides.keys())
    if args.slides:
        nums = [n for n in nums if n in args.slides]

    print(f"Parsed {len(slides)} slides; rendering {len(nums)}.")
    print(f"Voices: SP1={VOICE_SP1}  SP2={VOICE_SP2}")

    token = None
    if not args.dry_run:
        print("Acquiring AAD token...")
        token = get_token()

    for n in nums:
        turns = slides[n]
        if not turns:
            print(f"Slide {n}: no turns, skipping.")
            continue

        out_path = AUDIO_DIR / f"slide-{n:02d}.wav"
        if out_path.exists() and not args.force and not args.dry_run:
            print(f"Slide {n:02d}: exists, skipping ({out_path.stat().st_size/1024:,.0f} KB).")
            continue

        ssml = build_ssml(turns)
        chars = sum(len(clean_text_for_tts(t)) for _, t in turns)
        print(f"Slide {n:02d}: {len(turns)} turns, ~{chars} chars")

        if args.dry_run:
            print(ssml[:600] + ("..." if len(ssml) > 600 else ""))
            continue

        synthesize(ssml, out_path, token)


if __name__ == "__main__":
    main()
