# Preparation materials

This folder holds everything used to **author** the workshop. It is not part of what an attendee or instructor consumes during delivery, and it is excluded from the published GitHub Pages site (`exclude: [prep/]` in `_config.yml`).

Workshop deliverables live in the repo root (`short\`, `long\`, `instructor\`, `assets\`).

## Contents

| Folder | Purpose |
|---|---|
| `references\` | Sanitized context pack, content decisions, AgentOps operating model notes, source materials inventory, and working backlog. |
| `tools\` | Python scripts that generate diagrams, render slides to PNG, synthesize narration via Azure AI Speech, and assemble the narrated video. |
| `short\` | Authoring notes for the short track: `slide-plan.md` (deck breakdown), `observability-plan.md`, `demo-video-plan.md`, original single-voice `speaker-script-single.md` backup, and intermediate `audio\` and `video\` artefacts (gitignored). |

## Regenerating the narrated video

The published video lives at `short\agentops-short-video.mp4` and is served as a static asset by the private GitHub Pages site. To rebuild it from `short\speaker-script.md` and `short\slides.md`:

```powershell
# 1. Sign in to Azure with the tenant that owns the Foundry/Speech resource.
az login --tenant 16b3c013-d300-468d-ac64-7eda0820b6d3

# 2. Synthesize the two voices into prep\short\audio\*.wav (one per slide).
python prep\tools\render_speech.py

# 3. Render the 23 slides to 1920x1080 PNGs in prep\short\video\.
python prep\tools\render_slides_hd.py

# 4. Assemble the final video into short\agentops-short-video.mp4.
python prep\tools\build_video.py
```

After rebuilding, keep the file under GitHub's 100 MB per-file push limit so it can be committed directly. `build_video.py` already produces a faststart MP4; if it lands above 100 MB, shrink the audio with:

```powershell
ffmpeg -y -i short\agentops-short-video.mp4 `
    -c:v copy -c:a aac -b:a 48k -ac 1 -movflags +faststart `
    short\agentops-short-video.small.mp4
Move-Item -Force short\agentops-short-video.small.mp4 short\agentops-short-video.mp4
```

Then `git add short\agentops-short-video.mp4`, commit, and push. The video is embedded at `{{ '/short/agentops-short-video.mp4' | relative_url }}` on the home page; serving it same-origin from the private Pages site is what lets the `<video>` element actually play. A GitHub Release URL would 404 in the embed because the repo is private.

Notes:

- The Speech resource has `disableLocalAuth=true`, so only Microsoft Entra ID auth works. Scripts use `AzureCliCredential` pinned to the tenant above.
- Speech token is exchanged at `https://aif-agentops-experimentation.cognitiveservices.azure.com/sts/v1.0/issuetoken`.
- Voices: `en-US-AvaMultilingualNeural` (SP1) and `en-US-AndrewMultilingualNeural` (SP2). Speaker turns are marked `**SP1:**` and `**SP2:**` in `short\speaker-script.md`.
- `ffmpeg` must be on PATH for `build_video.py`.

## Other tools

- `tools\make_diagrams.py` - regenerates SVG/PNG diagrams under `short\images\` and `assets\`.
- `tools\gen_image.py` - one-off image generation helper.
- `tools\make_transparent.py` - removes a flat background from a PNG.
- `tools\marp_to_pptx.py` - exports the Marp deck `short\slides.md` to `short\slides.pptx`.

