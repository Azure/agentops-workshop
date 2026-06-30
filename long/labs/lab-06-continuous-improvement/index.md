---
title: "Lab 6: Incident Response and Continuous Improvement"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 6
---

# Lab 6: Incident Response and Continuous Improvement

This lab closes the AgentOps loop by turning production signals into stronger future releases.

## Duration

35 minutes

## Outcome

Attendees define how operational incidents, failed traces, and user feedback become fixes and future release gates.

## Concepts

- Incident triage
- Trace review
- Root cause categories
- Rollback or mitigation
- Eval-set expansion
- Ownership
- Continuous readiness review

## Artifact

A continuous improvement backlog:

- Incident intake path
- Trace triage checklist
- Fix workflow
- Eval-backlog update
- Release-gate update
- Owner and SLA

## Exercise flow

1. **Pick incident examples.** Use one bad answer, one failed tool call, one latency spike, and one safety event.
2. **Triage the trace.** Decide what data the responder needs to reconstruct the agent path.
3. **Classify root cause.** Map each issue to prompt, model, retrieval, tool, safety policy, app code, dependency, user behavior, or data freshness.
4. **Choose mitigation.** Decide whether to rollback, disable a tool, adjust prompt, update retrieval source, change threshold, or add guardrail.
5. **Update the system.** Convert the incident into eval rows, release-gate changes, dashboard changes, owner actions, and review cadence.

## Facilitator prompts

- What is the first place the on-call engineer looks?
- Which failures require rollback vs. safe degradation?
- How does the team prevent the same trace pattern from recurring?
- Which owner has to close the loop before the next release?

## Observability angle

Observability closes the AgentOps loop. A trace should lead to a diagnosis, a fix, a new eval row, and a stronger release gate.

## Completion criteria

- Incident intake path is documented.
- Root-cause categories are agreed.
- Trace triage checklist is ready.
- Eval-backlog and release-gate updates are part of the runbook.
