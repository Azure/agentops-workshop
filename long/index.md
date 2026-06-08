---
title: Long Workshop - VBD
layout: default
nav_order: 3
has_children: true
---

# Long Workshop - Value Based Delivery (VBD) version

{: .important }
> **Under construction.** The long (~8 hours) workshop is the Value Based Delivery (VBD) version and is still being designed. The pages below are planning material, not deliverable content. If you need a session you can run today, see the [short workshop]({{ '/short/' | relative_url }}).

This track is the full-day AgentOps workshop for the Value Based Delivery (VBD) version. The lab content is not implemented yet. This section defines the planned structure, learning outcomes, sequencing, and directory layout.

## Full-day outcome (planned)

By the end of the long workshop, attendees should have a practical blueprint for operating one AI agent in production:

- Define an agent target and release-readiness contract.
- Create an evaluation dataset and quality thresholds.
- Add CI/CD release gates and readiness evidence.
- Instrument observability for traces, telemetry, alerts, safety events, latency, and cost.
- Connect production traces back to evaluation and continuous improvement.
- Understand governance, red-team follow-through, and incident response patterns.

## Planning pages

| Page | Purpose |
|---|---|
| [Agenda]({{ '/long/agenda' | relative_url }}) | Full-day time plan. |
| [Lab roadmap]({{ '/long/lab-roadmap' | relative_url }}) | Lab sequence and learning objectives. |
| [Observability strategy]({{ '/long/observability-strategy' | relative_url }}) | Cross-cutting observability plan for the full-day workshop. |
| [Lab planning pages]({{ '/long/labs/' | relative_url }}) | Placeholder lab plans for future implementation. |

## Observability treatment

Observability is both a dedicated lab and a thread across the workshop. Every lab should preserve enough metadata to support release evidence and runtime diagnosis:

- Agent version
- Dataset and eval run
- Release or deployment ID
- Trace ID
- Safety findings
- Owner and incident path
- Runtime telemetry links
