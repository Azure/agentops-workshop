"""Probe: does the Azure TTS Avatar batch API accept SSML with long leading/
tailing silence bracketing a tiny utterance? If yes, we can capture the avatar
in its NATIVE idle state (the same idle motion the Live Avatar shows when not
being asked to speak) and loop it as the silent-listener overlay.

Usage:
    python probe_idle_ssml.py            # tests Ava (Lisa)
    python probe_idle_ssml.py harry      # tests Andrew (Harry)
"""
from __future__ import annotations

import json
import sys
import time
import uuid
from pathlib import Path

import requests
from azure.identity import AzureCliCredential

TENANT_ID = "16b3c013-d300-468d-ac64-7eda0820b6d3"
HOST = "aif-agentops-experimentation.cognitiveservices.azure.com"
API = f"https://{HOST}/avatar/batchsyntheses"
API_VERSION = "2024-08-01"
SCOPE = "https://cognitiveservices.azure.com/.default"
BG = "#00B140FF"

CHARS = {
    "lisa": ("en-US-AvaMultilingualNeural", "lisa", "casual-sitting"),
    "harry": ("en-US-AndrewMultilingualNeural", "harry", "business"),
}

# Try a few candidate SSML payloads. Longest leading silence we'd ideally
# want is ~15s so a typical silent-listener period of 4-10s never has to
# loop. We'll start with that and back off if rejected.
PAYLOADS = [
    ("leading10s+hm+tailing10s",
     '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
     'xmlns:mstts="http://www.w3.org/2001/mstts" version="1.0" xml:lang="en-US">'
     '<voice name="{voice}">'
     '<mstts:silence type="Leading-exact" value="10000ms"/>'
     '<prosody volume="x-soft">Mm.</prosody>'
     '<mstts:silence type="Tailing-exact" value="10000ms"/>'
     '</voice></speak>'),

    ("leading5s+hm+tailing5s",
     '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
     'xmlns:mstts="http://www.w3.org/2001/mstts" version="1.0" xml:lang="en-US">'
     '<voice name="{voice}">'
     '<mstts:silence type="Leading-exact" value="5000ms"/>'
     '<prosody volume="x-soft">Mm.</prosody>'
     '<mstts:silence type="Tailing-exact" value="5000ms"/>'
     '</voice></speak>'),

    ("breaks_only_5s",
     '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
     'xmlns:mstts="http://www.w3.org/2001/mstts" version="1.0" xml:lang="en-US">'
     '<voice name="{voice}">'
     '<break time="5000ms"/>'
     '<prosody volume="x-soft">Mm.</prosody>'
     '<break time="5000ms"/>'
     '</voice></speak>'),

    ("just_breath_chain",
     '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
     'xmlns:mstts="http://www.w3.org/2001/mstts" version="1.0" xml:lang="en-US">'
     '<voice name="{voice}">'
     '<prosody volume="x-soft">Mm.</prosody>'
     '<break time="5000ms"/>'
     '<prosody volume="x-soft">Mm.</prosody>'
     '<break time="5000ms"/>'
     '<prosody volume="x-soft">Mm.</prosody>'
     '</voice></speak>'),
]


def get_token() -> str:
    cred = AzureCliCredential(tenant_id=TENANT_ID)
    return cred.get_token(SCOPE).token


def submit(token: str, ssml: str, char: str, style: str) -> tuple[str, int, str]:
    job_id = str(uuid.uuid4())
    body = {
        "inputKind": "SSML",
        "inputs": [{"content": ssml}],
        "avatarConfig": {
            "talkingAvatarCharacter": char,
            "talkingAvatarStyle": style,
            "videoFormat": "webm",
            "videoCodec": "vp9",
            "subtitleType": "none",
            "backgroundColor": BG,
        },
    }
    url = f"{API}/{job_id}?api-version={API_VERSION}"
    r = requests.put(url, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }, data=json.dumps(body), timeout=30)
    return job_id, r.status_code, r.text


def poll(token: str, job_id: str) -> dict:
    url = f"{API}/{job_id}?api-version={API_VERSION}"
    for _ in range(120):
        r = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
        r.raise_for_status()
        data = r.json()
        st = data.get("status")
        if st in ("Succeeded", "Failed"):
            return data
        time.sleep(2)
    raise RuntimeError("poll timeout")


def main() -> int:
    char_key = sys.argv[1] if len(sys.argv) > 1 else "lisa"
    voice, char, style = CHARS[char_key]
    token = get_token()
    out_dir = Path("prep/short/avatar-cache")
    out_dir.mkdir(parents=True, exist_ok=True)

    for label, tmpl in PAYLOADS:
        ssml = tmpl.format(voice=voice)
        print(f"--- {label} ---")
        job_id, code, body = submit(token, ssml, char, style)
        if code >= 400:
            print(f"  REJECTED at submit: HTTP {code}: {body[:300]}")
            continue
        try:
            data = poll(token, job_id)
        except Exception as e:
            print(f"  POLL ERROR: {e}")
            continue
        if data.get("status") != "Succeeded":
            err = json.dumps(data.get("properties", {}).get("error", data), indent=2)[:500]
            print(f"  FAILED: {err}")
            continue
        url = data["outputs"]["result"]
        out = out_dir / f"probe-{char_key}-{label}.webm"
        with requests.get(url, stream=True, timeout=120) as r:
            r.raise_for_status()
            with open(out, "wb") as f:
                for chunk in r.iter_content(64 * 1024):
                    f.write(chunk)
        print(f"  OK -> {out} ({out.stat().st_size/1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
