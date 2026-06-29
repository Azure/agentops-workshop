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
| The short track is called "short workshop." | This avoids confusion with the long workshop while keeping the short delivery option clear. |
| The long track is planning-only for now. | Lab content should be implemented after scenario and prerequisites are approved. (Superseded: the long track is now implemented - see below.) |

## Four-pillar operating model (locked)

The canonical AgentOps operating model is the **four-pillar** model:

**Evaluate -> Ship -> Observe -> Operate**

This is the model the shipped short track (release `v0.3.0`) teaches, and it is the
model the full-day VBD track must use end to end.

| Decision | Rationale |
|---|---|
| Use the four pillars Evaluate, Ship, Observe, Operate. | Single, memorable operating loop that maps cleanly to the six program sections (Foundations, ADLC, Evaluation, CI/CD, Observability, Day-2). |
| Do not reintroduce the older six-step loop (Evaluate / Gate / Observe / Diagnose / Ship / Improve). | "Gate" folds into Ship; "Diagnose" and "Improve" fold into Operate. Keeping two competing loops confuses attendees. |
| Do not use "Own" as a pillar name. | The AgentOps Accelerator product tagline uses "Own", but the workshop pillar is named **Operate** to keep the operating model verb-consistent and avoid product/operating-model conflation. |
| Foundry stays the control plane; Azure Monitor + Application Insights are the runtime observability layer. | Consistent with the short track. |
| The AgentOps Accelerator (`Azure/agentops`) is the reference implementation for the labs. | It is the concrete "how" behind the four-pillar "what" for evaluation, CI/CD gates, and observability signals. It must not become the narrative. |

Note: `.github/copilot-instructions.md` still references the older six-step loop in a
couple of places (the "Evaluate, Gate, Observe, Diagnose, Ship, Improve" wording). Where
that conflicts with the four-pillar model, the four-pillar model wins because it matches
the shipped short track and the long-track issue. This decision record is the source of
truth for the loop naming until the instructions file is refreshed.

## Long track is implemented

The full-day VBD track is no longer planning-only. It now ships a Marp deck
(`long/slides.md` + `long/slides.pptx`), six hands-on labs plus a capstone under
`long/labs/`, artefact templates under `long/labs/templates/`, diagrams under
`long/images/`, an instructor guide, a datasheet, and a prerequisites checklist. The
labs use the AgentOps Accelerator as the reference implementation.

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
- Avoid long tool walkthroughs in the short workshop.
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
