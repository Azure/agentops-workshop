---
title: Lab Roadmap
layout: default
parent: AgentOps VBD Workshop
nav_order: 4
---

# Lab Roadmap

This roadmap defines the lab sequence, learning objectives, and the artefact each lab
produces. The labs are implemented under [`long/labs/`](labs/) and use the four-pillar
AgentOps model (Evaluate -> Ship -> Observe -> Operate) with the
[AgentOps Accelerator](https://github.com/Azure/agentops) as the reference
implementation.

## Planned labs

| Lab | Duration | Level | Planned outcome |
|---|---:|---|---|
| [Lab 1: Foundations and control plane](labs/lab-01-foundations/) | 60 min | no-code / low-code | Identify the agent target, Foundry project, repo contract, and production-readiness question. |
| [Lab 2: Evaluation design](labs/lab-02-evaluation/) | 75 min | low-code | Define dataset, metrics, thresholds, baseline comparison, and regression candidates. |
| [Lab 3: Release gates and evidence](labs/lab-03-release-gates/) | 60 min | low-code / full-code | Plan PR gates, deploy gates, eval reports, readiness evidence, and review workflow. |
| [Lab 4: Observability and trace-driven operations](labs/lab-04-observability/) | 90 min | low-code | Plan trace collection, telemetry correlation, dashboards, alerts, and trace-to-eval feedback. |
| [Lab 5: Safety, red-team follow-through, and governance](labs/lab-05-safety-governance/) | 45 min | no-code / low-code | Plan safety findings, policy evidence, governance ownership, and auditability. |
| [Lab 6: Incident response and continuous improvement](labs/lab-06-continuous-improvement/) | 35 min | no-code / low-code | Plan incident triage, diagnosis, fixes, and future eval coverage. |
| [Capstone: Production-readiness review](labs/capstone/) | 30 min | discussion | Assemble the readiness narrative for one production-candidate agent. |

## Cross-lab artifacts

The workshop produces ten artefacts, one per row below. Each has a downloadable
[template](labs/templates/):

| Artefact | Template | Produced in |
|---|---|---|
| Agent target inventory | [agent-target-inventory.md](labs/templates/agent-target-inventory/) | Lab 1 |
| Release-readiness contract | [release-readiness-contract.md](labs/templates/release-readiness-contract/) | Lab 1 |
| Evaluation dataset plan | [evaluation-dataset-plan.md](labs/templates/evaluation-dataset-plan/) | Lab 2 |
| Baseline and threshold plan | [baseline-and-threshold-plan.md](labs/templates/baseline-and-threshold-plan/) | Lab 2 |
| CI/CD gate plan | [cicd-gate-plan.md](labs/templates/cicd-gate-plan/) | Lab 3 |
| Readiness evidence package | [readiness-evidence-package.md](labs/templates/readiness-evidence-package/) | Lab 3 |
| Observability correlation model | [observability-correlation-model.md](labs/templates/observability-correlation-model/) | Lab 4 |
| Dashboard and alert plan | [dashboard-and-alert-plan.md](labs/templates/dashboard-and-alert-plan/) | Lab 4 |
| Safety and red-team follow-through plan | [safety-redteam-followthrough-plan.md](labs/templates/safety-redteam-followthrough-plan/) | Lab 5 |
| Incident response and continuous improvement plan | [incident-and-improvement-plan.md](labs/templates/incident-and-improvement-plan/) | Lab 6 |

## Observability thread

Observability should not be isolated to Lab 4. Each lab should preserve traceability:

- Lab 1 defines the target and version identity.
- Lab 2 defines which eval cases and metrics need production correlation.
- Lab 3 attaches release evidence to CI/CD decisions.
- Lab 4 builds the observability model.
- Lab 5 tracks safety and governance signals.
- Lab 6 turns incidents and traces into future eval rows.
- The capstone combines all evidence into a release-readiness review.
