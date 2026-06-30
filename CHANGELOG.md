# Changelog

## Unreleased

This update rebuilds the full-day VBD track from a facilitator planning skeleton into seven true hands-on labs that carry one live Microsoft Foundry agent through the complete AgentOps operating model.

### Highlights

- **From tabletop to keyboard.** The seven VBD labs are now step-by-step, beginner-proof, hands-on labs with exact commands and exact portal clicks, instead of high-level design exercises.
- **One agent, end to end.** Every lab builds on the same running example, the Contoso Travel Agent, and consumes the artifact the previous lab produced, so attendees experience the operating model as one continuous story.
- **Grounded in the real accelerator.** Commands use the public Azure AgentOps accelerator (PyPI `agentops-accelerator`, CLI `agentops`) and Microsoft Foundry, so the loop Evaluate, Ship, Observe, Operate is tangible on a live agent.
- **A continuity spine you can verify.** Dataset, baseline, regression versions, evidence pack, telemetry, governance, and trace promotion flow through fixed file paths and agent versions from Lab 1 to the capstone.
- **A working CI/CD gate.** The capstone generates a GitHub Actions pull request gate that blocks a regressed agent version before merge and publishes a release evidence pack.

### Content - AgentOps VBD Workshop (Paulo Lacerda)

- Rewrite Labs 1 through 6 and the capstone as hands-on labs grounded in `Azure/agentops` and Microsoft Foundry, replacing the previous design-exercise framing.
- Lock a continuity spine around the Contoso Travel Agent (`travel-agent:1/:2/:3`), a shared `agentops-vbd/` workspace, and fixed paths `.agentops/data/travel-smoke.jsonl`, `.agentops/baseline/results.json`, and `.agentops/release/latest/evidence.md`.
- Lab 1 installs the accelerator, signs in to Azure, creates the Foundry Prompt Agent, and runs `agentops init`; Lab 2 builds the JSONL eval dataset, thresholds, first `agentops eval run`, and a green baseline.
- Lab 3 ships a deliberately regressed `travel-agent:2`, proves the gate fails with exit code `2` against the baseline, and produces a Doctor evidence pack; Lab 4 enables Foundry and Application Insights tracing, imports telemetry, opens Cockpit as the local command center, and flags a bad trace.
- Lab 5 adds a content-safety evaluator, governance assertions, and a red-team pass; Lab 6 promotes the flagged production trace back into the dataset and refreshes the baseline.
- Capstone generates a GitHub Actions pull request gate, demonstrates a green pass and a red regression block, and assembles the final production-readiness evidence and ship decision.
- Rewrite `long/labs/index.md` and `long/lab-roadmap.md` to a hands-on framing with the running example, a build-and-artifact table, the continuity spine, and a prerequisites checklist.

### Follow-up

- Mirror the hands-on VBD labs and updated roadmap into the upstream `presentations/04-agentops/` materials when that private repo is reachable.

## v0.3.0 - 2026-06-29

This update brings the short workshop deck up to date with the latest speaker-flow, demo, Build 2026, and slide-generation changes while tightening release-rollout language for AgentOps delivery.

### Highlights

- **Updated 26-slide short deck flow.** The short deck now includes a dedicated Demo slide and closing Thank You slide, with the maturity model moved after the operating model.
- **Cleaner architecture narration.** Slide 10 now reads as a story that follows one agent version from inner-loop authoring to production feedback, instead of listing every box in the diagram.
- **Clearer rollout terminology.** Production rollout language now uses blue-green or canary rollout for safe release, reserving A/B testing for true comparative experiments.
- **Build 2026 alignment.** Speaker notes now reference ASSERT, ACS, Adaptive Evaluations context, and Microsoft Agent 365 where they support the AgentOps operating model.
- **Standalone AgentOps branding.** The short deck and narrated video now open as an AgentOps Workshop, without parent-program wording.
- **Consistent four-pillar site copy.** The GitHub Pages landing page and instructor guide now use Evaluate, Ship, Observe, Operate instead of the older six-step loop.
- **Cleaner track names.** The public site now labels the one-hour session as AgentOps Briefing and the VBD track as AgentOps Value Delivery Workshop.

### Content - Short workshop deck flow (Richard Healy)

- Add a dedicated `Demo` slide to the short deck and update the speaker script timing table to account for the demo block.
- Move the `Maturity model` slide after the `AgentOps operating model` so the foundations story flows from model to team self-assessment.
- Refresh speaker notes and transcript language for readability, timing, and current Build 2026 announcements.

### Content - Architecture and speaker script (Paulo Lacerda)

- Rewrite the slide 10 `AgentOps Architecture` speaker script as a narrative walkthrough of one agent version moving from sandbox authoring through dev, qa, prod, observability, and feedback into the next evaluation cycle.
- Update slide 10 timing to the measured 4:30 delivery and recalculate downstream running totals in `short/speaker-script.md`.
- Remove published speaker-name suggestions from `short/speaker-script.md`; the public script now keeps only SP1, SP2, and SP3 markers.
- Replace ambiguous production rollout wording that mixed A/B testing with canary release semantics. The architecture notes and script now refer to smoke tests plus blue-green or canary rollout for controlled production exposure.
- Rebrand the short deck title slide as `AgentOps` and remove visible parent-program wording from the short-track deck source.

### Content - Long workshop positioning (Paulo Lacerda)

- Clarify the long workshop as the VBD version across the public landing pages.

### Content - GitHub Pages site (Paulo Lacerda)

- Update the landing page and instructor delivery guide to describe the current four-pillar AgentOps model: `Evaluate -> Ship -> Observe -> Operate`.
- Rename the published workshop tracks to `AgentOps Briefing` and `AgentOps Value Delivery Workshop`, with the side navigation using `AgentOps VBD Workshop` for the full-day track.

### Diagrams

- Regenerate short-track diagrams with improved sizing and readability after the deck-generation updates. (Richard Healy)
- Fix word wrapping in the Foundry architecture diagram. (Richard Healy)
- Regenerate `short/images/agentops-four-pillars.png` so the diagram shows the renamed `Operate` pillar. (Paulo Lacerda)

### Tooling - Marp -> PPTX converter (Richard Healy)

- Update the PowerPoint generation pipeline to fix multiple formatting issues and improve generated slide layout fidelity.

### Tooling - Marp -> PPTX converter (Paulo Lacerda)

- Rename the legacy `A/B Testing Agent Configurations` image mapping to `Canary Rollout for Agent Configurations` so future generated decks use rollout terminology consistently.

### Tooling - Video production pipeline (Paulo Lacerda)

- Update `prep/tools/render_speech.py` so the speaker parser preserves multi-paragraph speaker turns after readability formatting in `short/speaker-script.md`.
- Update `prep/tools/build_production_video.py` to render the full 30-slide short deck, follow the scripted two-speaker assignment per slide, and insert the four demo videos from `short/videos/` directly after their demo intro slides.

### Tooling - Release notes convention (Paulo Lacerda)

- Document the release-notes-style CHANGELOG convention in `.github/copilot-instructions.md` so future updates retain intro, Highlights, attributed content sections, diagrams, tooling, artefacts, and follow-up structure.

### Tooling - GitHub Pages styling (Paulo Lacerda)

- Hide the default Just the Docs attribution footer from the left navigation.

### Artefacts

- Regenerate `short/slides.pptx` from the updated `short/slides.md`.
- Regenerate `short/agentops-short-video.mp4` from the two-speaker script, with embedded demo videos after the Evaluate, Ship, Observe, and Operate demo intro slides.
- Regenerate `short/slides.pptx` and `short/agentops-short-video.mp4` again after removing parent-program branding from the opening slide.
- Regenerate `short/slides.pptx` once more after the `Own` -> `Operate` pillar rename so the section-divider slides match the rest of the materials.
- Add the four source demo clips under `short/videos/` so the production video can be rebuilt reproducibly.

### Follow-up

- Mirror the updated deck to the upstream program repo at `presentations/04-agentops/`. (PR opened: private-program-owner/prod-readiness-workshop#2.)
- Author the full-day VBD workshop content (`long/slides.md`, `long/labs/lab-01..06`, `long/labs/capstone`, `long/images/`); currently only the planning skeleton exists.

## v0.2.1 - 2026-06-03

This release reorganises the short-workshop narrative around a single AgentOps operating model, polishes the Agent Foundations section, and fixes several rendering bugs in the Marp -> PPTX pipeline.

### Highlights

- **New AgentOps operating model.** The deck now tells one story end to end - Evaluate, Ship, Observe, Operate - replacing the older six-step loop that confused learners.
- **Stronger Agent Foundations section.** New "complexity vs anatomy" slide and updated narrative make the "why agents need a new operating model" pitch land more cleanly.
- **Cleaner slide rendering.** Subtitles no longer show a stray `>`, the four-pillar diagram renders full-width instead of as a corner thumbnail, and diagrams no longer overlap their subtitles.

### Content - Agent Foundations (Richard Healy)

- Add a new "complexity vs anatomy" slide and accompanying `anatomy-complexity.png` diagram to the Agent Foundations section, and re-order the surrounding slides so the foundations story flows from "what an agent is" into "why production is hard". Narratives updated to match.
- Refresh `production-gap.png` to align with the new ordering.
- Polish speaker notes throughout the deck so each slide intros its topic cleanly and sets up the next one.

### Content - Four-pillar operating model (Paulo Lacerda)

- Replace the six-step operating loop (`Evaluate, Gate, Observe, Diagnose, Ship, Improve`) with a single four-pillar model (`Evaluate -> Ship -> Observe -> Operate`) as the primary AgentOps story across the short track. Old loop items map as Gate+Ship -> Ship and Diagnose+Improve -> Operate.
- Update `short/slides.md`: retitle the operating-model slide and its visual, rename the Evaluation/CI-CD/Observability/Day-2 section dividers to Evaluate/Ship/Observe/Operate, rewrite affected speaker notes, and reframe the 30-day adoption path around the four pillars.
- Update `short/speaker-script.md`, `short/agenda.md`, `short/run-of-show.md`, and `short/index.md` so the narration and delivery materials present the four-pillar model consistently.

### Diagrams

- Add the `agentops-four-pillars` diagram to `prep/tools/make_diagrams.py` and render `short/images/agentops-four-pillars.png`; the operating-model slide no longer uses `operating-loop.png`. (Paulo Lacerda)
- Add a `model-lifecycle` diagram to `prep/tools/make_diagrams.py` and regenerate every diagram in `short/images/` without an embedded header, so the slide title in the deck no longer competes with the diagram title. (Richard Healy)

### Tooling - Marp -> PPTX converter (Paulo Lacerda)

- Strip the leading `>` from Markdown blockquote subtitles in `_extract_body_text`, so subtitles read as prose instead of showing a literal `>` character.
- Register `agentops-four-pillars.png` in `DIAGRAM_IMAGES` so the operating-model visual renders centered and full-width instead of as a tiny stock-photo thumbnail in the top-right corner.
- Push diagram images down to `Inches(2.3)` whenever a slide has both a blockquote subtitle and an inline diagram (both the inline-diagram and `IMAGE_MAP`-diagram paths respect `has_body`), so the diagram no longer overlaps the subtitle textbox.

### Artefacts

- Regenerate `short/slides.pptx` from the updated `slides.md`.

### Follow-up

- `short/agentops-short-video.mp4` is now out of sync with the revised script and should be re-rendered via `build_production_video.py` + `compress_production_video.py`.
- Mirror the deck to the upstream program repo at `presentations/04-agentops/`.

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
