---
title: Observability Strategy
layout: default
parent: AgentOps VBD Workshop
nav_order: 3
---

# Observability Strategy

## Why observability is central

AgentOps depends on observability because agent behavior cannot be understood from infrastructure metrics alone. Teams need to reconstruct the chain of decisions and dependencies behind an answer, a failed tool call, a safety block, a hallucination, a latency spike, or a cost regression.

AgentOps Value Delivery Workshop teaches observability as a practical system:

1. **Collect** traces, telemetry, safety events, feedback, latency, cost, and release metadata.
2. **Correlate** every signal to agent version, deployment, eval run, trace ID, and owner.
3. **Visualize** operational health, behavior quality, safety, and cost.
4. **Alert** on production-impacting signals.
5. **Diagnose** issues from traces and evidence.
6. **Improve** by promoting production traces into future evaluation rows.

## Observability domains

| Domain | Coverage |
|---|---|
| Trace observability | User request, agent decision path, model calls, retrieval, tool calls, safety events, response, feedback. |
| Release observability | Version, deployment, commit, prompt, environment, eval run, and gate result. |
| Quality observability | Eval trends, baseline deltas, production feedback, trace review outcomes. |
| Safety observability | Content safety events, red-team findings, jailbreak attempts, blocked responses, policy outcomes. |
| Reliability observability | Errors, timeouts, dependency failures, tool-call failures, retry behavior. |
| Performance observability | Latency, tokens, throughput, cold starts, slow dependencies. |
| Cost observability | Token usage, model mix, gateway controls, budget signals, per-agent cost. |
| Operations observability | Alerts, owners, incidents, service health, escalation path, review cadence. |

## Lab 4 focus

Lab 4 is the deepest observability experience. It guides attendees through:

- Defining a trace schema for an agent interaction.
- Identifying what Foundry captures and what the application must add.
- Correlating traces with eval runs and release versions.
- Designing an Azure Monitor or Application Insights view for agent operations.
- Defining alerts for failed tools, safety events, latency regression, cost spikes, and quality drift.
- Reviewing a trace and deciding whether it should become a new eval case.
- Adding an observability section to the readiness evidence package.

## Dashboard design

The workshop includes a dashboard design with these views:

1. **Executive readiness view**
   - Release status
   - Gate result
   - Open readiness risks
   - Recent incidents
   - Safety status

2. **Operations view**
   - Request volume
   - Error rate
   - Tool failures
   - Latency percentiles
   - Safety events
   - Cost and token usage

3. **Agent behavior view**
   - Trace samples
   - Conversation outcomes
   - Retrieval/tool paths
   - User feedback
   - Quality trend

4. **Continuous improvement view**
   - New regression candidates from traces
   - Eval coverage gaps
   - Red-team findings
   - Open action items

## Alert model

Alert categories:

- Tool dependency failure above threshold
- Latency regression after deployment
- Cost or token usage spike
- Increase in safety blocks or policy violations
- Drop in user feedback quality
- Eval gate failure
- Missing telemetry after deployment
- Production trace pattern not covered by evaluations

## Capstone expectation

The capstone should require attendees to answer:

> If this agent produces a bad answer in production tomorrow, can we find the trace, understand what happened, identify the shipped version, route it to the right owner, and prevent the same failure in the next release?
