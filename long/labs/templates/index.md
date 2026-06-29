---
title: Templates
layout: default
parent: Labs
nav_order: 8
---

# Lab artefact templates

These are the downloadable templates that back the labs. There is one template per
artefact in the [lab roadmap]({{ '/long/lab-roadmap' | relative_url }}). Copy a template
into your own repository (under `docs/agentops/` or alongside `agentops.yaml`) and fill
it in as you work through the matching lab. By the capstone, every template should be
complete for one production-candidate agent.

Each template is plain markdown so it diffs cleanly in a pull request and can travel
with the agent's release evidence.

| # | Artefact | Template | Lab |
|---|---|---|---|
| 1 | Agent target inventory | [agent-target-inventory](agent-target-inventory/) | Lab 1 |
| 2 | Release-readiness contract | [release-readiness-contract](release-readiness-contract/) | Lab 1 |
| 3 | Evaluation dataset plan | [evaluation-dataset-plan](evaluation-dataset-plan/) | Lab 2 |
| 4 | Baseline and threshold plan | [baseline-and-threshold-plan](baseline-and-threshold-plan/) | Lab 2 |
| 5 | CI/CD gate plan | [cicd-gate-plan](cicd-gate-plan/) | Lab 3 |
| 6 | Readiness evidence package | [readiness-evidence-package](readiness-evidence-package/) | Lab 3 |
| 7 | Observability correlation model | [observability-correlation-model](observability-correlation-model/) | Lab 4 |
| 8 | Dashboard and alert plan | [dashboard-and-alert-plan](dashboard-and-alert-plan/) | Lab 4 |
| 9 | Safety and red-team follow-through plan | [safety-redteam-followthrough-plan](safety-redteam-followthrough-plan/) | Lab 5 |
| 10 | Incident response and continuous improvement plan | [incident-and-improvement-plan](incident-and-improvement-plan/) | Lab 6 |

## Naming and traceability

Every template carries the same identity block so the artefacts cross-reference cleanly:

- `agent_id` - stable identifier for the agent (matches `agentops.yaml`).
- `agent_version` - the `name:version` under review.
- `owner` - accountable owner and escalation path.
- `eval_run_id` - the evaluation run that produced the current evidence.
- `release_id` - the gate or release decision identifier.

Keep these consistent across all ten artefacts. The capstone relies on them to thread a
single trace back to its version, evaluation, release, and owner.
