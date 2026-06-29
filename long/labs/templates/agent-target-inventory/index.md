---
title: "Template: Agent target inventory"
layout: default
nav_exclude: true
---

# Agent target inventory

Produced in [Lab 1]({{ '/long/labs/lab-01-foundations/' | relative_url }}). One row per
agent you are considering for production. The goal is to pick exactly one
production-candidate agent to carry through the rest of the day.

```markdown
# Agent target inventory

| Field | Value |
|---|---|
| agent_id |  |
| Display name |  |
| Business purpose (one sentence) |  |
| Agent type | Prompt agent / Hosted agent / HTTP endpoint |
| Foundry project |  |
| Foundry project endpoint |  |
| Current environment | sandbox / dev / qa / prod |
| Source repository |  |
| Owner (accountable) |  |
| Escalation contact |  |
| Knowledge sources (RAG) |  |
| Tools / MCP servers |  |
| External dependencies |  |
| Known risks today |  |
| Production-candidate? | yes / no |

## Selection rationale

- Why this agent is the right first candidate:
- Why now:
- What "in production" means for this agent:
```

The selected `agent_id`, `agent_version`, `owner`, and Foundry project carry forward into
every other artefact. Keep them identical so the release evidence threads together.
