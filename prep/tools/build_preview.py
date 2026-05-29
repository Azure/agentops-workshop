#!/usr/bin/env python3
"""Build a *preview* MP4 with a single active avatar and crossfaded speakers.

Scope: a small subset of slides (default: 1, 2, 3) so the user can evaluate the
look-and-feel before we commit to rebuilding the full ~46-minute video.

Visual conventions (locked, v4):
  - Only ONE avatar is on screen at any given time -- the speaker who is
   currently talking. The silent listener is NOT shown at all (the previous
   iteration kept both on screen and the user found the idle motion of the
   listener distracting from the speaker).
  - Lisa (SP1) speaks from the bottom-LEFT corner, flush with the screen
   bottom. Harry (SP2) speaks from the bottom-RIGHT corner, flush bottom.
   Their fixed corners preserve a left/right "voice" identity.
  - Speaker handoffs are CROSSFADED, not abrupt. The outgoing speaker fades
   OUT over FADE_DUR seconds at the end of their last turn, and the incoming
   speaker fades IN over FADE_DUR seconds at the start of their first turn.
   Consecutive turns by the SAME speaker have no fade (continuous presence).
  - Slides only fade between each other (xfade) -- there is NO Ken Burns zoom
   inside a slide. The slide just sits still while the avatar talks.
  - Avatar source crop is wide enough that natural arm gestures do NOT clip,
   and tall enough that the figure is flush with the canvas bottom so they
   look grounded (not floating).

Pipeline:
  1. Parse `short/speaker-script.md` for the requested slides.
  2. Submit one Azure TTS Avatar batch job per turn (cached by content hash).
      SP1 -> en-US-AvaMultilingualNeural + lisa (casual-sitting)
      SP2 -> en-US-AndrewMultilingualNeural + harry (business)
      videoFormat=webm, videoCodec=vp9, backgroundColor=#00B140FF (chromakey
      green; API does NOT honour transparent backgrounds, so we use solid
      green and chromakey it out in ffmpeg).
  3. For each turn, build a per-turn MP4 segment:
      - background: slide PNG scaled to 1920x1080 (no Ken Burns)
      - single overlay: the active speaker's webm, chromakeyed, with optional
        alpha fade-in/fade-out at speaker-change boundaries
      - audio = active speaker's own opus track
  4. Concat per-turn segments within a slide (no transition between turns).
  5. Chain per-slide segments with xfade + acrossfade.
  6. Write `prep/short/preview/avatar-preview.mp4`.

Auth: AzureCliCredential pinned to the resource tenant, same as render_speech.

Usage:
   python build_preview.py                # build preview for slides 1..3
   python build_preview.py --slides 1 2 3 5
   python build_preview.py --force        # ignore avatar/segment cache
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path

import requests
from azure.identity import AzureCliCredential

# Reuse the script parser and text cleaner from the production TTS pipeline
sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_speech import parse_script, clean_text_for_tts  # noqa: E402


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TENANT_ID = "16b3c013-d300-468d-ac64-7eda0820b6d3"
ACCOUNT_HOST = "aif-agentops-experimentation.cognitiveservices.azure.com"
AVATAR_API = f"https://{ACCOUNT_HOST}/avatar/batchsyntheses"
API_VERSION = "2024-08-01"
SCOPE = "https://cognitiveservices.azure.com/.default"

VOICE_SP1 = "en-US-AvaMultilingualNeural"
VOICE_SP2 = "en-US-AndrewMultilingualNeural"

# Prebuilt avatar character + style per speaker.
AVATAR_SP1 = ("lisa", "casual-sitting")
AVATAR_SP2 = ("harry", "business")

# Avatar source frame dims (API returns 1920x1080 with the figure roughly in
# the right-center). We crop a wide portrait window (so extended arm gestures
# never clip) and scale it to the overlay size. The figure's tight bbox is
# approximately cols 731..1225, so we centre the crop around col ~975 with
# generous left/right padding for arm motion.
AVATAR_CROP_W = 900
AVATAR_CROP_H = 1080
AVATAR_CROP_X = 510
AVATAR_CROP_Y = 0
# Overlay size: keep source aspect 900:1080 -> 380:456.
AVATAR_OUT_W = 380
AVATAR_OUT_H = 456
# Horizontal margin from screen edge. Vertical position is FLUSH BOTTOM
# (y = H - h) so the avatar looks grounded, not floating.
AVATAR_MARGIN_X = 36

# Avatar batch synthesis BG: API output is always opaque, so we request a
# pure green that no body/clothing color collides with and chromakey it out
# in ffmpeg. RRGGBBAA per API spec; alpha is ignored.
AVATAR_BG = "#00B140FF"

# Slide canvas
FPS = 30
WIDTH = 1920
HEIGHT = 1080

# Slide-to-slide transition
XFADE_DUR = 0.5

# Segment-file versioning. Bump this when we change the layout / filter graph
# so existing per-turn MP4s in SEG_DIR are not silently reused.
SEG_VERSION = "v4"

# Crossfade between consecutive turns with different speakers. Active speaker
# fades IN over FADE_DUR at the start of their first turn (and after a switch),
# and fades OUT over FADE_DUR at the end of their last turn (and before a
# switch). Consecutive turns by the same speaker have NO fades so the avatar
# stays continuously visible.
FADE_DUR = 0.4

# Skip the first N seconds of an idle clip when looping it as silent-listener
# overlay. The first ~0.3s of an Azure batch avatar webm is the "wake-up"
# frame (a brief lift-of-the-head as the avatar prepares to speak); skipping
# it gives a smoother loop entry into pure idle motion. (Kept for reference;
# the v4 single-active-avatar layout no longer overlays an idle source.)
IDLE_SKIP_S = 0.3

REPO = Path(__file__).resolve().parent.parent.parent
SCRIPT_PATH = REPO / "short" / "speaker-script.md"
SLIDE_DIR = REPO / "prep" / "short" / "video"
CACHE_DIR = REPO / "prep" / "short" / "avatar-cache"
PREVIEW_DIR = REPO / "prep" / "short" / "preview"
SEG_DIR = PREVIEW_DIR / "segments"
OUT_PATH = PREVIEW_DIR / "avatar-preview.mp4"


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

def get_aad_token() -> str:
    cred = AzureCliCredential(tenant_id=TENANT_ID, process_timeout=60)
    return cred.get_token(SCOPE).token


# ---------------------------------------------------------------------------
# Avatar synthesis (REST, batch)
# ---------------------------------------------------------------------------

def cache_key(text: str, voice: str, char: str, style: str) -> str:
    """Stable hash so we never re-submit the same turn twice."""
    h = hashlib.sha256()
    h.update(text.strip().encode("utf-8"))
    h.update(b"|")
    h.update(voice.encode("utf-8"))
    h.update(b"|")
    h.update(char.encode("utf-8"))
    h.update(b"|")
    h.update(style.encode("utf-8"))
    h.update(b"|bg=")
    h.update(AVATAR_BG.encode("utf-8"))
    return h.hexdigest()[:16]


def submit_avatar_job(
    token: str,
    text: str,
    voice: str,
    char: str,
    style: str,
    *,
    input_kind: str = "PlainText",
) -> str:
    job_id = str(uuid.uuid4())
    body = {
        "inputKind": input_kind,
        "inputs": [{"content": text}],
        "synthesisConfig": {"voice": voice},
        "avatarConfig": {
            "talkingAvatarCharacter": char,
            "talkingAvatarStyle": style,
            "videoFormat": "webm",
            "videoCodec": "vp9",
            "backgroundColor": AVATAR_BG,
            "subtitleType": "none",
        },
    }
    # S0 throttles avatar batch creation aggressively; retry on 429.
    for attempt in range(10):
        r = requests.put(
            f"{AVATAR_API}/{job_id}?api-version={API_VERSION}",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json=body,
            timeout=30,
        )
        if r.status_code in (200, 201, 202):
            return job_id
        if r.status_code == 429:
            retry_after = int(r.headers.get("Retry-After", "40"))
            wait = min(retry_after + 2, 90)
            print(f"  ! 429 throttle, sleeping {wait}s (attempt {attempt+1})")
            time.sleep(wait)
            continue
        raise SystemExit(f"avatar PUT HTTP {r.status_code}: {r.text[:500]}")
    raise SystemExit("avatar PUT exhausted retries on 429")


def poll_avatar_job(token: str, job_id: str, timeout_s: int = 600) -> dict:
    url = f"{AVATAR_API}/{job_id}?api-version={API_VERSION}"
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        r = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
        if r.status_code != 200:
            raise SystemExit(f"avatar GET HTTP {r.status_code}: {r.text[:500]}")
        data = r.json()
        status = data.get("status")
        if status == "Succeeded":
            return data
        if status in ("Failed", "Cancelled"):
            raise SystemExit(f"avatar job {job_id} {status}: {json.dumps(data)[:800]}")
        time.sleep(3)
    raise SystemExit(f"avatar job {job_id} timed out after {timeout_s}s")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with dest.open("wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 16):
                fh.write(chunk)


def synthesize_turn(token: str, turn: dict, force: bool) -> Path:
    """Submit + poll + download a single turn. Returns webm path.

    The turn dict may carry an optional ``input_kind`` field set to
    ``"SSML"`` (default ``"PlainText"``). Producers that need SSML pacing
    -- like merged single-speaker super-turns in the production pipeline --
    can build their own SSML doc, store it in ``turn["text"]``, and set
    ``turn["input_kind"] = "SSML"``; the hash in ``turn["key"]`` already
    reflects the literal text/SSML so PlainText and SSML caches never
    collide.
    """
    cache = CACHE_DIR / f"{turn['key']}.webm"
    if cache.exists() and not force:
        print(f"  [{turn['label']}] cached")
        return cache

    job_id = submit_avatar_job(
        token, turn["text"], turn["voice"], turn["char"], turn["style"],
        input_kind=turn.get("input_kind", "PlainText"),
    )
    print(f"  [{turn['label']}] submitted job {job_id[:8]}...")
    data = poll_avatar_job(token, job_id)
    out_url = data["outputs"]["result"]
    download(out_url, cache)
    dur_ms = data.get("properties", {}).get("durationInMilliseconds")
    print(f"  [{turn['label']}] done ({dur_ms} ms, {cache.stat().st_size//1024} KB)")
    return cache


def prepare_idle_clip(
    token: str | None,
    voice: str,
    char: str,
    style: str,
    out_webm: Path,
    force: bool,
) -> Path:
    """Ensure a 20-ish second idle webm exists for ``char``.

    The clip is generated by submitting an SSML batch job that wraps a brief
    soft "Mm." utterance in 10s of Leading-exact silence and 10s of Tailing-
    exact silence. The Azure batch avatar API refuses a job with NO speech
    content (it returns "Input audio is too short to generate meaningful
    video content"), but happily renders the ~20s of silence around a tiny
    "Mm." token. The result captures the same NATIVE idle motion that the
    Live Avatar shows when not being asked to speak: gentle breathing,
    blinks, hair settling, micro head shifts.

    The clip is looped at the ffmpeg input level (``-stream_loop -1``) with
    a small ``-ss`` skip to avoid the wake-up frame at t=0. Its audio track
    is never mixed into the output; only the active speaker's audio plays.
    """
    if out_webm.exists() and not force:
        return out_webm
    if token is None:
        raise SystemExit(
            f"Idle clip missing for {char} ({out_webm}); cannot synthesize "
            "without a token. Re-run without --skip-avatars to generate it, "
            "or restore the file from cache."
        )
    ssml = (
        '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
        'xmlns:mstts="http://www.w3.org/2001/mstts" '
        'version="1.0" xml:lang="en-US">'
        f'<voice name="{voice}">'
        '<mstts:silence type="Leading-exact" value="10000ms"/>'
        '<prosody volume="x-soft">Mm.</prosody>'
        '<mstts:silence type="Tailing-exact" value="10000ms"/>'
        '</voice></speak>'
    )
    print(f"  [idle-{char}] submitting SSML idle job...")
    job_id = submit_avatar_job(token, ssml, voice, char, style, input_kind="SSML")
    data = poll_avatar_job(token, job_id)
    download(data["outputs"]["result"], out_webm)
    print(f"  [idle-{char}] done ({out_webm.stat().st_size//1024} KB)")
    return out_webm


# ---------------------------------------------------------------------------
# ffmpeg helpers
# ---------------------------------------------------------------------------

def ffprobe_duration(path: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(json.loads(r.stdout)["format"]["duration"])


def build_turn_segment(
    seg_out: Path,
    slide_png: Path,
    active_src: Path,
    active_speaker: str,
    duration: float,
    fade_in: bool,
    fade_out: bool,
    force: bool,
) -> None:
    """One slide PNG + one avatar webm (the ACTIVE speaker only) -> per-turn MP4.

    Only the speaking avatar is on screen. Lisa (SP1) sits bottom-LEFT; Harry
    (SP2) sits bottom-RIGHT. Both are flush with the canvas bottom edge.

    When ``fade_in`` is True (first turn, or previous turn was a different
    speaker) the avatar's alpha fades in from 0 over FADE_DUR seconds at the
    start. When ``fade_out`` is True (last turn, or next turn is a different
    speaker) it fades back to 0 over FADE_DUR seconds at the end. When both
    flags are False the avatar stays fully visible (consecutive same-speaker
    turns).

    Concatenated, the result is: speaker A fully visible -> fade out -> blank
    background for the duration of the inter-turn gap (typically zero) ->
    speaker B fades in. Adjacent fade-out + fade-in across a speaker switch
    reads as a crossfade between corners.
    """
    if seg_out.exists() and not force:
        return

    seg_out.parent.mkdir(parents=True, exist_ok=True)

    if active_speaker == "SP1":
        overlay_x = f"{AVATAR_MARGIN_X}"
    else:
        overlay_x = f"W-w-{AVATAR_MARGIN_X}"

    fade_filters: list[str] = []
    if fade_in:
        fade_filters.append(f"fade=in:st=0:d={FADE_DUR}:alpha=1")
    if fade_out:
        fade_out_start = max(0.0, duration - FADE_DUR)
        fade_filters.append(
            f"fade=out:st={fade_out_start:.3f}:d={FADE_DUR}:alpha=1"
        )
    fade_chain = ("," + ",".join(fade_filters)) if fade_filters else ""

    fc = (
        # Background: just scale the slide; no Ken Burns.
        f"[0:v]scale={WIDTH}:{HEIGHT}:flags=lanczos,"
        f"setsar=1,format=yuv420p,fps={FPS}[bg];"
        # Active speaker overlay (input 1). Chromakey, crop, scale, optional
        # alpha fade in/out at speaker-change boundaries.
        f"[1:v]fps={FPS},chromakey=0x00B140:0.10:0.04,"
        f"crop={AVATAR_CROP_W}:{AVATAR_CROP_H}:{AVATAR_CROP_X}:{AVATAR_CROP_Y},"
        f"scale={AVATAR_OUT_W}:{AVATAR_OUT_H}:flags=lanczos,"
        f"format=yuva420p{fade_chain}[av];"
        # Composite: single overlay at the speaker's corner, flush bottom.
        f"[bg][av]overlay=x={overlay_x}:y=H-h:format=auto[v];"
        f"[1:a]aresample=async=1[a]"
    )

    cmd: list[str] = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-r", str(FPS), "-t", f"{duration:.3f}", "-i", str(slide_png),
        "-i", str(active_src),
        "-filter_complex", fc,
        "-map", "[v]", "-map", "[a]",
        "-t", f"{duration:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k",
        "-movflags", "+faststart",
        str(seg_out),
    ]
    subprocess.run(cmd, check=True)


def concat_segments(segs: list[Path], out_path: Path) -> None:
    """Lossless concat of segments with identical codec params (concat demuxer)."""
    listfile = out_path.with_suffix(".txt")
    listfile.write_text("".join(f"file '{p.as_posix()}'\n" for p in segs), encoding="ascii")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(listfile),
        "-c", "copy",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)
    listfile.unlink(missing_ok=True)


def chain_with_xfade(slide_segments: list[tuple[Path, float]], out_path: Path) -> None:
    """xfade slide segments with acrossfade audio."""
    inputs: list[str] = []
    for path, _ in slide_segments:
        inputs += ["-i", str(path)]

    filters: list[str] = []
    for i, (_, dur) in enumerate(slide_segments):
        filters.append(
            f"[{i}:v]fps={FPS},scale={WIDTH}:{HEIGHT}:flags=lanczos,"
            f"setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v{i}]"
        )
        filters.append(f"[{i}:a]asetpts=PTS-STARTPTS[a{i}]")

    if len(slide_segments) == 1:
        vlabel, alabel = "v0", "a0"
    else:
        cumulative = slide_segments[0][1]
        vlabel, alabel = "v0", "a0"
        for i in range(1, len(slide_segments)):
            offset = cumulative - XFADE_DUR
            new_v = f"vx{i}"
            new_a = f"ax{i}"
            filters.append(
                f"[{vlabel}][v{i}]xfade=transition=fade:duration={XFADE_DUR}:"
                f"offset={offset:.3f}[{new_v}]"
            )
            filters.append(
                f"[{alabel}][a{i}]acrossfade=d={XFADE_DUR}:c1=tri:c2=tri[{new_a}]"
            )
            cumulative = cumulative + slide_segments[i][1] - XFADE_DUR
            vlabel = new_v
            alabel = new_a

    cmd = [
        "ffmpeg", "-y", "-loglevel", "info",
        *inputs,
        "-filter_complex", ";".join(filters),
        "-map", f"[{vlabel}]", "-map", f"[{alabel}]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def build_turn_list(slides_data: dict[int, list[tuple[str, str]]], slide_nums: list[int]) -> list[dict]:
    """Flatten requested slides into a list of turn dicts."""
    turns: list[dict] = []
    for sn in slide_nums:
        if sn not in slides_data:
            raise SystemExit(f"Slide {sn} not found in script")
        for turn_idx, (speaker, raw) in enumerate(slides_data[sn], start=1):
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
                "label": f"S{sn:02d}T{turn_idx:02d}/{speaker}",
                "key": cache_key(text, voice, char, style),
            })
    return turns


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--slides", type=int, nargs="+", default=[1, 2, 3])
    p.add_argument("--force", action="store_true",
                   help="Ignore avatar cache and segment cache.")
    p.add_argument("--skip-avatars", action="store_true",
                   help="Assume avatar cache is already populated.")
    args = p.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise SystemExit(f"{tool} not in PATH")

    script_text = SCRIPT_PATH.read_text(encoding="utf-8")
    slides_data = parse_script(script_text)
    turns = build_turn_list(slides_data, args.slides)
    print(f"Slides: {args.slides}; total turns: {len(turns)}")

    # ---- Phase 1: Avatar synthesis -----------------------------------------
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if not args.skip_avatars:
        print("Phase 1: avatar batch synthesis (speaking turns)")
        token = get_aad_token()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
            list(ex.map(lambda t: synthesize_turn(token, t, args.force), turns))

    # Verify cache for all speaking turns
    for t in turns:
        cache = CACHE_DIR / f"{t['key']}.webm"
        if not cache.exists():
            raise SystemExit(f"Missing avatar cache for {t['label']}: {cache}")

    # ---- Phase 1b: idle clips ---------------------------------------------
    # v4 single-active-avatar layout no longer overlays an idle source, so we
    # skip the idle-clip synthesis entirely. The cached idle webms (if any)
    # remain on disk for potential reuse by other pipelines.
    print("Phase 1b: skipped (v4 single-active-avatar layout)")

    # ---- Phase 2: per-turn segments ----------------------------------------
    print("Phase 2: per-turn composite segments (single active avatar + crossfades)")
    SEG_DIR.mkdir(parents=True, exist_ok=True)
    for i, t in enumerate(turns):
        slide_png = SLIDE_DIR / f"slide-{t['slide']:02d}.png"
        if not slide_png.exists():
            raise SystemExit(f"Missing slide PNG: {slide_png}")
        active_webm = CACHE_DIR / f"{t['key']}.webm"
        dur = ffprobe_duration(active_webm)

        # Crossfade boundary detection: only fade in/out when the speaker
        # actually changes (or at the very first/last turn of the run).
        prev_speaker = turns[i - 1]["speaker"] if i > 0 else None
        next_speaker = turns[i + 1]["speaker"] if i + 1 < len(turns) else None
        fade_in = prev_speaker != t["speaker"]
        fade_out = next_speaker != t["speaker"]

        seg = SEG_DIR / f"{SEG_VERSION}-turn-{t['slide']:02d}-{t['turn_idx']:02d}.mp4"
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
    print("Phase 3: concat turns into per-slide segments")
    slide_segments: list[tuple[Path, float]] = []
    for sn in args.slides:
        turn_segs = [
            SEG_DIR / f"{SEG_VERSION}-turn-{t['slide']:02d}-{t['turn_idx']:02d}.mp4"
            for t in turns if t["slide"] == sn
        ]
        slide_seg = SEG_DIR / f"{SEG_VERSION}-slide-{sn:02d}.mp4"
        if len(turn_segs) == 1:
            shutil.copyfile(turn_segs[0], slide_seg)
        else:
            concat_segments(turn_segs, slide_seg)
        dur = ffprobe_duration(slide_seg)
        slide_segments.append((slide_seg, dur))
        print(f"  slide {sn}: {dur:.2f}s")

    # ---- Phase 4: final xfade chain ----------------------------------------
    print(f"Phase 4: chain {len(slide_segments)} slides with xfade -> {OUT_PATH.name}")
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    chain_with_xfade(slide_segments, OUT_PATH)

    final_dur = ffprobe_duration(OUT_PATH)
    size_mb = OUT_PATH.stat().st_size / (1024 * 1024)
    print(f"Done: {OUT_PATH}")
    print(f"  duration: {final_dur:.1f}s ({final_dur/60:.2f} min)")
    print(f"  size:     {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
