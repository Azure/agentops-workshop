---
title: "Template: Release-readiness contract"
layout: default
nav_exclude: true
---

# Release-readiness contract

Produced in [Lab 1]({{ '/long/labs/lab-01-foundations/' | relative_url }}). The contract
turns "I think it works" into "we have evidence for this release". It is the checklist
every later artefact fills in.

```markdown
# Release-readiness contract

agent_id:
agent_version:
owner:
environment_target: dev / qa / prod

## Release-readiness question

> If this agent ships and produces a bad answer in production tomorrow, can we find the
> trace, identify the version, route it to the right owner, and prevent the same failure
> in the next release?

## Criteria (each must be met to ship)

| # | Criterion | Owner | Evidence link | Status |
|---|---|---|---|---|
| 1 | Target and version are explicit | | | not met |
| 2 | Eval dataset and thresholds exist | | | not met |
| 3 | Baseline comparison is green | | | not met |
| 4 | CI/CD gate blocks regressions | | | not met |
| 5 | Telemetry and traces are wired | | | not met |
| 6 | Safety and red-team findings are tracked | | | not met |
| 7 | Release evidence is reviewable | | | not met |
| 8 | Owners know what to do when signals fail | | | not met |

## Out of scope for this release

-

## Sign-off

- Prepared by:
- Reviewed by:
- Decision (go / no-go):
- Date:
```

Map each criterion to the artefact that satisfies it: criterion 2 and 3 -> evaluation
dataset and baseline plans (Lab 2); criterion 4 and 7 -> CI/CD gate plan and readiness
evidence package (Lab 3); criterion 5 -> observability correlation model (Lab 4);
criterion 6 -> safety and red-team follow-through plan (Lab 5).
