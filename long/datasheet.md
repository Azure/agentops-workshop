---
title: Datasheet
layout: default
parent: AgentOps VBD Workshop
nav_order: 1
---

# AgentOps Value Delivery Workshop - Datasheet

A one-day, hands-on engagement that takes one of your AI agents from "it works in testing"
to "we can operate it safely in production", using the four-pillar AgentOps operating
model on Microsoft Foundry.

## At a glance

| | |
|---|---|
| **Title** | AgentOps Value Delivery Workshop |
| **Format** | Full-day (~8 hours), instructor-led, hands-on |
| **Level** | Intermediate (no-code / low-code labs, some full-code optional) |
| **Delivery** | On-site or remote; one shared sample agent plus each attendee's own agent |
| **Audience size** | 6-20 participants |
| **Control plane** | Microsoft Foundry |
| **Observability** | Azure Monitor + Application Insights |
| **Reference implementation** | [AgentOps Accelerator](https://github.com/Azure/agentops) (open source) |

## Who it is for

- AI application builders and architects
- DevOps and platform engineers
- AI governance and Responsible AI stakeholders
- Technical decision makers responsible for production AI systems

## What attendees learn

The four-pillar AgentOps operating model, applied end to end on one real agent:

- **Evaluate** - golden datasets, Foundry evaluators, thresholds, and baseline comparison.
- **Ship** - CI/CD release gates, environment promotion, and reviewable release evidence.
- **Observe** - trace schemas, correlation keys, dashboards, alerts, and the trace-to-eval
  loop.
- **Operate** - safety and red-team follow-through, governance, incident response, and
  continuous improvement.

## What attendees walk away with

For one production-candidate agent, a complete release-readiness package:

1. Agent target inventory and release-readiness contract
2. Evaluation dataset plan with thresholds and a baseline comparison
3. CI/CD gate plan and a readiness evidence package
4. Observability correlation model plus a dashboard and alert plan
5. Safety and red-team follow-through plan and a governance / RACI map
6. Incident response and continuous-improvement plan
7. A capstone go / no-go decision and a 30-day plan

## Outcomes

- A repeatable pattern for moving agents to production, proven on one agent.
- Release evidence that a human can review and an auditor can reproduce.
- A production trace that can be walked back to its version, evaluation, release, and
  owner.

## Duration and structure

Kickoff, six hands-on labs, a capstone review, and a closeout. See the
[agenda]({{ '/long/agenda' | relative_url }}) for the full-day flow and the
[lab roadmap]({{ '/long/lab-roadmap' | relative_url }}) for objectives and artefacts.

## Prerequisites

A Microsoft Foundry project, a sample agent, a GitHub repository, Azure Monitor /
Application Insights access, and named participants. Full details in the
[prerequisites checklist]({{ '/long/prerequisites' | relative_url }}).

## Related

The [AgentOps Briefing]({{ '/short/' | relative_url }}) (~1 hour) is the executive-level
introduction to the same operating model and is a good primer before this workshop.
