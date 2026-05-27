#!/usr/bin/env python3
"""Generate an image with Azure OpenAI gpt-image-* and save as PNG.

Auth: uses Azure AD (azure-identity) — same identity you already have via `az login`.

Usage:
    python gen_image.py --prompt "..." --out path/to/file.png
                        [--size 1536x1024] [--quality high]
                        [--deployment gpt-image-1]
"""

from __future__ import annotations

import argparse
import base64
import os
import sys
import time
from pathlib import Path

import requests
from azure.identity import DefaultAzureCredential

ENDPOINT = os.environ.get(
    "AZURE_OPENAI_ENDPOINT",
    "https://aif-agentops-experimentation.openai.azure.com",
)
API_VERSION = "2025-04-01-preview"
SCOPE = "https://cognitiveservices.azure.com/.default"


def generate(prompt: str, out_path: Path, size: str = "1536x1024",
             quality: str = "high", deployment: str = "gpt-image-1",
             background: str = "auto") -> None:
    cred = DefaultAzureCredential()
    token = cred.get_token(SCOPE).token

    url = (
        f"{ENDPOINT}/openai/deployments/{deployment}/images/generations"
        f"?api-version={API_VERSION}"
    )
    payload = {
        "prompt": prompt,
        "n": 1,
        "size": size,
        "quality": quality,
        "output_format": "png",
        "background": background,
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print(f"POST {url}")
    print(f"  size={size}  quality={quality}  bg={background}")
    print(f"  prompt: {prompt[:120]}{'...' if len(prompt) > 120 else ''}")

    t0 = time.time()
    r = requests.post(url, headers=headers, json=payload, timeout=600)
    elapsed = time.time() - t0
    print(f"  -> {r.status_code} in {elapsed:.1f}s")

    if r.status_code != 200:
        print(r.text[:2000])
        sys.exit(2)

    data = r.json()
    b64 = data["data"][0].get("b64_json")
    if not b64:
        print("No b64_json in response:")
        print(str(data)[:1000])
        sys.exit(3)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(base64.b64decode(b64))
    print(f"  saved: {out_path}  ({out_path.stat().st_size:,} bytes)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--size", default="1536x1024",
                   choices=["1024x1024", "1024x1536", "1536x1024"])
    p.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    p.add_argument("--deployment", default="gpt-image-1")
    p.add_argument("--background", default="auto",
                   choices=["auto", "transparent", "opaque"])
    args = p.parse_args()
    generate(args.prompt, args.out, args.size, args.quality,
             args.deployment, args.background)


if __name__ == "__main__":
    main()
