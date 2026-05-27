#!/usr/bin/env python3
"""Render the 23-slide deck PDF into 1920x1080 PNGs for video assembly.

Strategy: render each PDF page at scale 4.0 (= 3840x2160 for a 16:9 deck),
then downsample with Lanczos to 1920x1080. This keeps text sharp.

The PDF is produced by LibreOffice from 1-hour/slides.pptx; if missing, this
script re-runs the conversion.

Usage:
    python render_slides_hd.py                 # render all missing PNGs
    python render_slides_hd.py --force         # re-render everything
    python render_slides_hd.py --slides 4 7    # specific pages only
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image

REPO = Path(__file__).resolve().parent.parent.parent
PPTX = REPO / "1-hour" / "slides.pptx"
PDF_DIR = Path(os.environ.get("TEMP", "/tmp")) / "pptx-preview"
PDF_PATH = PDF_DIR / "slides.pdf"
OUT_DIR = REPO / "prep" / "1-hour" / "video"

TARGET_W = 1920
TARGET_H = 1080
RENDER_SCALE = 4.0


def ensure_pdf(force: bool = False) -> Path:
    if PDF_PATH.exists() and not force:
        return PDF_PATH
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    soffice = shutil.which("soffice") or r"C:\Program Files\LibreOffice\program\soffice.exe"
    if not Path(soffice).exists():
        print(f"LibreOffice not found at {soffice}", file=sys.stderr)
        sys.exit(2)
    print(f"Converting {PPTX.name} -> PDF via LibreOffice...")
    subprocess.run(
        [soffice, "--headless", "--convert-to", "pdf",
         "--outdir", str(PDF_DIR), str(PPTX)],
        check=True,
    )
    if not PDF_PATH.exists():
        print(f"PDF not produced at {PDF_PATH}", file=sys.stderr)
        sys.exit(2)
    return PDF_PATH


def render_page(pdf: pdfium.PdfDocument, page_index: int, out_path: Path) -> None:
    page = pdf[page_index]
    pil = page.render(scale=RENDER_SCALE).to_pil()
    # Convert to RGB (Pillow Lanczos requires non-paletted)
    if pil.mode != "RGB":
        pil = pil.convert("RGB")
    # Pillow >= 10 uses Image.Resampling.LANCZOS
    resample = getattr(Image, "Resampling", Image).LANCZOS
    pil = pil.resize((TARGET_W, TARGET_H), resample)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pil.save(out_path, "PNG", optimize=True)
    page.close()
    print(f"  -> {out_path.name}  ({out_path.stat().st_size/1024:,.0f} KB)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slides", type=int, nargs="*",
                   help="1-based slide numbers (default: all).")
    p.add_argument("--force", action="store_true",
                   help="Re-render even if PNG exists.")
    p.add_argument("--rebuild-pdf", action="store_true",
                   help="Re-run LibreOffice even if PDF cached.")
    args = p.parse_args()

    pdf_path = ensure_pdf(force=args.rebuild_pdf)
    pdf = pdfium.PdfDocument(str(pdf_path))
    n_pages = len(pdf)
    print(f"PDF: {pdf_path} ({n_pages} pages)")

    pages = args.slides or list(range(1, n_pages + 1))

    for slide_num in pages:
        idx = slide_num - 1
        if idx < 0 or idx >= n_pages:
            print(f"Slide {slide_num}: out of range, skipping.")
            continue
        out_path = OUT_DIR / f"slide-{slide_num:02d}.png"
        if out_path.exists() and not args.force:
            print(f"Slide {slide_num:02d}: exists, skipping ({out_path.stat().st_size/1024:,.0f} KB).")
            continue
        print(f"Slide {slide_num:02d}: rendering at scale {RENDER_SCALE}")
        render_page(pdf, idx, out_path)

    pdf.close()


if __name__ == "__main__":
    main()
