# Preparation materials

This folder holds everything used to **author** the workshop. It is not part of what an attendee or instructor consumes during delivery, and it is excluded from the published GitHub Pages site (`exclude: [prep/]` in `_config.yml`).

Workshop deliverables live in the repo root (`1-hour\`, `8-hour\`, `instructor\`, `assets\`).

## Contents

| Folder | Purpose |
|---|---|
| `references\` | Sanitized context pack, content decisions, AgentOps operating model notes, source materials inventory, and working backlog. |
| `tools\` | Python scripts that generate diagrams, render slides to PNG, synthesize narration via Azure AI Speech, and assemble the narrated video. |
| `1-hour\` | Authoring notes for the 1-hour track: `slide-plan.md` (deck breakdown), `observability-plan.md`, `demo-video-plan.md`, original single-voice `speaker-script-single.md` backup, and intermediate `audio\` and `video\` artefacts (gitignored). |

## Regenerating the narrated video

The published video lives at `1-hour\agentops-1hour-video.mp4`. To rebuild it from `1-hour\speaker-script.md` and `1-hour\slides.md`:

```powershell
# 1. Sign in to Azure with the tenant that owns the Foundry/Speech resource.
az login --tenant 16b3c013-d300-468d-ac64-7eda0820b6d3

# 2. Synthesize the two voices into prep\1-hour\audio\*.wav (one per slide).
python prep\tools\render_speech.py

# 3. Render the 23 slides to 1920x1080 PNGs in prep\1-hour\video\.
python prep\tools\render_slides_hd.py

# 4. Assemble the final video into 1-hour\agentops-1hour-video.mp4.
python prep\tools\build_video.py
```

Notes:

- The Speech resource has `disableLocalAuth=true`, so only Microsoft Entra ID auth works. Scripts use `AzureCliCredential` pinned to the tenant above.
- Speech token is exchanged at `https://aif-agentops-experimentation.cognitiveservices.azure.com/sts/v1.0/issuetoken`.
- Voices: `en-US-AndrewMultilingualNeural` (M) and `en-US-AvaMultilingualNeural` (F). Speaker turns are marked `**M:**` and `**F:**` in `1-hour\speaker-script.md`.
- `ffmpeg` must be on PATH for `build_video.py`.

## Other tools

- `tools\make_diagrams.py` - regenerates SVG/PNG diagrams under `1-hour\images\` and `assets\`.
- `tools\gen_image.py` - one-off image generation helper.
- `tools\make_transparent.py` - removes a flat background from a PNG.
- `tools\marp_to_pptx.py` - exports the Marp deck `1-hour\slides.md` to `1-hour\slides.pptx`.
