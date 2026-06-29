---
title: "Template: Observability correlation model"
layout: default
nav_exclude: true
---

# Observability correlation model

Produced in [Lab 4]({{ '/long/labs/lab-04-observability/' | relative_url }}). Defines the
trace schema and the correlation keys that let one trace answer questions across release,
runtime, evaluation, and Day-2.

```markdown
# Observability correlation model

agent_id:
agent_version:

## Trace schema (one agent interaction)

| Span | Captured by | Key attributes |
|---|---|---|
| User request | app | session_id, user_intent |
| Agent plan | Foundry | plan steps |
| Model call(s) | Foundry | model, tokens, latency |
| Retrieval | app / Foundry | sources, scores |
| Tool call(s) | Foundry | tool name, args, result, error |
| Safety event | Content Safety | category, action |
| Response | app | output, latency_total |
| Feedback | app | thumbs, comment |

## Correlation keys (must be present on every trace)

| Key | Source | Why |
|---|---|---|
| trace_id | OpenTelemetry | reconstruct the interaction |
| session_id | app | group multi-turn |
| agent_version | release metadata | which version produced it |
| deployment_id | release metadata | where it ran |
| eval_run_id | release metadata | which evidence shipped it |
| release_id | release metadata | which gate decision |
| owner | release metadata | who to route to |

## Coverage check

- What does Foundry capture automatically?
- What must the application add?
- Are all seven correlation keys present end to end? yes / no
```

This model is the heart of the observability thread: Lab 1 defines the keys, this lab
makes them present on every trace, and the capstone uses them to walk a single trace back
to its version, evaluation, release, and owner.
