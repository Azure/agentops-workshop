---
title: Content Decisions
layout: default
parent: Source Materials
nav_order: 3
---

# Content Decisions

This page records editorial and structural decisions already made for the workshop.

## Positioning decisions

| Decision | Rationale |
|---|---|
| The main theme is AgentOps, not AgentOps Toolkit. | The workshop should teach an operating model, not a product walkthrough. |
| AgentOps Toolkit is an optional accelerator. | It can make evals, readiness evidence, Doctor, and local command center flows tangible, but it should not dominate the narrative. |
| Foundry remains the control plane. | AgentOps practices should connect Foundry signals to release decisions and operations, not replace Foundry. |
| Observability gets explicit depth. | Agents require trace-level understanding, telemetry correlation, and trace-to-eval feedback loops. |
| The short track is called "1-hour session." | This avoids confusion with the 8-hour workshop while keeping the short delivery option clear. |
| The 8-hour track is planning-only for now. | Lab content should be implemented after scenario and prerequisites are approved. |

## Content hierarchy

Use this priority order when editing:

1. Production confidence and release readiness.
2. AgentOps operating model.
3. Microsoft Foundry control plane.
4. Evaluation and release gates.
5. Observability and diagnostics.
6. Safety, governance, and cost.
7. AgentOps Toolkit as an optional implementation component.

## Style decisions

- Use English for all repo content.
- Prefer practical, customer-facing language.
- Avoid generic "AI transformation" language.
- Avoid installation-first content.
- Avoid long tool walkthroughs in the 1-hour session.
- Use markdown that can become deck content later.

## Privacy decisions

- Do not include personal names.
- Do not include private URLs.
- Do not include local machine paths.
- Do not include raw SharePoint shortcuts.
- Do not include tenant-specific screenshots or telemetry.
- Summarize private materials into sanitized notes.

## Observability decision

Observability should be presented as a closed loop:

**Trace -> diagnose -> add eval row -> gate future release -> observe again**

The workshop should avoid treating observability as a generic dashboard topic. The key lesson is that production behavior becomes future evaluation coverage.
