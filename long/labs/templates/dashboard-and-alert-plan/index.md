---
title: "Template: Dashboard and alert plan"
layout: default
nav_exclude: true
---

# Dashboard and alert plan

Produced in [Lab 4]({{ '/long/labs/lab-04-observability/' | relative_url }}). Defines the
Azure Monitor / Application Insights views and the alerts that turn signals into action.

```markdown
# Dashboard and alert plan

agent_id:
app_insights_resource:
log_analytics_workspace:

## Dashboard views

### 1. Executive readiness view
- Release status, gate result, open readiness risks, recent incidents, safety status

### 2. Operations view
- Request volume, error rate, tool failures, latency p50/p95/p99, safety events, cost/tokens

### 3. Agent behavior view
- Trace samples, conversation outcomes, retrieval/tool paths, user feedback, quality trend

### 4. Continuous improvement view
- New regression candidates from traces, eval coverage gaps, red-team findings, open actions

## Alerts

| Alert | Signal | Threshold | Severity | Action / runbook |
|---|---|---|---|---|
| Tool dependency failure | tool error rate | > __% over 5 min | S2 | disable tool, fall back |
| Latency regression | p95 latency | > __ ms after deploy | S3 | pause canary, investigate |
| Cost / token spike | token usage | > __% of budget | S3 | throttle via gateway, notify FinOps |
| Safety blocks rising | content safety events | > __ over 1 h | S1 | block, content safety incident |
| Quality / feedback drop | thumbs-down rate | > __% | S2 | open ticket, sample into eval |
| Eval gate failure | CI gate | any | S2 | stop release |
| Missing telemetry | trace count | == 0 after deploy | S2 | check instrumentation |

## Accelerator wiring

- `agentops telemetry validate <name>` and `agentops telemetry import <name> --apply`
  bring Azure Monitor / App Insights signals into the workspace.
- `agentops cockpit` shows the production-signal snapshot and links to these views.
```

Each alert maps to a runbook entry in the incident and improvement plan (Lab 6).
