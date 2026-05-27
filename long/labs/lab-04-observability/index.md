---
title: "Lab 4: Observability and Trace-Driven Operations"
layout: default
parent: Lab Planning Pages
grand_parent: Long Workshop
nav_order: 4
---

# Lab 4: Observability and Trace-Driven Operations

{: .planning }
This is a planning placeholder. Lab implementation content has not been written yet.

## Planned duration

90 minutes

## Planned outcome

Attendees design an observability model for a production AI agent and connect traces back to evaluation, release evidence, and incident response.

## Planned concepts

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

## Planned artifact

An observability design:

- Trace schema
- Correlation fields
- Dashboard views
- Alert categories
- Telemetry ownership
- Post-release verification checklist
- Trace review workflow
- Eval-backlog promotion criteria

## Planned exercise flow

1. Identify the agent interaction path.
2. List the trace spans needed to explain behavior.
3. Define correlation fields across Foundry, repo, CI/CD, and Azure Monitor.
4. Design the operations dashboard.
5. Define alerts for tool failure, latency regression, safety events, and cost spikes.
6. Review an example trace and decide whether it becomes a new eval case.
7. Add observability evidence to the release-readiness package.

## Observability model

Minimum signals:

- User request
- Agent plan or reasoning boundary, where available
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

## Implementation backlog

- Decide which telemetry views are available in the demo environment.
- Create safe sample traces or screenshots if live telemetry is not available.
- Define KQL examples later, if appropriate.
- Decide whether dashboards are built live or shown as planning artifacts.
- Add a trace-review worksheet.
