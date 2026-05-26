---
title: AgentOps Operating Model
layout: default
parent: Source Materials
nav_order: 2
---

# AgentOps Operating Model

## Definition

AgentOps is the operating model for moving AI agents from prototype to production with evaluation, release gates, observability, diagnostics, safety, governance, and continuous improvement.

It is not a single tool. It is a set of practices that connect Foundry, repo workflows, CI/CD, telemetry, ownership, and release evidence.

## Operating loop

| Step | Meaning | Evidence |
|---|---|---|
| Evaluate | Measure quality, safety, groundedness, behavior, latency, and cost before release. | Eval results, baseline comparison, threshold status. |
| Gate | Enforce release criteria in pull request and deployment workflows. | Passing or failing gates, workflow logs, readiness report. |
| Observe | Capture runtime behavior after release. | Traces, telemetry, dashboards, alerts, safety events, user feedback. |
| Diagnose | Use evidence to understand failures, regressions, incidents, and drift. | Trace review, incident record, root cause, owner action. |
| Ship | Promote only when release evidence supports the decision. | Release package, approval record, post-release checks. |
| Improve | Feed production learnings back into future evals and gates. | New eval rows, updated thresholds, improved prompts/tools/policies. |

## Foundry role

Microsoft Foundry should be positioned as the control plane for agent lifecycle, models, evaluation, tracing, safety, and governance.

AgentOps should be positioned as the operating model that connects Foundry signals to release decisions, repo-side practices, CI/CD gates, readiness checks, diagnostics, and Day-2 operations.

## Observability role

Observability is central because agent behavior cannot be understood from infrastructure metrics alone.

Agent observability should explain:

- What the user asked.
- What the agent planned or attempted.
- Which model calls were made.
- Which retrieval sources were used.
- Which tools were invoked.
- Which safety events fired.
- Which version produced the behavior.
- Whether quality, latency, cost, safety, or user feedback changed after release.
- Which traces should become future evaluation rows.

## Release-readiness evidence

A release-readiness package should eventually include:

- Agent target and version.
- Eval dataset and thresholds.
- Baseline comparison.
- Gate result.
- Observability links.
- Safety and red-team status.
- Known risks.
- Owner and escalation path.
- Next eval improvements.

## Adoption principle

Do not start by trying to operationalize every agent. Start with one production-candidate agent, define its release criteria, wire evaluation and observability, and use that pattern as the repeatable model.
