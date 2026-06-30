---
title: Agenda
layout: default
parent: AgentOps VBD Workshop
nav_order: 1
---

# AgentOps Value Delivery Workshop Agenda

This is the full-day VBD version of the AgentOps workshop. It is designed as a facilitated working session for one customer team and one production-candidate agent.

## Target audience

- AI application builders
- Cloud solution architects
- DevOps and platform engineers
- AI governance and Responsible AI stakeholders
- Technical decision makers responsible for production AI systems

## Prerequisites

The workshop can be run in two modes:

- **Design-lab mode** - use the customer's real agent, repo, Foundry project, and telemetry access.
- **Tabletop mode** - use the provided prompts and worksheets when live access is not available.

For design-lab mode, attendees should have:

- Access to a Microsoft Foundry project.
- A pre-created or sample agent.
- Permissions to view or configure evaluation, telemetry, and deployment artifacts.
- GitHub repository access for workflow and release-gate examples.
- Azure Monitor or Application Insights access for observability examples.

## Full-day flow

| Time | Segment | Format | Outcome |
|---:|---|---|---|
| 0:00-0:30 | Welcome and AgentOps foundations | Presentation + discussion | Align on the production-readiness problem and the four-pillar AgentOps model. |
| 0:30-1:30 | Lab 1: Foundations and control plane | Guided working session | Map the agent target, Foundry control plane, repo contract, and release-readiness question. |
| 1:30-1:45 | Break | Break | - |
| 1:45-3:00 | Lab 2: Evaluation design | Guided working session | Define dataset strategy, metrics, thresholds, and baseline comparison. |
| 3:00-4:00 | Lab 3: Release gates and evidence | Guided working session | Define PR and deployment gates, reports, and readiness artifacts. |
| 4:00-4:45 | Lunch / extended break | Break | - |
| 4:45-6:15 | Lab 4: Observability and trace-driven operations | Guided working session | Define agent traces, telemetry correlation, dashboards, alerts, and trace-to-eval feedback. |
| 6:15-6:30 | Break | Break | - |
| 6:30-7:15 | Lab 5: Safety, red-team follow-through, and governance | Guided working session | Define safety evidence, governance ownership, auditability, and risk controls. |
| 7:15-7:50 | Lab 6: Incident response and continuous improvement | Guided working session | Define diagnostics, incident workflow, trace triage, and eval-set updates. |
| 7:50-8:00 | Wrap-up and next steps | Discussion | Leave with a 30-day implementation backlog for one production-candidate agent. |

## Facilitator checkpoints

| Checkpoint | Question |
|---|---|
| End of Lab 1 | Can the team name the exact agent version and production-readiness decision? |
| End of Lab 2 | Are quality, groundedness, safety, latency, and cost gates measurable? |
| End of Lab 3 | Would a failing evaluation block the release in the real delivery path? |
| End of Lab 4 | Can the team trace a production answer back to version, deployment, eval run, and owner? |
| End of Lab 5 | Are safety findings connected to governance, telemetry, and future evaluations? |
| End of Lab 6 | Does the incident workflow create stronger future release gates? |

## Delivery principle

Every lab should produce one artifact that contributes to release readiness. The full-day workshop should not become a collection of disconnected demos.
