# Changelog

## Unreleased

- Fix the Marp -> PPTX converter so it stops rendering Markdown blockquote subtitles with a literal leading `>` and so slides with both a blockquote subtitle and an inline diagram push the image down to `Inches(2.3)` to avoid overlapping the subtitle textbox (`prep/tools/marp_to_pptx.py`: `_extract_body_text` strips the prefix, both inline-diagram and IMAGE_MAP-diagram paths respect `has_body`).
- Register `agentops-four-pillars.png` in `DIAGRAM_IMAGES` so the operating-model visual renders centered and full-width instead of as a tiny stock-photo thumbnail in the top-right corner.
- Replace the six-step operating loop (`Evaluate, Gate, Observe, Diagnose, Ship, Improve`) with a single four-pillar model (`Evaluate -> Ship -> Observe -> Own`) as the primary AgentOps story across the short track. Old loop items map as Gate+Ship -> Ship and Diagnose+Improve -> Own.
- Update `short/slides.md`: retitle the operating-model slide and its visual, rename the Evaluation/CI-CD/Observability/Day-2 section dividers to Evaluate/Ship/Observe/Own, rewrite affected speaker notes, and reframe the 30-day adoption path around the four pillars.
- Add the `agentops-four-pillars` diagram to `prep/tools/make_diagrams.py` and render `short/images/agentops-four-pillars.png`; the slide no longer uses `operating-loop.png`.
- Update `short/speaker-script.md`, `short/agenda.md`, `short/run-of-show.md`, and `short/index.md` so the narration and delivery materials present the four-pillar model consistently.
- Regenerate `short/slides.pptx` from the updated `slides.md`.
- Follow-up needed: `short/agentops-short-video.mp4` is now out of sync with the revised script and should be re-rendered via `build_production_video.py` + `compress_production_video.py`, and the deck mirrored to upstream `presentations/04-agentops/`.

## v0.2.0

- Regenerate `short/agentops-short-video.mp4` with the new mixed-mode avatar staging (Lisa SP1 bottom-left, Harry SP2 bottom-right). Intro slides 1-3 keep the per-turn jogral handoff with a 0.4s alpha crossfade at every SP1/SP2 change; core slides 4-23 use a single merged-SSML super-turn per slide rendered by one alternating speaker (slide 4 = SP2, alternating to slide 23 = SP1), with 350 ms `<break>` pauses preserving the original turn cadence. Slide-to-slide handoffs use the existing 0.5 s `xfade` plus `acrossfade`; the avatar alpha fade is suppressed at slide boundaries to avoid a double-fade ghosting effect.
- Add `prep/tools/build_production_video.py` (production builder reusing v4 helpers from `build_preview.py`), `prep/tools/compress_production_video.py` (size-ladder re-encoder that drops the raw build under the 100 MB push limit), and `synthesize_turn` SSML support in `build_preview.py`.
- Document the new "intro-jogral + core-merged-per-slide" production convention in `.github/copilot-instructions.md` so future regenerations and the long-workshop video build follow the same staging without re-litigating it.
- Embed the narrated video directly from the Pages site instead of from the private GitHub Release. Private releases are not reachable by an HTML `<video>` element (cross-origin to `github.com` without credentials returns 404), so the embedded player on the home page was empty for every visitor, including signed-in Azure members.
- Compress `short/agentops-short-video.mp4` (101 MB AAC 100 kbps stereo audio metadata -> 85 MB AAC 48 kbps mono audio, video stream copied) so it fits under GitHub's 100 MB per-file push limit and can be committed to the repo.
- Stop ignoring `short/agentops-short-video.mp4` and serve it as a static Pages asset (`{{ '/short/agentops-short-video.mp4' | relative_url }}`). This keeps the video private (same-origin to the private Pages site) without depending on the GitHub Release URL.
- Update the "Narrated video" download card on `index.md` and `short/index.md` to point at the same in-repo asset; refresh the size hint to 69 MB after the v0.2.0 1080p CRF 28 re-encode.

## v0.1.0

- Created the GitHub Pages workshop structure.
- Added the short workshop planning track.
- Added the long workshop planning track.
- Added lab planning placeholders, including a dedicated observability lab.
