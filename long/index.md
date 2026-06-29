---
title: AgentOps VBD Workshop
layout: default
nav_order: 3
has_children: true
---

# AgentOps Value Delivery Workshop

This is the full-day (~8 hour) AgentOps Value Delivery (VBD) Workshop. Where the
[AgentOps Briefing]({{ '/short/' | relative_url }}) answers *"what is AgentOps and why
does it matter"*, this track answers *"how do I actually take one of my agents to
production"*. Attendees leave with a 30-day plan plus a release-readiness package
filled in for one of their own production-candidate agents.

The workshop teaches the four-pillar AgentOps operating model - **Evaluate -> Ship ->
Observe -> Operate** - through a presentation deck and six hands-on labs plus a
capstone. Microsoft Foundry stays the control plane; Azure Monitor and Application
Insights are the runtime observability layer. Labs use the open-source
[AgentOps Accelerator](https://github.com/Azure/agentops) as the concrete
implementation path for evaluation, CI/CD gates, and observability signals.

## Full-day outcome

By the end of the workshop, each attendee has, for one real agent:

- An agent target inventory and a release-readiness contract.
- An evaluation dataset plan with metrics, thresholds, and a baseline comparison.
- CI/CD release gates and a readiness evidence package.
- Observability wired for traces, telemetry correlation, dashboards, and alerts.
- A safety and red-team follow-through plan plus a governance and ownership map.
- An incident-response and continuous-improvement loop that turns production traces
  into future evaluation coverage.
- A capstone production-readiness review that composes every artefact into a
  go/no-go decision.

## How the day is organized

| Page | Purpose |
|---|---|
| [Datasheet]({{ '/long/datasheet' | relative_url }}) | One-page customer-facing summary: outcomes, duration, level, prerequisites. |
| [Prerequisites]({{ '/long/prerequisites' | relative_url }}) | What the customer needs in place before Day 1. |
| [Agenda]({{ '/long/agenda' | relative_url }}) | Full-day time plan that matches the real lab timings. |
| [Lab roadmap]({{ '/long/lab-roadmap' | relative_url }}) | Lab sequence, learning objectives, and the artefact each lab produces. |
| [Observability strategy]({{ '/long/observability-strategy' | relative_url }}) | Cross-cutting observability thread that runs through every lab. |
| [Labs]({{ '/long/labs/' | relative_url }}) | The six hands-on labs, the capstone, and the artefact templates. |
| [Instructor guide]({{ '/long/instructor-guide' | relative_url }}) | Facilitator setup, timing, and lab-by-lab pitfalls. |

## The observability thread

Observability is both a dedicated lab (Lab 4) and a thread across the whole workshop.
Every lab preserves the metadata needed for release evidence and runtime diagnosis:

- Agent version and deployment ID
- Evaluation dataset and run ID
- Release or gate decision ID
- Trace ID convention
- Safety and red-team findings
- Owner and escalation path
- Runtime telemetry links

Lab 1 defines these identifiers, Lab 4 expands them into a correlation model, and the
capstone consumes them. See the [observability strategy]({{ '/long/observability-strategy' | relative_url }})
for the full thread.
