#!/usr/bin/env python3
"""Assemble the narrated AgentOps video from per-slide PNGs and WAVs.

Two phases:
  Phase A: for each slide, build a per-slide MP4 segment
           (looped PNG @ 1920x1080@30fps + audio with 0.3s silent lead/tail).
  Phase B: chain all 23 segments with ffmpeg `xfade` (video) and
           `acrossfade` (audio) for smooth transitions; output a single MP4.

Per-slide segments are cached under prep/short/video/segments/.
The final file is written to short/agentops-short-video.mp4.

Usage:
    python build_video.py                       # build everything that's missing
    python build_video.py --rebuild-segments    # re-encode each per-slide MP4
    python build_video.py --final-only          # skip segments; just chain
    python build_video.py --xfade-dur 0.5       # crossfade duration in seconds
    python build_video.py --pad 0.3             # silent lead/tail per slide
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
AUDIO_DIR = REPO / "prep" / "short" / "audio"
SLIDE_DIR = REPO / "prep" / "short" / "video"
SEG_DIR = SLIDE_DIR / "segments"
OUT_PATH = REPO / "short" / "agentops-short-video.mp4"

FPS = 30
WIDTH = 1920
HEIGHT = 1080


def ffprobe_duration(path: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(json.loads(r.stdout)["format"]["duration"])


def build_segment(slide_num: int, pad: float, force: bool) -> tuple[Path, float]:
    png = SLIDE_DIR / f"slide-{slide_num:02d}.png"
    wav = AUDIO_DIR / f"slide-{slide_num:02d}.wav"
    out = SEG_DIR / f"seg-{slide_num:02d}.mp4"
    if not png.exists():
        raise SystemExit(f"Missing {png}")
    if not wav.exists():
        raise SystemExit(f"Missing {wav}")

    audio_dur = ffprobe_duration(wav)
    total = audio_dur + 2 * pad

    if out.exists() and not force:
        existing_dur = ffprobe_duration(out)
        if abs(existing_dur - total) < 0.05:
            print(f"  seg-{slide_num:02d}: cached ({existing_dur:.2f}s)")
            return out, existing_dur

    SEG_DIR.mkdir(parents=True, exist_ok=True)
    # Looped still image as video; audio padded with adelay (lead) + apad (tail).
    # -t bounds the whole segment so apad's infinite silence is trimmed.
    pad_ms = int(round(pad * 1000))
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-r", str(FPS), "-i", str(png),
        "-i", str(wav),
        "-filter_complex",
        f"[0:v]scale={WIDTH}:{HEIGHT}:flags=lanczos,setsar=1,format=yuv420p[v];"
        f"[1:a]adelay={pad_ms}|{pad_ms},apad,aresample=async=1[a]",
        "-map", "[v]", "-map", "[a]",
        "-t", f"{total:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(out),
    ]
    print(f"  seg-{slide_num:02d}: encoding {total:.2f}s ({audio_dur:.2f}s audio + 2x{pad:.2f}s pad)")
    subprocess.run(cmd, check=True)
    return out, total


def build_segments(pad: float, force: bool) -> list[tuple[Path, float]]:
    print("Phase A: building per-slide segments")
    segs = []
    for n in range(1, 24):
        segs.append(build_segment(n, pad, force))
    total = sum(d for _, d in segs)
    print(f"Total segment duration: {total:.1f}s ({total/60:.2f} min)")
    return segs


def chain_with_xfade(segs: list[tuple[Path, float]], xfade_dur: float) -> None:
    """Single ffmpeg invocation that xfades+acrossfades all segments."""
    print(f"Phase B: chaining {len(segs)} segments with xfade={xfade_dur}s")

    inputs = []
    for path, _ in segs:
        inputs += ["-i", str(path)]

    filters = []
    # Normalize each input so xfade gets matching streams
    for i, (_, dur) in enumerate(segs):
        filters.append(
            f"[{i}:v]fps={FPS},scale={WIDTH}:{HEIGHT}:flags=lanczos,"
            f"setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v{i}]"
        )
        filters.append(f"[{i}:a]asetpts=PTS-STARTPTS[a{i}]")

    cumulative = segs[0][1]
    vlabel = "v0"
    alabel = "a0"
    for i in range(1, len(segs)):
        offset = cumulative - xfade_dur
        new_v = f"vx{i}"
        new_a = f"ax{i}"
        filters.append(
            f"[{vlabel}][v{i}]xfade=transition=fade:duration={xfade_dur}:"
            f"offset={offset:.3f}[{new_v}]"
        )
        filters.append(
            f"[{alabel}][a{i}]acrossfade=d={xfade_dur}:c1=tri:c2=tri[{new_a}]"
        )
        cumulative = cumulative + segs[i][1] - xfade_dur
        vlabel = new_v
        alabel = new_a

    print(f"Expected final duration: {cumulative:.1f}s ({cumulative/60:.2f} min)")

    filter_complex = ";".join(filters)
    cmd = [
        "ffmpeg", "-y", "-loglevel", "info",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", f"[{vlabel}]", "-map", f"[{alabel}]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(OUT_PATH),
    ]
    print(f"Encoding -> {OUT_PATH.name} (this may take a few minutes)")
    subprocess.run(cmd, check=True)
    final_dur = ffprobe_duration(OUT_PATH)
    size_mb = OUT_PATH.stat().st_size / (1024 * 1024)
    print(f"Done: {OUT_PATH}")
    print(f"  duration: {final_dur:.1f}s ({final_dur/60:.2f} min)")
    print(f"  size:     {size_mb:.1f} MB")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--rebuild-segments", action="store_true",
                   help="Re-encode each per-slide MP4 even if cached.")
    p.add_argument("--final-only", action="store_true",
                   help="Skip segment build; just chain (must exist).")
    p.add_argument("--xfade-dur", type=float, default=0.5)
    p.add_argument("--pad", type=float, default=0.3,
                   help="Silent lead/tail per slide (seconds).")
    args = p.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        print("ffmpeg/ffprobe not in PATH", file=sys.stderr)
        sys.exit(2)

    if args.final_only:
        segs = []
        for n in range(1, 24):
            p_ = SEG_DIR / f"seg-{n:02d}.mp4"
            if not p_.exists():
                print(f"Missing {p_}; run without --final-only first.", file=sys.stderr)
                sys.exit(2)
            segs.append((p_, ffprobe_duration(p_)))
    else:
        segs = build_segments(args.pad, args.rebuild_segments)

    chain_with_xfade(segs, args.xfade_dur)


if __name__ == "__main__":
    main()
