---
title: Agenda
layout: default
parent: AgentOps VBD Workshop
nav_order: 1
---

# AgentOps Value Delivery Workshop Agenda

This is the full-day VBD version of the AgentOps workshop. It is a hands-on lab day for one team and one agent: attendees install the Azure AgentOps accelerator, deploy the Contoso Travel Agent to Microsoft Foundry, and operate it end to end. Each lab builds on the artifact the previous lab produced.

## Target audience

- AI application builders
- Cloud solution architects
- DevOps and platform engineers
- AI governance and Responsible AI stakeholders
- Technical decision makers responsible for production AI systems

## Prerequisites

The labs are hands-on against a real Microsoft Foundry project. Before the workshop, each attendee should have:

- An Azure subscription and access to a Microsoft Foundry project (model `gpt-4o-mini` or equivalent).
- Python 3.10+, the Azure CLI, and git installed locally.
- A GitHub repository they can push to (used for the CI/CD release gate).
- An Application Insights resource for observability (Lab 4).
- Permissions to deploy an agent and view evaluation, telemetry, and deployment artifacts.

If live Azure access is not available for some attendees, they can pair with a teammate who does; the continuity spine means every attendee still sees the full end-to-end flow.

## Full-day flow

Per-lab learning objectives and the artifact each lab hands to the next are in the [Lab roadmap]({{ '/long/lab-roadmap' | relative_url }}). Lab time budgets below are tuned to fit an eight-hour day.

| Time | Segment | Format | Outcome |
|---:|---|---|---|
| 0:00-0:30 | Welcome and AgentOps foundations | Presentation + discussion | Align on the production-readiness problem and the four-pillar AgentOps model. |
| 0:30-1:15 | Lab 1: Foundations and control plane | Hands-on lab | Install the accelerator, deploy `travel-agent:1` to Foundry, and run `agentops init`. |
| 1:15-2:15 | Lab 2: Evaluation | Hands-on lab | Build a JSONL dataset, set thresholds, run `agentops eval run`, and capture a green baseline. |
| 2:15-3:10 | Lab 3: Release gates and evidence | Hands-on lab | Regress to `travel-agent:2`, fail the baseline-compared gate, and produce an evidence pack. |
| 3:10-3:20 | Break | Break | - |
| 3:20-4:35 | Lab 4: Observability and trace-driven operations | Hands-on lab | Turn on Foundry + App Insights tracing, import telemetry, open Cockpit, and drill into a trace. |
| 4:35-5:15 | Lunch | Break | - |
| 5:15-6:05 | Lab 5: Safety, red-team follow-through, and governance | Hands-on lab | Add a content-safety evaluator, wire governance-as-code, and run a Foundry red-team scan. |
| 6:05-6:50 | Lab 6: Incident response and continuous improvement | Hands-on lab | Promote a real trace into the dataset, re-evaluate, and move the baseline forward. |
| 6:50-7:00 | Break | Break | - |
| 7:00-7:50 | Capstone: Production-readiness review | Hands-on lab | Generate a GitHub Actions PR gate, prove it green and red, and sign a ship decision. |
| 7:50-8:00 | Wrap-up and next steps | Discussion | Leave with a working pipeline, an evidence pack, and a 30-day backlog. |

## Facilitator checkpoints

| Checkpoint | Question |
|---|---|
| End of Lab 1 | Is `travel-agent:1` deployed and does `agentops init` succeed against the workspace? |
| End of Lab 2 | Does `agentops eval run` produce a green baseline with measurable thresholds? |
| End of Lab 3 | Does the weakened `travel-agent:2` make the gate exit non-zero and produce an evidence pack? |
| End of Lab 4 | Can the team trace a production answer back to version, deployment, eval run, and owner? |
| End of Lab 5 | Are content-safety and red-team findings recorded in the evidence pack and governance files? |
| End of Lab 6 | Did a real trace become a permanent regression row that the baseline now covers? |
| End of Capstone | Does the GitHub Actions gate block the red PR and pass once it is fixed? |

## Delivery principle

Every lab produces one working artifact that the next lab consumes. The full-day workshop is one continuous build, not a collection of disconnected demos.
