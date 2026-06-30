---
title: "Capstone: Production-Readiness Review"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 7
---

# Capstone: Production-Readiness Review

The capstone assembles the outputs from every lab into a release-readiness narrative for one production-candidate agent.

## Duration

30 minutes

## Outcome

Attendees assemble a production-readiness narrative for one agent.

## Review questions

- What agent are we preparing to release?
- What release criteria have been defined?
- What evaluation evidence exists?
- What gates block regressions?
- What observability exists after release?
- What safety and governance evidence exists?
- Who owns incidents and readiness review?
- What production traces should become future evals?

## Artifact

A one-page readiness review:

- Release decision
- Evidence summary
- Open risks
- Observability coverage
- Safety findings
- Owner actions
- Next release improvements

## Review format

| Section | Decision evidence |
|---|---|
| Agent and release | Agent readiness profile from Lab 1. |
| Evaluation | Dataset, metrics, thresholds, baseline, and known gaps from Lab 2. |
| Shipping | Gate contract, evidence package, reviewers, and promotion criteria from Lab 3. |
| Observability | Trace schema, dashboard, alert, and trace-review workflow from Lab 4. |
| Safety and governance | Findings, controls, approvals, and risk acceptance from Lab 5. |
| Operate and improve | Incident path, root-cause model, and eval-backlog process from Lab 6. |

## Final decision

The team should leave with one of three outcomes:

| Outcome | Meaning |
|---|---|
| Ready to pilot | Evidence is sufficient for a controlled pilot, with known risks documented. |
| Needs remediation | Specific gaps must be closed before pilot or production promotion. |
| Not ready | The target agent lacks enough evidence, ownership, or observability to proceed. |

## Observability angle

The capstone should make observability visible in the final decision. The release should not be considered ready unless the team can find and explain production behavior through traces and telemetry.

## 30-day action backlog

Close with three owner-backed actions:

1. One evaluation improvement.
2. One release-gate or evidence improvement.
3. One observability or incident-response improvement.
