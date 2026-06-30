---
title: "Lab 4: Observability and Trace-Driven Operations"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 4
---

# Lab 4: Observability and Trace-Driven Operations

This lab is the center of the VBD workshop. It defines how the team sees, diagnoses, and improves agent behavior after release.

## Duration

90 minutes

## Outcome

Attendees design an observability model for a production AI agent and connect traces back to evaluation, release evidence, and incident response.

## Concepts

- Agent traces
- Model call telemetry
- Retrieval and tool-call telemetry
- Safety events
- User feedback
- Latency, error, and cost signals
- Release metadata
- Azure Monitor and Application Insights views
- Foundry trace and evaluation context
- Trace-to-evaluation feedback loop

## Artifact

An observability design:

- Trace schema
- Correlation fields
- Dashboard views
- Alert categories
- Telemetry ownership
- Post-release verification checklist
- Trace review workflow
- Eval-backlog promotion criteria

## Exercise flow

1. Identify the agent interaction path.
2. List the trace spans needed to explain behavior.
3. Define correlation fields across Foundry, repo, CI/CD, and Azure Monitor.
4. Design the operations dashboard.
5. Define alerts for tool failure, latency regression, safety events, and cost spikes.
6. Review an example trace and decide whether it becomes a new eval case.
7. Add observability evidence to the release-readiness package.

## Dashboard design exercise

Design four views:

| View | Must answer |
|---|---|
| Executive readiness | Is this release healthy, blocked, or carrying accepted risk? |
| Operations | Are users seeing errors, latency, failed tools, safety events, or cost spikes? |
| Agent behavior | What path did the agent take through model, retrieval, tools, and safety controls? |
| Improvement backlog | Which traces, feedback, or incidents should become new eval cases? |

## Facilitator prompts

- Could an on-call engineer explain a bad answer from one trace?
- Which signals live in Foundry and which must come from the app or gateway?
- Which dashboard view would a service owner check every morning?
- Which telemetry gaps would block production release?

## Observability model

Minimum signals:

- User request
- Agent decision path or reasoning boundary, where available
- Model call
- Retrieval event
- Tool call
- Safety event
- Response
- User feedback
- Latency
- Token usage and cost
- Release version
- Eval run or dataset reference

Minimum correlation:

- Trace ID
- Conversation or session ID
- Agent name and version
- Environment
- Deployment ID
- Commit or prompt version
- Eval run ID
- Incident or alert ID
- Owner

## Completion criteria

- Trace spans and correlation fields are defined.
- Dashboard views are sketched.
- Alert categories are mapped to owners.
- The team has a rule for turning traces into evaluation backlog items.
