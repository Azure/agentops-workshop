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

The published video lives at `short\agentops-short-video.mp4` (distributed via GitHub Release). To rebuild it from `short\speaker-script.md` and `short\slides.md`:

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

After rebuilding, publish the video as a GitHub Release asset so the Pages download link keeps working:

```powershell
gh release create v0.1.1-short short\agentops-short-video.mp4 `
    --title "Short workshop kit (v0.1.1)" `
    --notes "Updated narrated video."
```

Notes:

- The Speech resource has `disableLocalAuth=true`, so only Microsoft Entra ID auth works. Scripts use `AzureCliCredential` pinned to the tenant above.
- Speech token is exchanged at `https://aif-agentops-experimentation.cognitiveservices.azure.com/sts/v1.0/issuetoken`.
- Voices: `en-US-AndrewMultilingualNeural` (M) and `en-US-AvaMultilingualNeural` (F). Speaker turns are marked `**M:**` and `**F:**` in `short\speaker-script.md`.
- `ffmpeg` must be on PATH for `build_video.py`.

## Other tools

- `tools\make_diagrams.py` - regenerates SVG/PNG diagrams under `short\images\` and `assets\`.
- `tools\gen_image.py` - one-off image generation helper.
- `tools\make_transparent.py` - removes a flat background from a PNG.
- `tools\marp_to_pptx.py` - exports the Marp deck `short\slides.md` to `short\slides.pptx`.

