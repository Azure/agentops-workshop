#!/usr/bin/env python3
"""Production AgentOps short video builder (avatar-aware).

Two staging modes per slide:

* **Intro slides (1-3): jogral** -- per-turn single active avatar with a 0.4s
  alpha crossfade at every WITHIN-slide speaker change. Same look-and-feel
  the user approved in the v4 preview (lisa<->harry corner handoff). At
  slide boundaries we DROP the alpha fade and let the 0.5s slide xfade do
  the handoff (avoids a "double-fade" ghosting effect where avatar opacity
  is multiplied by the slide dissolve).

* **Core slides (4+): one-avatar-per-slide.** All SP1/SP2 turns within a
  core slide are merged into a single super-turn rendered by ONE speaker
  via Azure TTS Avatar with SSML pacing -- the original turn boundaries
  become ``<break time='350ms'/>`` pauses so a 1-2 minute monologue still
  has the natural cadence the dual-voice script was written for.

  The speaker is taken from the script for that slide, so the rendered
  video follows the two-speaker content assignment exactly.

* **Demo slots:** after demo-intro slides 14, 17, 21, and 26, the matching
  MP4 under ``short/videos`` is inserted directly with its original audio and
  no avatar overlay. Demo files are normalized to the deck canvas before the
  final slide/demo xfade chain.

The script reuses every v4 helper from ``build_preview.py``: avatar batch
synthesis, content-hash WEBM caching, chromakey + alpha-fade overlay,
per-slide concat, and the final xfade chain. To avoid clobbering the
preview segment cache (same v4 segment names but different turn structure
for slides 4-23), production segments live under a separate
``v4p-*`` segment-version namespace inside ``prep/short/preview/segments/``.

Output: ``short/agentops-short-video.mp4`` (replaces the previous
voiceover-only build from the legacy ``build_video.py``). The raw artefact
is expected to exceed GitHub's 100 MB push limit, so run
``compress_production_video.py`` before committing the published MP4.

Usage::

    python build_production_video.py                   # full 30-slide build
    python build_production_video.py --skip-avatars    # cache already populated
    python build_production_video.py --force           # ignore segment cache too
    python build_production_video.py --slides 4 5 6    # subset for iteration
"""

from __future__ import annotations

import argparse
import concurrent.futures
import shutil
import subprocess
import sys
import xml.sax.saxutils as xml_utils
from pathlib import Path

# Reuse all the v4 building blocks from the preview pipeline.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_preview import (  # noqa: E402
    AVATAR_SP1, AVATAR_SP2, VOICE_SP1, VOICE_SP2,
    SCRIPT_PATH, SLIDE_DIR, CACHE_DIR, SEG_DIR,
    parse_script, clean_text_for_tts, cache_key,
    get_aad_token, synthesize_turn,
    build_turn_segment, ffprobe_duration,
    concat_segments, chain_with_xfade,
)


# ---------------------------------------------------------------------------
# Production-specific constants
# ---------------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent.parent
OUT_PATH = REPO / "short" / "agentops-short-video.mp4"
DEMO_DIR = REPO / "short" / "videos"

# Separate segment-version namespace so production renders never collide
# with preview renders (same slide+turn coords but different turn content
# for slides 4-23 because of the merged-text mode).
PROD_SEG_VERSION = "v4p2"

# Slides 1..INTRO_END (inclusive) use per-turn jogral.
INTRO_END = 3
# Slides CORE_START..EXPECTED_LAST_SLIDE (inclusive) use merged single-speaker per slide.
CORE_START = 4

# Pin the highest slide so an accidental script edit cannot silently
# stretch the build. parse_script will validate the actual range.
EXPECTED_LAST_SLIDE = 30

DEMO_VIDEO_BY_SLIDE = {
    14: DEMO_DIR / "part1-evaluate.mp4",
    17: DEMO_DIR / "part2-ship.mp4",
    21: DEMO_DIR / "part3-observe.mp4",
    26: DEMO_DIR / "part4-own.mp4",
}

# Inter-turn pause for merged super-turns (matches render_speech.py).
INTER_TURN_BREAK_MS = 350


def core_speaker_for(slide_turns: list[tuple[str, str]]) -> str:
    """Use the scripted speaker for one-avatar-per-slide production mode."""
    speakers = {speaker for speaker, _raw in slide_turns}
    if len(speakers) > 1:
        raise SystemExit(
            "Production core mode expects one scripted speaker per slide; "
            f"found mixed speakers: {sorted(speakers)}"
        )
    return slide_turns[0][0]


def normalize_demo_segment(src: Path, dst: Path, force: bool) -> None:
    """Normalize a demo MP4 to the deck canvas while preserving its audio."""
    if dst.exists() and not force:
        return
    if not src.exists():
        raise SystemExit(f"Missing demo video: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    vf = (
        "fps=30,"
        "scale=1920:1080:flags=lanczos:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
        "setsar=1,format=yuv420p"
    )
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(src),
        "-vf", vf,
        "-af", "aresample=async=1",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(dst),
    ]
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------------------
# SSML construction for merged super-turns
# ---------------------------------------------------------------------------

def build_merged_ssml(voice: str, raw_turns: list[tuple[str, str]]) -> str:
    """Build SSML that reads ``raw_turns`` in one voice with paced breaks.

    Each original SP1/SP2 turn becomes a ``<prosody>`` block; consecutive
    blocks are separated by a 350 ms ``<break>`` so the merged monologue
    still has the conversational cadence the dual-voice script was
    written for. The text is XML-escaped via saxutils.escape.

    Pattern mirrors render_speech.build_ssml: the break sits between two
    <prosody> elements inside the same <voice>, never as a direct child of
    <speak> (Azure TTS rejects that with HTTP 400).
    """
    parts = [
        "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' "
        "xml:lang='en-US'>",
        f"<voice name='{voice}'>",
    ]
    for i, (_speaker, raw) in enumerate(raw_turns):
        safe = xml_utils.escape(clean_text_for_tts(raw))
        parts.append(f"<prosody rate='-2%'>{safe}</prosody>")
        if i < len(raw_turns) - 1:
            parts.append(f"<break time='{INTER_TURN_BREAK_MS}ms'/>")
    parts.append("</voice></speak>")
    return "".join(parts)


# ---------------------------------------------------------------------------
# Turn list construction (mixed mode)
# ---------------------------------------------------------------------------

def build_production_turn_list(
    slides_data: dict[int, list[tuple[str, str]]],
    slide_nums: list[int],
) -> list[dict]:
    """Produce a flat turn list with intro-jogral and core-merged modes."""
    turns: list[dict] = []
    for sn in slide_nums:
        if sn not in slides_data:
            raise SystemExit(f"Slide {sn} not found in script")
        slide_turns = slides_data[sn]
        if sn <= INTRO_END:
            # Jogral: one segment per SP1/SP2 alternation in the script.
            for turn_idx, (speaker, raw) in enumerate(slide_turns, start=1):
                text = clean_text_for_tts(raw)
                if speaker == "SP1":
                    voice, (char, style) = VOICE_SP1, AVATAR_SP1
                else:
                    voice, (char, style) = VOICE_SP2, AVATAR_SP2
                turns.append({
                    "slide": sn,
                    "turn_idx": turn_idx,
                    "speaker": speaker,
                    "voice": voice,
                    "char": char,
                    "style": style,
                    "text": text,
                    "input_kind": "PlainText",
                    "label": f"S{sn:02d}T{turn_idx:02d}/{speaker}",
                    "key": cache_key(text, voice, char, style),
                })
        else:
            # Merged: one SSML-paced super-turn for the whole slide,
            # using the slide's scripted speaker.
            speaker = core_speaker_for(slide_turns)
            if speaker == "SP1":
                voice, (char, style) = VOICE_SP1, AVATAR_SP1
            else:
                voice, (char, style) = VOICE_SP2, AVATAR_SP2
            ssml = build_merged_ssml(voice, slide_turns)
            turns.append({
                "slide": sn,
                "turn_idx": 1,
                "speaker": speaker,
                "voice": voice,
                "char": char,
                "style": style,
                "text": ssml,
                "input_kind": "SSML",
                # Asterisk on the label to flag the merged-mode super-turn.
                "label": f"S{sn:02d}T01/{speaker}*merged({len(slide_turns)}t)",
                # The SSML literal is the cache-key text -- different from
                # any individual PlainText turn so no collision with intro
                # cache entries.
                "key": cache_key(ssml, voice, char, style),
            })
    return turns


# ---------------------------------------------------------------------------
# Cross-slide-aware fade decision
# ---------------------------------------------------------------------------

def compute_fades(turns: list[dict], i: int) -> tuple[bool, bool]:
    """Return (fade_in, fade_out) for ``turns[i]``.

    Rule: alpha-fade the avatar only at WITHIN-slide speaker changes
    (intro jogral). At slide boundaries the 0.5s slide xfade already
    crossdissolves the whole frame, so adding a per-avatar alpha fade on
    top would multiply the opacity dip and read as a ghosty double fade.

    Exceptions:
      * Very first turn fades in from nothing (smooth appear).
      * Very last turn fades out to nothing (smooth disappear).
    """
    t = turns[i]
    first = i == 0
    last = i == len(turns) - 1
    fade_in = first
    fade_out = last
    if not first:
        prev = turns[i - 1]
        if prev["slide"] == t["slide"] and prev["speaker"] != t["speaker"]:
            fade_in = True
    if not last:
        nxt = turns[i + 1]
        if nxt["slide"] == t["slide"] and nxt["speaker"] != t["speaker"]:
            fade_out = True
    return fade_in, fade_out


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--slides", type=int, nargs="+", default=None,
                   help=f"Slides to render (default: 1..{EXPECTED_LAST_SLIDE}).")
    p.add_argument("--force", action="store_true",
                   help="Ignore avatar cache and segment cache.")
    p.add_argument("--skip-avatars", action="store_true",
                   help="Assume avatar WEBM cache is already populated.")
    p.add_argument("--output", default=str(OUT_PATH),
                   help=f"Output mp4 path (default: {OUT_PATH}).")
    args = p.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise SystemExit(f"{tool} not in PATH")

    script_text = SCRIPT_PATH.read_text(encoding="utf-8")
    slides_data = parse_script(script_text)
    if args.slides is None:
        slide_nums = list(range(1, EXPECTED_LAST_SLIDE + 1))
    else:
        slide_nums = sorted(args.slides)

    turns = build_production_turn_list(slides_data, slide_nums)
    intro_count = sum(1 for t in turns if t["slide"] <= INTRO_END)
    core_count = len(turns) - intro_count
    print(f"Slides: {slide_nums[0]}..{slide_nums[-1]} ({len(slide_nums)} slides)")
    print(f"  intro slides (1..{INTRO_END}) -> jogral, {intro_count} per-turn segments")
    print(f"  core slides ({CORE_START}..{slide_nums[-1]}) -> merged SSML, {core_count} per-slide segments")
    print(f"  total segments: {len(turns)}")

    # ---- Phase 1: avatar synthesis -----------------------------------------
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not args.skip_avatars:
        print("\nPhase 1: avatar batch synthesis (Azure TTS Avatar)")
        token = get_aad_token()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
            list(ex.map(lambda t: synthesize_turn(token, t, args.force), turns))

    for t in turns:
        cache = CACHE_DIR / f"{t['key']}.webm"
        if not cache.exists():
            raise SystemExit(f"Missing avatar cache for {t['label']}: {cache}")

    # ---- Phase 2: per-turn composite segments ------------------------------
    print(f"\nPhase 2: per-turn composite segments ({PROD_SEG_VERSION} namespace)")
    SEG_DIR.mkdir(parents=True, exist_ok=True)
    for i, t in enumerate(turns):
        slide_png = SLIDE_DIR / f"slide-{t['slide']:02d}.png"
        if not slide_png.exists():
            raise SystemExit(f"Missing slide PNG: {slide_png}")
        active_webm = CACHE_DIR / f"{t['key']}.webm"
        dur = ffprobe_duration(active_webm)

        fade_in, fade_out = compute_fades(turns, i)

        seg = SEG_DIR / (
            f"{PROD_SEG_VERSION}-turn-{t['slide']:02d}-{t['turn_idx']:02d}.mp4"
        )
        markers = []
        if fade_in:
            markers.append("fade-in")
        if fade_out:
            markers.append("fade-out")
        print(f"  {t['label']}: {dur:.2f}s {' '.join(markers) or 'continuous'}")
        build_turn_segment(
            seg, slide_png, active_webm, t["speaker"], dur,
            fade_in, fade_out, args.force,
        )

    # ---- Phase 3: concat per slide -----------------------------------------
    print("\nPhase 3: concat per-turn segments into per-slide/demo segments")
    slide_segments: list[tuple[Path, float]] = []
    for sn in slide_nums:
        sn_turns = [t for t in turns if t["slide"] == sn]
        turn_segs = [
            SEG_DIR / f"{PROD_SEG_VERSION}-turn-{t['slide']:02d}-{t['turn_idx']:02d}.mp4"
            for t in sn_turns
        ]
        slide_seg = SEG_DIR / f"{PROD_SEG_VERSION}-slide-{sn:02d}.mp4"
        if len(turn_segs) == 1:
            shutil.copyfile(turn_segs[0], slide_seg)
        else:
            concat_segments(turn_segs, slide_seg)
        dur = ffprobe_duration(slide_seg)
        slide_segments.append((slide_seg, dur))
        print(f"  slide {sn:02d}: {dur:.2f}s")
        if sn in DEMO_VIDEO_BY_SLIDE:
            demo_src = DEMO_VIDEO_BY_SLIDE[sn]
            demo_seg = SEG_DIR / f"{PROD_SEG_VERSION}-demo-after-slide-{sn:02d}.mp4"
            normalize_demo_segment(demo_src, demo_seg, args.force)
            demo_dur = ffprobe_duration(demo_seg)
            slide_segments.append((demo_seg, demo_dur))
            print(f"  demo after slide {sn:02d}: {demo_dur:.2f}s ({demo_src.name})")

    # ---- Phase 4: chain with xfade -----------------------------------------
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"\nPhase 4: chain {len(slide_segments)} slides with xfade -> {out_path}")
    chain_with_xfade(slide_segments, out_path)

    final_dur = ffprobe_duration(out_path)
    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"\nDone: {out_path}")
    print(f"  duration: {final_dur:.1f}s ({final_dur/60:.2f} min)")
    print(f"  size:     {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
