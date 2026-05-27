# AgentOps Workshop - Copilot Instructions

## Repository purpose

This repository is a GitHub Pages content workspace for the **AgentOps Workshop**, with two delivery tracks:

- **1-hour**: short session plan, slide plan, run of show, and demo video plan.
- **8-hour**: full-day workshop plan with multiple labs. Lab content is intentionally planning-only for now.

Treat this as a workshop and documentation repository, not as an application codebase. Do not add application scaffolding, sample implementations, SDK code, or lab solution code unless explicitly requested.

## Repository layout

The repo is split into **workshop content** (what an attendee or instructor consumes) and **preparation materials** (authoring notes, build tools, and intermediate artefacts that the consumer does not need to see).

Workshop content (consumer-facing, published to GitHub Pages):

- `index.md`, `README.md`, `_config.yml`, Gemfile (site root)
- `1-hour\` - the 1-hour session deliverables: `agenda.md`, `slides.md`, `slides.pptx`, `agentops-1hour-video.mp4`, `speaker-script.md`, `run-of-show.md`, `images\`
- `8-hour\` - the full-day workshop planning skeleton
- `instructor\delivery-guide.md` - cross-track instructor notes
- `assets\` - shared images, slides, video, data

Preparation materials (excluded from the published site via `_config.yml`):

- `prep\references\` - sanitized context pack, content decisions, operating model notes, source materials, working backlog
- `prep\tools\` - Python scripts that generate diagrams, render slides, synthesize speech, and assemble the narrated video
- `prep\1-hour\` - planning docs (`slide-plan.md`, `observability-plan.md`, `demo-video-plan.md`), original single-voice script backup, and intermediate audio/video artefacts (gitignored)

When new authoring artefacts are created (notes, planning docs, build scripts, intermediates), place them under `prep\`. Only files an attendee or instructor would consume belong at the root.

## Parent program

This workshop is one component of a broader engagement program called the **AI Path to Production - Delivery Accelerator**.

- Upstream program repository (private): https://github.com/tbhamidipati/prod-readiness-workshop
- The program has six webinar topics. AgentOps is **Topic 4**.
- Upstream location for the AgentOps presentation assets: https://github.com/tbhamidipati/prod-readiness-workshop/tree/master/presentations/04-agentops

Working agreement with the upstream program:

- `agentops-workshop` (this repo) is the authoring workspace. Planning artifacts, references, run-of-show, observability plan, demo video plan, and per-track materials are produced here.
- Final presentation deliverables (Marp `slides.md` and exported `.pptx`) authored here must be mirrored into the upstream `presentations/04-agentops/` folder.
- When proposing structural changes to the deck, cross-check the upstream `presentations/04-agentops/slides.md` so the 1-hour and 8-hour materials stay consistent with the program's section taxonomy: **AgentOps Foundations, Agent Development Lifecycle, Evaluation, CI/CD for Agentic AI, Observability, Day-2 Operations**.
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
- `prep\1-hour\slide-plan.md`
- `1-hour\agenda.md`
- `prep\1-hour\demo-video-plan.md`
- `8-hour\lab-roadmap.md`

External source references:

- Private GenAIOps Training deck notes summarized in `prep\references\source-materials.md`.
- Private AgentOps end-to-end tutorial notes summarized in `prep\references\source-materials.md`.
- Upstream AgentOps deck in the parent program: `presentations\04-agentops\slides.md` in the `tbhamidipati\prod-readiness-workshop` repository. Use it as the structural reference for section taxonomy, Marp format, and slide ordering.
- Prior planning content consolidated into the 1-hour and 8-hour track pages.

## Content conventions

- Keep markdown files directly useful for building the deck later.
- For slide outlines, include: purpose, on-slide content, speaker cue, visual idea, and source mapping.
- Keep the 1-hour deck concise, but reserve explicit time for observability.
- Move deep technical detail to appendix ideas rather than the main flow.
- Prefer concise bullets over long paragraphs.
- Use ASCII punctuation in markdown.
- For the 8-hour track, create plans and placeholders only until the user asks for lab implementation.
- GitHub Pages uses Jekyll with Just the Docs. Use front matter consistently.

## Presentation deliverables

Every deliverable session (currently the 1-hour track, later the 8-hour track) must be produced as **two paired artifacts**:

1. A **Marp Markdown** source file (`slides.md`) - the structural source of truth for the deck.
2. A **PowerPoint** file (`slides.pptx` or `AgentOps.pptx`) - the delivered artifact, generated from the Markdown using the upstream `marp_to_pptx.py` converter and the program's branded template.

### File locations

- 1-hour track: `1-hour\slides.md`, `1-hour\slides.pptx`, `1-hour\images\`
- 8-hour track (when authored): `8-hour\slides.md`, `8-hour\slides.pptx`, `8-hour\images\`
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

For the 1-hour deck, the operating loop **Evaluate, Gate, Observe, Diagnose, Ship, Improve** remains the storyline. Map condensed content to the six sections above so it stays consistent with the upstream program structure.

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
- Short track: `1-hour\`
- Full workshop track: `8-hour\`
- Lab planning pages: `8-hour\labs\`
- Static assets: `assets\`
- Authoring materials and source notes: `prep\` (excluded from the published site via `_config.yml`)
- Keep pages compatible with the `just-the-docs` Jekyll theme.

## Privacy and source handling

- Do not add personal names, private SharePoint URLs, local user paths, tenant identifiers, or raw customer data to public pages.
- Summarize private materials into sanitized reference notes instead of linking to the private source directly.
- If a source is private, describe it generically, for example: "private training deck notes" or "private end-to-end tutorial notes."
