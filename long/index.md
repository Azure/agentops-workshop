---
title: AgentOps VBD Workshop
layout: default
nav_order: 3
has_children: true
---

# AgentOps Value Delivery Workshop

{: .note }
> **Facilitator-ready workshop.** This VBD track is a full-day design-lab workshop. It is ready to use as a guided customer working session, but it intentionally does not include runnable lab code or sample implementations.

This track expands the one-hour AgentOps Briefing into an eight-hour Value Delivery Workshop. The goal is to help a customer team define the production operating model for one real or representative AI agent, using the four AgentOps pillars:

**Evaluate -> Ship -> Observe -> Operate**

The workshop is delivered as a facilitated design lab. Attendees leave with a concrete AgentOps readiness package, not just a conceptual overview.

## Full-day outcome

By the end of the VBD workshop, attendees should have a practical blueprint for operating one AI agent in production:

- Define an agent target and release-readiness contract.
- Create an evaluation dataset and quality thresholds.
- Add CI/CD release gates and readiness evidence.
- Instrument observability for traces, telemetry, alerts, safety events, latency, and cost.
- Connect production traces back to evaluation and continuous improvement.
- Understand governance, red-team follow-through, and incident response patterns.

## Workshop structure

| Block | Purpose | Output |
|---|---|---|
| Foundations | Select the target agent, owners, environments, and readiness question. | Agent readiness profile. |
| Evaluate | Define datasets, metrics, thresholds, baseline comparison, and regression handling. | Evaluation contract. |
| Ship | Convert evaluation evidence into PR gates, deployment gates, approvals, and release notes. | Release evidence package. |
| Observe | Design trace, telemetry, dashboard, alert, and feedback-loop coverage. | Observability model. |
| Operate | Define safety follow-through, incident response, cost review, model lifecycle, and continuous improvement. | Operating runbook. |
| Capstone | Decide whether the agent is ready to move forward and what risks remain. | Production-readiness review. |

## Workshop pages

| Page | Purpose |
|---|---|
| [Agenda]({{ '/long/agenda' | relative_url }}) | Full-day schedule. |
| [Lab roadmap]({{ '/long/lab-roadmap' | relative_url }}) | Lab sequence and learning objectives. |
| [Observability strategy]({{ '/long/observability-strategy' | relative_url }}) | Cross-cutting observability model for the full-day workshop. |
| [Lab guide]({{ '/long/labs/' | relative_url }}) | Facilitator-ready design-lab exercises and artifacts. |

## Observability treatment

Observability is both a dedicated lab and a thread across the workshop. Every lab should preserve enough metadata to support release evidence and runtime diagnosis:

- Agent version
- Dataset and eval run
- Release or deployment ID
- Trace ID
- Safety findings
- Owner and incident path
- Runtime telemetry links

## What this is not

This VBD track is not an AgentOps Toolkit walkthrough and not an app-build tutorial. It is a production-readiness working session around Microsoft Foundry, repo-side release evidence, CI/CD gates, Azure Monitor and Application Insights telemetry, safety review, and Day-2 operations.
