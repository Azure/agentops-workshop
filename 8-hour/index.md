---
title: 8-Hour Workshop
layout: default
nav_order: 3
has_children: true
---

# 8-Hour Workshop

This track is the full-day AgentOps workshop plan. It is inspired by workshop formats such as LLMOps Workshop, but it is centered on AgentOps for production-ready AI agents.

The lab content is not implemented yet. This section defines the planned structure, learning outcomes, sequencing, and directory layout.

## Full-day outcome

By the end of the 8-hour workshop, attendees should have a practical blueprint for operating one AI agent in production:

- Define an agent target and release-readiness contract.
- Create an evaluation dataset and quality thresholds.
- Add CI/CD release gates and readiness evidence.
- Instrument observability for traces, telemetry, alerts, safety events, latency, and cost.
- Connect production traces back to evaluation and continuous improvement.
- Understand governance, red-team follow-through, and incident response patterns.

## Workshop pages

| Page | Purpose |
|---|---|
| [Agenda](agenda.md) | Full-day time plan. |
| [Lab roadmap](lab-roadmap.md) | Lab sequence and learning objectives. |
| [Observability strategy](observability-strategy.md) | Cross-cutting observability plan for the full-day workshop. |
| [Lab planning pages](labs/) | Placeholder lab plans for future implementation. |

## Observability treatment

Observability is both a dedicated lab and a thread across the workshop. Every lab should preserve enough metadata to support release evidence and runtime diagnosis:

- Agent version
- Dataset and eval run
- Release or deployment ID
- Trace ID
- Safety findings
- Owner and incident path
- Runtime telemetry links
