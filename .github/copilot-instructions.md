# AgentOps Workshop - Copilot Instructions

## Repository purpose

This repository is a GitHub Pages content workspace for the **AgentOps Workshop**, with two delivery tracks:

- **1-hour**: short session plan, slide plan, run of show, and demo video plan.
- **8-hour**: full-day workshop plan with multiple labs. Lab content is intentionally planning-only for now.

Treat this as a workshop and documentation repository, not as an application codebase. Do not add application scaffolding, sample implementations, SDK code, or lab solution code unless explicitly requested.

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

- `references\source-materials.md`
- `references\context-brief.md`
- `references\agentops-operating-model.md`
- `references\content-decisions.md`
- `references\workshop-backlog.md`
- `1-hour\slide-plan.md`
- `1-hour\agenda.md`
- `1-hour\demo-video-plan.md`
- `8-hour\lab-roadmap.md`

External source references:

- Private GenAIOps Training deck notes summarized in `references\source-materials.md`.
- Private AgentOps end-to-end tutorial notes summarized in `references\source-materials.md`.
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
- Source notes: `references\`
- Keep pages compatible with the `just-the-docs` Jekyll theme.

## Privacy and source handling

- Do not add personal names, private SharePoint URLs, local user paths, tenant identifiers, or raw customer data to public pages.
- Summarize private materials into sanitized reference notes instead of linking to the private source directly.
- If a source is private, describe it generically, for example: "private training deck notes" or "private end-to-end tutorial notes."
