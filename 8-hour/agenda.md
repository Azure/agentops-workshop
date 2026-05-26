---
title: Agenda
layout: default
parent: 8-Hour Workshop
nav_order: 1
---

# 8-Hour Workshop Agenda

## Target audience

- AI application builders
- Cloud solution architects
- DevOps and platform engineers
- AI governance and Responsible AI stakeholders
- Technical decision makers responsible for production AI systems

## Prerequisite assumptions

The final implemented workshop will likely require:

- Access to a Microsoft Foundry project.
- A pre-created or sample agent.
- Permissions to view or configure evaluation, telemetry, and deployment artifacts.
- GitHub repository access for workflow and release-gate examples.
- Azure Monitor or Application Insights access for observability examples.

The current repository only defines the planning structure. Lab implementation details will be added later.

## Full-day flow

| Time | Segment | Format | Outcome |
|---:|---|---|---|
| 0:00-0:30 | Welcome and AgentOps foundations | Presentation | Align on the production-readiness problem and operating loop. |
| 0:30-1:30 | Lab 1: Foundations and control plane | Lab plan | Map the agent target, Foundry control plane, repo contract, and release-readiness question. |
| 1:30-1:45 | Break | Break | - |
| 1:45-3:00 | Lab 2: Evaluation design | Lab plan | Define dataset strategy, metrics, thresholds, and baseline comparison. |
| 3:00-4:00 | Lab 3: Release gates and evidence | Lab plan | Plan PR and deployment gates, reports, and readiness artifacts. |
| 4:00-4:45 | Lunch / extended break | Break | - |
| 4:45-6:15 | Lab 4: Observability and trace-driven operations | Lab plan | Plan agent traces, telemetry correlation, dashboards, alerts, and trace-to-eval feedback. |
| 6:15-6:30 | Break | Break | - |
| 6:30-7:15 | Lab 5: Safety, red-team follow-through, and governance | Lab plan | Plan safety evidence, governance ownership, auditability, and risk controls. |
| 7:15-7:50 | Lab 6: Incident response and continuous improvement | Lab plan | Plan diagnostics, incident workflow, trace triage, and eval-set updates. |
| 7:50-8:00 | Wrap-up and next steps | Discussion | Leave with a 30-day implementation plan for one production-candidate agent. |

## Delivery principle

Every lab should produce one artifact that contributes to release readiness. The full-day workshop should not become a collection of disconnected demos.
