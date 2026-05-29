#!/usr/bin/env python3
"""Compress the production video to fit under GitHub's 100 MB per-file limit.

The raw build from ``build_production_video.py`` is high-quality (CRF 20 at
1080p with 192 kbps stereo audio) and lands around 250-400 MB. The repo
convention is to commit the narrated video directly so the Pages embed
works (private GitHub Release URLs return 404 to ``<video>`` elements
cross-origin from pages.github.io to github.com -- see CHANGELOG entry
"Serve narrated video from the Pages site to fix empty embed").

This script ladders CRF/resolution presets until the file is comfortably
under ``--target-mb`` (default 90 MB so we keep margin under the 100 MB
push limit and account for git LFS pointers etc). It picks the first
preset that fits and stops; you can also force a specific preset with
``--preset 1080p-crf30``.

Ladder (best quality first):
    1. 1080p CRF 28 slow, audio 48 kbps mono
    2. 1080p CRF 30 slow, audio 48 kbps mono
    3. 1080p CRF 32 slow, audio 40 kbps mono
    4. 720p  CRF 28 slow, audio 48 kbps mono
    5. 720p  CRF 30 slow, audio 40 kbps mono

Usage::

    python compress_production_video.py
    python compress_production_video.py --in short/agentops-short-video.mp4 \
        --out short/agentops-short-video.mp4 --target-mb 90
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent.parent
DEFAULT_IN = REPO / "short" / "agentops-short-video.mp4"
DEFAULT_OUT = REPO / "short" / "agentops-short-video.mp4"


PRESETS = [
    ("1080p-crf28", "1920", "1080", "28", "48k"),
    ("1080p-crf30", "1920", "1080", "30", "48k"),
    ("1080p-crf32", "1920", "1080", "32", "40k"),
    ("720p-crf28", "1280", "720", "28", "48k"),
    ("720p-crf30", "1280", "720", "30", "40k"),
]


def file_mb(p: Path) -> float:
    return p.stat().st_size / (1024 * 1024)


def encode(src: Path, dst: Path, width: str, height: str,
           crf: str, audio_kbps: str) -> None:
    vf = (
        f"scale={width}:{height}:flags=lanczos,"
        "setsar=1,format=yuv420p"
    )
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(src),
        "-vf", vf,
        "-c:v", "libx264", "-preset", "slow", "-crf", crf,
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", audio_kbps, "-ac", "1",
        "-movflags", "+faststart",
        str(dst),
    ]
    subprocess.run(cmd, check=True)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--in", dest="src", default=str(DEFAULT_IN),
                   help=f"Input MP4 (default: {DEFAULT_IN}).")
    p.add_argument("--out", dest="dst", default=str(DEFAULT_OUT),
                   help=f"Output MP4 (default: {DEFAULT_OUT}; in-place).")
    p.add_argument("--target-mb", type=float, default=90.0,
                   help="Target max size in MB (default: 90.0).")
    p.add_argument("--preset", default=None,
                   help="Force a specific preset id (skip the ladder).")
    args = p.parse_args()

    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg not in PATH")

    src = Path(args.src)
    dst = Path(args.dst)
    if not src.exists():
        raise SystemExit(f"Input not found: {src}")

    orig_mb = file_mb(src)
    print(f"Input:    {src} ({orig_mb:.1f} MB)")
    print(f"Target:   <= {args.target_mb:.1f} MB")

    # If the in-place case, encode to a temp file and only move at the end
    # so we never lose the source mid-encode.
    inplace = src.resolve() == dst.resolve()
    work_dir = dst.parent
    work_dir.mkdir(parents=True, exist_ok=True)

    presets = PRESETS
    if args.preset is not None:
        presets = [pr for pr in PRESETS if pr[0] == args.preset]
        if not presets:
            raise SystemExit(f"Unknown preset {args.preset!r}; "
                             f"valid: {', '.join(p[0] for p in PRESETS)}")

    chosen = None
    for pid, w, h, crf, akbps in presets:
        tmp = work_dir / f".compress-{pid}.mp4"
        print(f"\nTry preset {pid} ({w}x{h} crf={crf} a={akbps} mono)")
        encode(src, tmp, w, h, crf, akbps)
        mb = file_mb(tmp)
        print(f"  -> {mb:.1f} MB")
        if mb <= args.target_mb or args.preset is not None:
            chosen = (pid, tmp, mb)
            break
        tmp.unlink(missing_ok=True)

    if chosen is None:
        raise SystemExit(
            "No preset reached the target size. Consider lowering "
            "--target-mb (last resort) or publishing externally."
        )

    pid, tmp, mb = chosen
    if inplace:
        backup = src.with_suffix(src.suffix + ".bak")
        if backup.exists():
            backup.unlink()
        src.replace(backup)
        try:
            tmp.replace(dst)
            backup.unlink(missing_ok=True)
        except Exception:
            backup.replace(src)
            raise
    else:
        tmp.replace(dst)

    final_mb = file_mb(dst)
    print(f"\nDone: {dst}")
    print(f"  preset:   {pid}")
    print(f"  size:     {final_mb:.1f} MB (was {orig_mb:.1f} MB)")


if __name__ == "__main__":
    main()
