---
title: Agenda
layout: default
parent: 1-Hour Session
nav_order: 1
---

# 1-Hour Session Agenda

## Recommended title

**From Agent Prototype to Production: AgentOps Readiness on Microsoft Foundry**

Other options:

1. **AgentOps for Production-Ready AI Agents on Microsoft Foundry**
2. **Evaluate, Gate, Observe, Diagnose, Ship: An AgentOps Model for AI Agents**
3. **From Agent Demos to Reliable Operations: A Practical AgentOps Session**
4. **Operationalizing AI Agents with Evaluation, Observability, and CI/CD Gates**

## Abstract

AI agents are moving quickly from prototypes into customer-facing and business-critical workflows. That shift creates a new operational challenge: teams need confidence that agents are evaluated consistently, monitored effectively, governed responsibly, and released through repeatable gates.

In this 1-hour session, we introduce a practical AgentOps operating model for production AI agents on Microsoft Foundry. We cover evaluation strategy, CI/CD quality gates, observability, diagnostics, Responsible AI readiness, red-team follow-through, and Day-2 operations. The session includes a demo story showing a release-readiness flow: an existing Foundry agent is evaluated, a regression is blocked before release, the issue is fixed, readiness evidence is reviewed, and telemetry links the release decision back to runtime behavior.

Attendees leave with a production-readiness checklist and a practical starting path for moving one agent from "it works in testing" to "we can operate this safely."

## Timeboxed flow

| Time | Segment | Purpose |
|---:|---|---|
| 0:00-0:03 | Opening and promise | Frame the shift from prototype success to production confidence. |
| 0:03-0:08 | Why AgentOps now | Explain quality, safety, monitoring, ownership, release risk, and cost. |
| 0:08-0:13 | Complexity from prompts to agents | Show why agentic systems need stronger operating discipline. |
| 0:13-0:18 | AgentOps operating model | Introduce Evaluate, Gate, Observe, Diagnose, Ship, Improve. |
| 0:18-0:24 | Lifecycle and maturity | Give customers a simple self-assessment model. |
| 0:24-0:30 | Foundry control plane and readiness checklist | Clarify roles across Foundry, Azure Monitor, repo, and CI/CD. |
| 0:30-0:36 | Evaluation, safety, and release gates | Show how release evidence is produced and enforced. |
| 0:36-0:44 | Observability for agents | Explore traces, telemetry correlation, dashboards, alerting, and trace-to-eval feedback. |
| 0:44-0:53 | Demo video | Show a regression caught, fixed, observed, and promoted with evidence. |
| 0:53-0:57 | What the demo proved | Translate demo actions into AgentOps practices. |
| 0:57-1:00 | Adoption blueprint and close | Start with one production-candidate agent and define release criteria. |

## Speaker guidance

Emphasize:

- The customer problem is production confidence, not tooling novelty.
- The strongest value moment is the failed gate: if the agent regresses, the release stops.
- Foundry remains the control plane and system of record.
- AgentOps adds the repeatable operating loop around evaluation, repo, CI/CD, diagnostics, observability, and release evidence.
- Observability must connect runtime traces to release decisions and future evaluations.
- AgentOps Toolkit can be shown as a reference accelerator for the demo, but it should not dominate the storyline.

Avoid:

- Making the session about AgentOps Toolkit.
- Starting with installation details.
- Spending too much time on command syntax.
- Describing AgentOps as a replacement for Foundry.
- Treating observability as generic infrastructure monitoring.
