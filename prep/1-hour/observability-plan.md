---
title: Observability Plan
layout: default
parent: 1-Hour Session
nav_order: 4
---

# Observability Plan for the 1-Hour Session

## Positioning

Observability is one of the most important differentiators in the AgentOps story. For traditional services, monitoring often starts with availability, latency, errors, and resource health. For AI agents, those signals are necessary but not sufficient.

Agent observability must answer:

- What did the user ask?
- What did the agent decide to do?
- Which model, prompt, retrieval source, memory, or tool influenced the response?
- Which safety events fired?
- Which release version produced the behavior?
- Did quality, cost, latency, safety, or user feedback change after release?
- Which production traces should become future evaluation cases?

## Core message

> AgentOps observability turns production behavior into release evidence and future evaluation coverage.

## Observability signals to explain

| Signal | Why it matters |
|---|---|
| Conversation trace | Reconstructs the end-to-end user journey and agent behavior. |
| Model calls | Shows prompt, model, token usage, latency, and response behavior. |
| Retrieval events | Explains grounding, source selection, freshness, and missing context. |
| Tool calls | Shows external dependencies, failures, arguments, latency, and side effects. |
| Safety events | Captures blocked content, jailbreak attempts, policy violations, and red-team findings. |
| Eval results | Connects pre-release evidence to production behavior. |
| Release metadata | Correlates traces to version, environment, commit, prompt, and deployment. |
| User feedback | Captures business-facing quality signals and escalation paths. |
| Cost and latency | Helps teams operate within performance and budget targets. |

## Correlation model

The 1-hour session should show that observability depends on correlation, not isolated dashboards.

Minimum correlation fields to mention:

- Agent name and version
- Environment
- Release or deployment ID
- Commit or prompt version
- Trace ID
- Session or conversation ID
- Eval run ID
- Dataset or test case ID
- Incident or alert ID
- Owner or service team

## Recommended slide treatment

Use two observability slides:

1. **Observability for agents is more than monitoring**
   - Contrast endpoint monitoring with trace-level agent observability.
   - Show a trace waterfall across prompt, model, retrieval, tools, safety, and response.

2. **From telemetry to action**
   - Show the closed loop from production trace to diagnosis, new eval row, release gate, and improved production behavior.

## Observability narrative in the deck

Without an embedded demo block, the slides themselves carry the observability story. The narrative flow:

1. After the CI/CD gate slide (slide 14), transition into observability as the post-release operating layer.
2. On slide 16, show a trace waterfall conceptually: a single user interaction decomposing into prompt, model call, retrieval, tool call, response, and safety event.
3. Connect the trace to release context: agent version, deployment, eval run, owner.
4. On slide 17, show the closed loop: traces become diagnoses, diagnoses become eval rows, eval rows become future gates.
5. Transition into Day-2 by showing how the incident runbook (slide 20) consumes traces as the primary triage signal.

An optional backup video (see `demo-video-plan.md`) may visualize this flow with real screenshots and traces, but the slides do not depend on it.

## Avoid

- Do not equate observability with a generic monitoring dashboard.
- Do not focus only on infrastructure metrics.
- Do not imply that traces replace evaluation.
- Do not show logs without explaining how they connect to release decisions.
- Do not over-index on one tool; the operating model matters more than a specific UI.
