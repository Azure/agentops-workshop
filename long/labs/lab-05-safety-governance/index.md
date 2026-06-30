---
title: "Lab 5: Safety, Red-Team Follow-Through, and Governance"
layout: default
parent: Lab Planning Pages
grand_parent: AgentOps VBD Workshop
nav_order: 5
---

# Lab 5: Safety, Red-Team Follow-Through, and Governance

This lab makes safety and governance operational rather than a one-time review.

## Duration

45 minutes

## Outcome

Attendees plan how Responsible AI findings, safety policies, red-team results, and governance controls become operational evidence.

## Concepts

- Content safety
- Red-team findings
- Jailbreak and adversarial prompts
- Policy mapping
- RBAC and auditability
- Owner review
- Risk acceptance
- Governance cadence

## Artifact

A safety and governance plan:

- Safety signal inventory
- Red-team finding workflow
- Governance owner
- Approval path
- Audit evidence
- Risk register link
- Eval updates from safety findings

## Exercise flow

1. **List safety scenarios.** Identify content safety, groundedness, privacy, tool misuse, jailbreak, and policy risks.
2. **Map controls.** Connect each risk to prevention, detection, review, and response controls.
3. **Define red-team follow-through.** Decide how findings are tracked, retested, and converted into future eval cases.
4. **Assign governance owners.** Name who reviews safety evidence, approves risk acceptance, and audits the release.
5. **Connect telemetry.** Decide how safety blocks, policy violations, and adversarial attempts appear in traces and dashboards.

## Facilitator prompts

- What safety finding would stop the release?
- Who can accept residual risk, and where is that decision recorded?
- How does a red-team finding become a regression test?
- Can safety events be queried by agent version and release?

## Observability angle

Safety events must be observable in production. The lab plans how safety blocks, policy violations, jailbreak attempts, and red-team regressions appear in traces, dashboards, alerts, and readiness evidence.

## Completion criteria

- Safety scenarios are linked to controls.
- Red-team follow-through is explicit.
- Governance approvals and risk acceptance are documented.
- Safety telemetry is part of the observability plan.
