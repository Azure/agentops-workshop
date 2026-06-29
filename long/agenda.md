---
title: Agenda
layout: default
parent: AgentOps VBD Workshop
nav_order: 3
---

# AgentOps Value Delivery Workshop Agenda

A full day (~8 hours of content plus breaks). The morning establishes the operating
model and the first three pillars; the afternoon goes deep on observability, then
safety, governance, and Day-2 operations, and closes with a capstone production-readiness
review.

## Target audience

- AI application builders
- Cloud solution architects
- DevOps and platform engineers
- AI governance and Responsible AI stakeholders
- Technical decision makers responsible for production AI systems

Assume a mixed audience. The labs are hands-on but stay no-code / low-code so leaders
and engineers can both follow them against a shared sample agent.

## Prerequisites

See the [prerequisites checklist]({{ '/long/prerequisites' | relative_url }}). In short,
each participant needs a Microsoft Foundry project, a sample agent, a GitHub repository,
Azure Monitor / Application Insights access, and the
[AgentOps Accelerator](https://github.com/Azure/agentops) installed
(`python -m pip install agentops-accelerator`).

## Full-day flow

| Time | Segment | Format | Outcome / artefact |
|---:|---|---|---|
| 0:00-0:30 | Kickoff and AgentOps foundations | Presentation | Align on the production gap, the four-pillar model, and the day's goal. |
| 0:30-1:30 | [Lab 1: Foundations and control plane](labs/lab-01-foundations/) | Lab (60 min) | Agent target inventory + release-readiness contract. |
| 1:30-1:40 | Break | Break | - |
| 1:40-2:55 | [Lab 2: Evaluation design](labs/lab-02-evaluation/) | Lab (75 min) | Evaluation dataset plan + baseline/threshold plan. |
| 2:55-3:55 | [Lab 3: Release gates and evidence](labs/lab-03-release-gates/) | Lab (60 min) | CI/CD gate plan + readiness evidence package. |
| 3:55-4:40 | Lunch | Break | - |
| 4:40-6:10 | [Lab 4: Observability and trace-driven operations](labs/lab-04-observability/) | Lab (90 min) | Observability correlation model + dashboard and alert plan. |
| 6:10-6:20 | Break | Break | - |
| 6:20-7:05 | [Lab 5: Safety, red-team follow-through, and governance](labs/lab-05-safety-governance/) | Lab (45 min) | Safety and red-team follow-through plan + governance/RACI map. |
| 7:05-7:40 | [Lab 6: Incident response and continuous improvement](labs/lab-06-continuous-improvement/) | Lab (35 min) | Incident response and continuous-improvement plan. |
| 7:40-8:10 | [Capstone: Production-readiness review](labs/capstone/) | Capstone (30 min) | Composed release-readiness review and go/no-go decision. |
| 8:10-8:20 | Closeout and 30-day plan | Discussion | Each attendee leaves with a 30-day plan for one agent. |

Total content time is about 8 hours including the kickoff, six labs, capstone, and
closeout. Breaks and lunch add roughly 75 minutes; schedule a start time that lets the
room finish with margin.

## How the labs fit together

Each lab produces at least one artefact from the
[lab roadmap]({{ '/long/lab-roadmap' | relative_url }}), and the capstone composes them
into a single release-readiness narrative. The morning (Labs 1-3) builds the release
contract and the evidence to ship; the afternoon (Labs 4-6) makes production behavior
observable, safe, and continuously improving. The
[observability thread]({{ '/long/observability-strategy' | relative_url }}) connects
the metadata across all of them.

## Delivery principle

Every lab produces one artefact that contributes to release readiness. The full-day
workshop is not a collection of disconnected demos: by the capstone, every artefact
should be filled in for one of the attendee's own production-candidate agents.
