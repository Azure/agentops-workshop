---
title: Lab Roadmap
layout: default
parent: 8-Hour Workshop
nav_order: 2
---

# Lab Roadmap

This roadmap defines the intended lab sequence. The labs are placeholders for now and should not be implemented until the workshop plan is approved.

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

The implemented workshop should eventually produce these artifacts:

- Agent target inventory
- Release-readiness contract
- Evaluation dataset plan
- Baseline and threshold plan
- CI/CD gate plan
- Readiness evidence package
- Observability correlation model
- Dashboard and alert plan
- Safety and red-team follow-through plan
- Incident response and continuous improvement plan

## Observability thread

Observability should not be isolated to Lab 4. Each lab should preserve traceability:

- Lab 1 defines the target and version identity.
- Lab 2 defines which eval cases and metrics need production correlation.
- Lab 3 attaches release evidence to CI/CD decisions.
- Lab 4 builds the observability model.
- Lab 5 tracks safety and governance signals.
- Lab 6 turns incidents and traces into future eval rows.
- The capstone combines all evidence into a release-readiness review.
