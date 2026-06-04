# AgentOps Workshop - Copilot Instructions

## Repository purpose

This repository is a GitHub Pages content workspace for the **AgentOps Workshop**, with two delivery tracks:

- **short**: short session plan, slide plan, run of show, and demo video plan.
- **long**: full-day workshop plan with multiple labs. Lab content is intentionally planning-only for now.

Treat this as a workshop and documentation repository, not as an application codebase. Do not add application scaffolding, sample implementations, SDK code, or lab solution code unless explicitly requested.

## Repository layout

The repo is split into **workshop content** (what an attendee or instructor consumes) and **preparation materials** (authoring notes, build tools, and intermediate artefacts that the consumer does not need to see).

Workshop content (consumer-facing, published to GitHub Pages):

- `index.md`, `README.md`, `_config.yml`, Gemfile (site root)
- `short\` - the short (~1-hour) session deliverables: `agenda.md`, `slides.md`, `slides.pptx`, `agentops-short-video.mp4`, `speaker-script.md`, `run-of-show.md`, `images\`
- `long\` - the long (~8-hour) full-day workshop planning skeleton
- `instructor\delivery-guide.md` - cross-track instructor notes
- `assets\` - shared images, slides, video, data

Preparation materials (excluded from the published site via `_config.yml`):

- `prep\references\` - sanitized context pack, content decisions, operating model notes, source materials, working backlog
- `prep\tools\` - Python scripts that generate diagrams, render slides, synthesize speech, and assemble the narrated video
- `prep\short\` - planning docs (`slide-plan.md`, `observability-plan.md`, `demo-video-plan.md`), original single-voice script backup, and intermediate audio/video artefacts (gitignored)

When new authoring artefacts are created (notes, planning docs, build scripts, intermediates), place them under `prep\`. Only files an attendee or instructor would consume belong at the root.

## Parent program

This workshop is one component of a broader engagement program called the **AI Path to Production - Delivery Accelerator**.

- Upstream program repository (private): https://github.com/tbhamidipati/prod-readiness-workshop
- The program has six webinar topics. AgentOps is **Topic 4**.
- Upstream location for the AgentOps presentation assets: https://github.com/tbhamidipati/prod-readiness-workshop/tree/master/presentations/04-agentops

Working agreement with the upstream program:

- `agentops-workshop` (this repo) is the authoring workspace. Planning artifacts, references, run-of-show, observability plan, demo video plan, and per-track materials are produced here.
- Final presentation deliverables (Marp `slides.md` and exported `.pptx`) authored here must be mirrored into the upstream `presentations/04-agentops/` folder.
- When proposing structural changes to the deck, cross-check the upstream `presentations/04-agentops/slides.md` so the short and long materials stay consistent with the program's section taxonomy: **AgentOps Foundations, Agent Development Lifecycle, Evaluation, CI/CD for Agentic AI, Observability, Day-2 Operations**.
- Do not link to the upstream private repo from public site pages. Reference it only inside repository instructions, internal notes, and `prep\references\` materials.

## Core positioning

The theme is **AgentOps**, not AgentOps Toolkit.

Use this framing:

> AgentOps is the operating model for moving AI agents from prototype to production with evaluation, release gates, observability, diagnostics, safety, governance, and continuous improvement.

AgentOps Toolkit may be mentioned, but only as one practical component or reference accelerator that can help implement parts of the AgentOps operating model. Do not make the workshop a product walkthrough or a toolkit launch deck.

## Audience

Default audience: customer-facing technical and platform stakeholders:

- AI application builders
- Architects
- DevOps and platform teams
- AI governance stakeholders
- Technical decision makers responsible for production AI systems

Assume a mixed audience. Keep the main story understandable for leaders, but include enough technical depth for architects and engineers.

## Messaging rules

Do:

- Lead with production confidence, release evidence, and operational readiness.
- Explain how AgentOps applies DevOps discipline to agentic AI.
- Keep Microsoft Foundry as the control plane for agents, evaluation, observability, safety, and governance.
- Position Azure Monitor and Application Insights as the runtime observability layer.
- Position AgentOps practices as the repeatable operating loop around Foundry, repo, CI/CD, readiness checks, and release evidence.
- Use the operating loop: **Evaluate, Gate, Observe, Diagnose, Ship, Improve**.
- Include evaluation, CI/CD gates, observability, red-team follow-through, incident response, cost, and governance.
- Explore observability deeply. Treat traces, telemetry correlation, dashboards, alerting, release evidence, and trace-to-evaluation feedback loops as first-class AgentOps practices.

Avoid:

- Making AgentOps Toolkit the central narrative.
- Calling the session an AgentOps Toolkit walkthrough.
- Starting with installation or command syntax.
- Spending too much time on tool internals.
- Describing AgentOps as a replacement for Foundry.
- Calling Cockpit a dashboard if the intended wording is local command center.

## Preferred language

Use English for all repository files, plans, website pages, speaker notes, lab plans, and GitHub Pages content.

## Source materials

Primary sources:

- `prep\references\source-materials.md`
- `prep\references\context-brief.md`
- `prep\references\agentops-operating-model.md`
- `prep\references\content-decisions.md`
- `prep\references\workshop-backlog.md`
- `prep\short\slide-plan.md`
- `short\agenda.md`
- `prep\short\demo-video-plan.md`
- `long\lab-roadmap.md`

External source references:

- Private GenAIOps Training deck notes summarized in `prep\references\source-materials.md`.
- Private AgentOps end-to-end tutorial notes summarized in `prep\references\source-materials.md`.
- Upstream AgentOps deck in the parent program: `presentations\04-agentops\slides.md` in the `tbhamidipati\prod-readiness-workshop` repository. Use it as the structural reference for section taxonomy, Marp format, and slide ordering.
- Prior planning content consolidated into the short and long track pages.

## Content conventions

- Keep markdown files directly useful for building the deck later.
- For slide outlines, include: purpose, on-slide content, speaker cue, visual idea, and source mapping.
- Keep the short deck concise, but reserve explicit time for observability.
- Move deep technical detail to appendix ideas rather than the main flow.
- Prefer concise bullets over long paragraphs.
- Use ASCII punctuation in markdown.
- For the long track, create plans and placeholders only until the user asks for lab implementation.
- GitHub Pages uses Jekyll with Just the Docs. Use front matter consistently.

## Presentation deliverables

Every deliverable session (currently the short track, later the long track) must be produced as **two paired artifacts**:

1. A **Marp Markdown** source file (`slides.md`) - the structural source of truth for the deck.
2. A **PowerPoint** file (`slides.pptx` or `AgentOps.pptx`) - the delivered artifact, generated from the Markdown using the upstream `marp_to_pptx.py` converter and the program's branded template.

### File locations

- Short track: `short\slides.md`, `short\slides.pptx`, `short\images\`
- Long track (when authored): `long\slides.md`, `long\slides.pptx`, `long\images\`
- Upstream mirror path: `presentations\04-agentops\slides.md` and `presentations\04-agentops\AgentOps.pptx`

### Marp Markdown format

The `slides.md` must follow the upstream program's Marp conventions so it converts cleanly with `marp_to_pptx.py`:

- YAML front matter declares `marp: true`, theme, pagination, header, and footer. Use the program header `"Production Readiness Workshop"` and a topic-specific footer such as `"Topic 4 - AgentOps"`.
- Slides are separated by `---` on its own line.
- Title and section-divider slides use the `<!-- _class: lead -->` directive immediately before the heading.
- The first slide carries the workshop title and subtitle.
- The second slide is the agenda, listing the six AgentOps sections.
- Each subsequent section opens with a lead-class divider slide for: **AgentOps Foundations**, **Agent Development Lifecycle**, **Evaluation**, **CI/CD for Agentic AI**, **Observability**, **Day-2 Operations**.
- Body slides use a single `#` heading, then bullets, tables, or images.
- Every content slide ends with a `<!-- Speaker notes: ... -->` HTML comment containing the speaker narrative and, where relevant, a source link to Microsoft Learn or another authoritative reference.
- Images live in `images\` next to `slides.md` and are referenced with relative paths.
- Use ASCII punctuation and avoid smart quotes.

### Section taxonomy

Within a deck, organize content under the six AgentOps sections defined by the parent program:

1. AgentOps Foundations
2. Agent Development Lifecycle
3. Evaluation
4. CI/CD for Agentic AI
5. Observability
6. Day-2 Operations

For the short deck, the operating loop **Evaluate, Gate, Observe, Diagnose, Ship, Improve** remains the storyline. Map condensed content to the six sections above so it stays consistent with the upstream program structure.

### Upstream mirroring rules

- Treat the `slides.md` produced here as the source. Copy it (and the matching `pptx` and `images\`) into `presentations\04-agentops\` in the upstream repo when a milestone is ready.
- Keep section names and slide ordering aligned with the upstream deck unless a divergence is explicitly recorded in `prep\references\content-decisions.md`.
- Do not move private or sanitized references from `prep\references\` into the slides themselves; the deck must stand on its own without linking to private materials.

## AgentOps Toolkit treatment

Approved subtle mentions:

- "AgentOps Toolkit can be used as a reference accelerator for the demo flow."
- "In the demo, AgentOps Toolkit components such as CLI, Doctor, and Cockpit can make the operating model tangible."
- "The toolkit is one implementation path for repo-side release contracts, eval evidence, and readiness checks."

Avoid these phrasings:

- "This session is about AgentOps Toolkit."
- "AgentOps equals AgentOps Toolkit."
- "AgentOps Toolkit replaces Foundry."
- "The customer problem is installing the toolkit."

## GitHub Pages conventions

- Site home: `index.md`
- Short track: `short\`
- Long track: `long\`
- Lab planning pages: `long\labs\`
- Static assets: `assets\`
- Authoring materials and source notes: `prep\` (excluded from the published site via `_config.yml`)
- Keep pages compatible with the `just-the-docs` Jekyll theme.

## Privacy and source handling

- Do not add personal names, private SharePoint URLs, local user paths, tenant identifiers, or raw customer data to public pages.
- Summarize private materials into sanitized reference notes instead of linking to the private source directly.
- If a source is private, describe it generically, for example: "private training deck notes" or "private end-to-end tutorial notes."

## Release management

Binary artefacts (today: the narrated short-workshop video) are committed directly to the repo and served as static assets by the private GitHub Pages site. This is the *only* way a `<video>` element on the published site can actually play the file - the repo is private, so the GitHub Release asset URL (`https://github.com/.../releases/download/...`) returns 404 to any cross-origin request from `pages.github.io`, which produces an empty embedded player.

Hard constraints to respect when regenerating these artefacts:

- Each file must stay **under GitHub's 100 MB per-file push limit**. The current narrated MP4 lands at ~85 MB by ending `build_video.py` with `ffmpeg -c:v copy -c:a aac -b:a 48k -ac 1 -movflags +faststart`. If a future artefact cannot be compressed below 100 MB without unacceptable quality loss, do not silently fall back to a GitHub Release URL in the embed - it will not play. Instead, mirror to a location reachable without auth (public Azure Blob, unlisted YouTube embed, etc.) and update the embed accordingly.
- Embed paths must be relative URLs (`{{ '/short/agentops-short-video.mp4' | relative_url }}`) so the asset is fetched same-origin from the Pages site.
- The Pages site is private (`x-pages-private: 1`); only signed-in Azure org members can reach it, so privacy is preserved without obscuring the URL.

Versioning when artefacts change:

- Bump the `CHANGELOG.md` entry under `## Unreleased` describing what changed.
- Tag a semver release (`v0.1.0`, `v0.1.1`, ...) when shipping a milestone. Tags are plain semver with no track suffix; one tag covers the whole kit at a point in time.
- GitHub Releases are optional now (the file lives in git). If you do publish a release, attach the same MP4 as an archival download for `gh release download` users and keep its tag pinned forever (do not delete older releases - instructors may have copied pinned links).

### CHANGELOG and release-notes formatting

The user prefers a CHANGELOG that reads like product release notes, not a flat list of "stuff I changed". Every released version (and the `## Unreleased` section, when it has more than one or two bullets) must follow this structure:

1. **One-line release intro** under the version header summarising what the release is about ("This release reorganises ... and fixes several rendering bugs in the Marp -> PPTX pipeline.").
2. **`### Highlights`** - three to five short, learner-friendly bullets that someone skimming the release page can understand without context. Lead with the user-visible win, not the file path.
3. **One or more `### Content - <area> (<Author Name>)` sections** - grouped by area of the deliverable (e.g. Agent Foundations, Four-pillar operating model, Long workshop labs). Author attribution in parentheses is REQUIRED on each grouped section so contributions stay clearly attributable when multiple people land work in the same release. If a section is genuinely co-authored, list both names.
4. **`### Diagrams`** when any image under `short/images/`, `long/images/`, or `assets/` was added or regenerated. Attribute per diagram in trailing parentheses (e.g. "(Richard Healy)").
5. **`### Tooling - <component> (<Author Name>)`** for any change under `prep/tools/`, `.github/`, `_config.yml`, build scripts, etc.
6. **`### Artefacts`** for regenerated binary outputs (`short/slides.pptx`, `short/agentops-short-video.mp4`, ...). Keep this short - just list what was rebuilt.
7. **`### Follow-up`** for known out-of-sync artefacts or upstream mirroring work that is intentionally deferred.

Rules that apply to every CHANGELOG entry:

- Always attribute contributions by author when more than one person has committed since the previous tag. Use `git log <previous-tag>..HEAD --pretty=format:"%h | %an | %s"` to recover authorship before writing the section.
- Never collapse multiple authors' work into an undifferentiated bullet list. Group their contributions into their own subsections so a reader can tell who did what.
- Use plain English in highlights and section headings. Save the file-path-heavy detail for the bullets inside each section.
- Wrap inline code (file paths, identifiers, CLI flags) in backticks consistently.
- Prefer ASCII punctuation. No em dashes as sentence separators - use " - " (space hyphen space) instead.
- Keep the same structure for the matching GitHub Release notes when publishing via `gh release create`, plus a closing `**Contributors**: ...` line that names every committer in the release.

Workflow when shipping a release:

1. Read the existing `## Unreleased` block and the `git log` since the previous tag.
2. Replace the `## Unreleased` header with `## vX.Y.Z - YYYY-MM-DD` and reorganise the bullets into the Highlights / Content / Diagrams / Tooling / Artefacts / Follow-up structure above, attributing every grouped section to its author(s).
3. Commit the reorganised CHANGELOG (`git commit -m "Promote Unreleased entries into vX.Y.Z with per-author attribution"`).
4. Tag it: `git tag -a vX.Y.Z -m "vX.Y.Z - <one-line summary>"`.
5. Push commits and tag: `git push origin main && git push origin vX.Y.Z`.
6. Publish the GitHub Release with `gh release create vX.Y.Z --title "vX.Y.Z - <one-line summary>" --notes-file <tempfile>` using release notes that mirror the CHANGELOG structure plus a `**Contributors**` line.
7. After publishing, add a fresh empty `## Unreleased` block at the top of `CHANGELOG.md` for the next cycle (only if the user is continuing work in the same session - otherwise leave it for the next change).

## Video production conventions

These conventions apply to every narrated workshop video built in this repo (currently the short-session preview at `prep\short\preview\avatar-preview.mp4` and the production short video at `short\agentops-short-video.mp4`). They are locked because we iterated on them with the user and the resulting look is approved. Do not re-litigate them when adding new slides or new tracks.

Avatar staging (single active speaker with crossfaded handoffs):

- The video shows **only ONE avatar at a time** -- the speaker who is currently talking. Do NOT keep both on screen as co-presenters; the previous "always-both-visible" layout was rejected because the silent listener's idle motion competed with the speaker for the viewer's attention.
- **Lisa (SP1, en-US-AvaMultilingualNeural, character `lisa` / style `casual-sitting`)** appears in the **bottom-LEFT** corner whenever she speaks.
- **Harry (SP2, en-US-AndrewMultilingualNeural, character `harry` / style `business`)** appears in the **bottom-RIGHT** corner whenever he speaks.
- Their fixed left/right corners preserve a "voice = position" identity throughout the deck; do not move them or merge into a single centre slot.
- Avatar overlays must be **flush with the screen bottom** (`y = canvas_height - overlay_height`). Do not add a bottom margin - it makes them look like they are floating. Use a horizontal margin only (~36 px from the side edge).
- The avatar source crop must be **wide enough to contain natural arm gestures** without clipping. The known-good crop for the Azure pre-built avatars is `900x1080` taken at `x=510, y=0` from a 1920x1080 source, then scaled down to `380x456` for the overlay. Smaller crops clip Harry's hands when he opens his arms.
- **Speaker handoffs use an alpha crossfade**, not an abrupt cut. The outgoing speaker fades OUT over ~0.4 s at the end of their last turn; the incoming speaker fades IN over ~0.4 s at the start of their first turn. Consecutive turns by the SAME speaker have no fades, so the avatar stays continuously visible across multiple turns in a row. Because the two avatars sit in opposite corners, the fade-out and fade-in never overlap on the same pixels -- you simply see Lisa dim on the left, then Harry rise on the right.
- The idle-webm approach used in v3 (looped 20 s native-motion clip captured via SSML `<mstts:silence Leading-exact 10000ms/>Mm.<mstts:silence Tailing-exact 10000ms/>`) is preserved in `prepare_idle_clip` for potential reuse, but the v4 layout no longer overlays an idle source. The cached `idle-lisa.webm` / `idle-harry.webm` files are kept around but not consumed by the current pipeline.

Slide motion:

- **No Ken Burns, no zoompan, no slow pans inside a slide.** A slide just sits still while the avatars talk. The earlier zoom effect was rejected as distracting; do not reintroduce it.
- **Slide-to-slide transitions use `xfade` (crossfade, ~0.5 s) plus `acrossfade` on audio**. No wipes, no slides, no cuts.

Preview vs production staging (when to switch modes):

- The **preview pipeline** (`prep\tools\build_preview.py`, output `prep\short\preview\avatar-preview.mp4`) renders **every slide in jogral mode** -- one avatar per SP1/SP2 turn with a crossfade at every speaker change. This is what the user evaluates new staging or motion ideas against; keep it pure jogral so the visuals are predictable.
- The **production pipeline** (`prep\tools\build_production_video.py`, output `short\agentops-short-video.mp4`) uses **mixed staging** because doing pure jogral for ~45 minutes was rejected as too "tossy" / cognitively expensive:
  - **Intro slides (1-3): jogral** -- the short title + agenda + operating-loop slides keep the tight back-and-forth dialogue between Lisa and Harry so the workshop opens with energy.
  - **Core slides (4+): one merged avatar per slide.** All SP1/SP2 turns inside a single slide are concatenated into ONE super-turn rendered by ONE speaker via SSML with 350 ms `<break>` pauses replacing each former speaker boundary. The assigned speaker **alternates per slide** so attention still bounces between Lisa and Harry, but only at slide transitions -- never inside a slide.
  - The core-slide speaker assignment starts with **SP2 (Harry) on slide 4** so the intro->core handoff is a same-speaker continuation (slide 3 already ends on SP2). The alternation lands the final slide on **SP1 (Lisa)**, which keeps the "Thank you for watching" line on the original scripted speaker.
- **Cross-slide fade rule** (production): at slide boundaries the 0.5 s slide xfade dissolves the entire frame, so do NOT also alpha-fade the avatar at that boundary. Doing both produces a ghosty double-fade because the avatar's opacity is multiplied by the slide dissolve. The avatar alpha fade is reserved for WITHIN-slide speaker changes (intro-jogral) plus the very-first and very-last turns of the whole video. `compute_fades()` in `build_production_video.py` encodes this rule.

Avatar rendering pipeline notes:

- Output format from Azure: `videoFormat=webm`, `videoCodec=vp9`, **`backgroundColor=#00B140FF`** (chromakey green). The Azure API does **not** honour transparent backgrounds for the prebuilt avatars; requesting `#00000000` produces a video with a solid background anyway. We therefore use the well-known chromakey green and key it out in ffmpeg (`chromakey=0x00B140:0.10:0.05`).
- One Azure job per speaking unit (per-turn in jogral mode, per-slide merged-SSML super-turn in production core mode), cached on disk by content hash so re-runs reuse the cached webm. The cache key includes the background color so changing chromakey approach automatically invalidates cached files. Plain-text and SSML inputs hash differently because the literal text changes, so the same slide can have both intro-jogral cache entries and a separate merged-SSML cache entry without collision.
- **Merged super-turns must be SSML, not concatenated plain text.** Plain text with `\n\n` does not pace as a break; you need `<prosody rate='-2%'>...</prosody><break time='350ms'/><prosody...>...` all inside one `<voice>` inside one `<speak>`. Putting `<break>` as a direct child of `<speak>` returns HTTP 400 from Azure TTS. `build_merged_ssml()` in `build_production_video.py` follows the correct pattern -- copy it, don't reinvent.
- When changing the layout or filter graph, bump the `SEG_VERSION` string (`v4` for the preview pipeline, `v4p` for the production pipeline) so existing per-turn composite files are not silently reused with the old layout. The two version strings must stay distinct so preview and production renders never clobber each other in the shared `prep\short\preview\segments\` directory.

Reference implementations: `prep\tools\build_preview.py` (jogral throughout) and `prep\tools\build_production_video.py` (intro-jogral + core-merged). When adding a new track (e.g. the long workshop) or regenerating the production video after a script edit, mirror the same staging, motion, chromakey, and SSML-pacing settings unless this section is updated first.

Compression for the published asset:

- The production raw output lands well over GitHub's 100 MB per-file push limit (typically 250-400 MB at the build script's CRF 20 / 192 kbps stereo settings). Always run `prep\tools\compress_production_video.py` afterwards to ladder through quality presets until the file fits comfortably under 90 MB (preserving margin under the 100 MB limit).
- The compress script tries 1080p CRF 28 first and only drops resolution to 720p as a last resort. If even 720p CRF 30 cannot reach the target, that is the signal to revisit the embed strategy (host externally) per the Release management section above -- do NOT silently push a >100 MB file.
