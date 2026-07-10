---
title: AgentOps VBD Workshop
layout: default
nav_order: 3
has_children: true
---

# AgentOps Value Delivery Workshop

{: .note }
> **Facilitator-ready, hands-on.** This VBD track is a full-day, hands-on workshop. Across seven connected labs, attendees build and operate one real agent on Microsoft Foundry, and every lab consumes the artifact the previous lab produced.

This track expands the one-hour AgentOps Briefing into an eight-hour Value Delivery Workshop. Attendees take one agent - the Contoso Travel Agent - all the way around the four AgentOps pillars on Microsoft Foundry:

**Evaluate -> Ship -> Observe -> Operate**

The workshop is delivered as a sequence of hands-on labs. Attendees leave with a working end-to-end AgentOps pipeline and an evidence pack, not just a conceptual overview.

## Full-day outcome

By the end of the VBD workshop, attendees have built and operated one AI agent in production:

- Deploy the agent to Microsoft Foundry and set up the workspace and CLI.
- Author an evaluation suite with concrete quality thresholds.
- Add CI/CD release gates and watch them block a deliberate regression.
- Instrument observability for traces, telemetry, alerts, safety events, latency, and cost.
- Connect production traces back to evaluation and continuous improvement.
- Run the full loop on a red-to-green pull request and produce an evidence pack.

## Workshop structure

| Block | What attendees do | Built artifact |
|---|---|---|
| Foundations | Deploy travel-agent:1 and set up the agentops-vbd workspace and CLI. | Live agent and configured workspace. |
| Evaluate | Author an eval suite that scores the agent on real criteria. | Passing evaluation suite. |
| Ship | Turn the eval suite into a CI gate that blocks a regression. | Gated, passing pipeline. |
| Observe | Emit traces and correlate runtime telemetry to a release. | Dashboards and correlated traces. |
| Operate | Add safety follow-through and turn a trace into a new eval case. | Standing safety checks and a closed feedback loop. |
| Capstone | Drive a red pull request to green through the full loop. | Production-readiness evidence pack. |

## Workshop pages

| Page | Purpose |
|---|---|
| [Agenda]({{ '/long/agenda' | relative_url }}) | Full-day schedule. |
| [Lab roadmap]({{ '/long/lab-roadmap' | relative_url }}) | Lab sequence and learning objectives. |
| [Observability strategy]({{ '/long/observability-strategy' | relative_url }}) | Cross-cutting observability model for the full-day workshop. |
| [Lab guide]({{ '/long/labs/' | relative_url }}) | Step-by-step hands-on labs from Lab 1 through the capstone. |

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

This VBD track is not an AgentOps Accelerator walkthrough and not an app-build tutorial. It is a production-readiness working session around Microsoft Foundry, repo-side release evidence, CI/CD gates, Azure Monitor and Application Insights telemetry, safety review, and Day-2 operations.
