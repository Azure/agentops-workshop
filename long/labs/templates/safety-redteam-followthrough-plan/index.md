---
title: "Template: Safety and red-team follow-through plan"
layout: default
nav_exclude: true
---

# Safety and red-team follow-through plan

Produced in [Lab 5]({{ '/long/labs/lab-05-safety-governance/' | relative_url }}). Tracks
safety findings from discovery to closed eval coverage, plus the governance ownership map.

```markdown
# Safety and red-team follow-through plan

agent_id:
agent_version:
owner:

## Risk categories in scope

| Category | In scope? | Notes |
|---|---|---|
| Harmful content |  |  |
| Jailbreak / prompt injection |  |  |
| Hallucination / ungrounded claims |  |  |
| Data exfiltration / PII leakage |  |  |

## Red-team findings

| Finding ID | Category | Severity | Status | Eval row added? | Owner |
|---|---|---|---|---|---|
|  |  |  | open / fixed / accepted |  |  |

## Cadence

- Pre-release gate: yes / no
- Scheduled scans: weekly / monthly
- Post-incident: required

## Governance and ownership (RACI)

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Evaluation sign-off |  |  |  |  |
| Release approval |  |  |  |  |
| Safety / red-team review |  |  |  |  |
| Incident response |  |  |  |  |
| Cost ownership |  |  |  |  |

## Accelerator and Foundry wiring

- Foundry AI Red Teaming Agent (PyRIT) produces adversarial findings.
- Each finding becomes an adversarial row in the eval dataset (Lab 2) for regression
  coverage, closing the loop.
```

A red-team finding is not closed when it is fixed; it is closed when it is covered by an
eval row that would catch the regression in a future release.
