---
title: Source Materials
layout: default
nav_order: 5
has_children: true
---

# Source Materials

## Primary reference deck

Private GenAIOps Training deck notes were used as the main conceptual source. Treat the source as a training deck that needs to be compressed for a 1-hour AgentOps session.

Important content to preserve:

- POC-to-production gap
- GenAIOps operating model
- People, process, platform
- Non-linear lifecycle
- Maturity model
- Evaluation strategy
- CI/CD integration
- Responsible AI and red teaming
- AI gateway / APIM pattern
- Observability and tracing
- Governance and cost

## Demo reference

Private AgentOps end-to-end tutorial notes should be used as the source of truth for the demo video. The tutorial covers:

- Foundry control plane
- Travel Agent target
- Repo-side release contract
- Evaluation path
- Regression and fix loop
- CI/CD gates
- Observability
- Doctor/readiness evidence
- Cockpit/local command center
- Trace learning

## Prior planning materials

Earlier planning content was consolidated into:

- `..\..\1-hour\agenda.md`
- `..\1-hour\slide-plan.md`
- `..\1-hour\demo-video-plan.md`
- `..\1-hour\observability-plan.md`

## Website reference

The repository structure is inspired by:

- GitHub repository: `https://github.com/microsoft/llmops-workshop`
- GitHub Pages site: `https://microsoft.github.io/llmops-workshop`

This repo follows the same general idea: markdown-first content, Jekyll/Just the Docs navigation, and lab-oriented structure. The content itself is AgentOps-specific.

## Positioning rule

AgentOps Toolkit is a practical implementation component. It can help demonstrate CLI-based evaluation, Doctor/readiness checks, Cockpit/local command center, and evidence generation. It is not the topic of the session.

## Observability rule

Observability is a first-class AgentOps topic. When adapting source content, preserve and expand material related to:

- Traces
- Telemetry correlation
- Azure Monitor and Application Insights
- Foundry tracing and evaluation context
- Runtime quality and safety signals
- Cost and latency
- Alerting and incident response
- Production trace promotion into future evaluation sets

## Reference pages

Use these companion pages to continue work without needing private chat history:

- [Context Brief](context-brief.md)
- [AgentOps Operating Model](agentops-operating-model.md)
- [Content Decisions](content-decisions.md)
- [Workshop Backlog](workshop-backlog.md)
