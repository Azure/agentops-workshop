---
title: "Template: CI/CD gate plan"
layout: default
nav_exclude: true
---

# CI/CD gate plan

Produced in [Lab 3]({{ '/long/labs/lab-03-release-gates/' | relative_url }}). Defines
where evaluation evidence is enforced in pull requests and deployments.

```markdown
# CI/CD gate plan

agent_id:
agent_version:
repo:
ci_system: GitHub Actions / Azure DevOps

## Gates

| Gate | Trigger | Checks | Blocks on | Evidence artefact |
|---|---|---|---|---|
| PR gate | pull_request | eval run vs baseline, safety eval | any hard-gate metric below threshold | report.md, evidence.md |
| Deploy-to-qa gate | merge to main | integration tests, red-team scan | red-team high finding | evidence.json |
| Deploy-to-prod gate | manual approval | smoke tests, human sign-off | missing release evidence | release evidence package |

## Environment promotion

sandbox -> dev -> qa -> prod

| Environment | Re-evaluate? | Added checks |
|---|---|---|
| dev | yes | manual tests, quality + safety evals |
| qa | yes | integration tests, red team |
| prod | no (evidence locked at qa) | smoke tests, blue-green / canary |

## Accelerator wiring

- `agentops workflow analyze` recommends the CI/CD shape.
- `agentops workflow generate` scaffolds the workflow files.
- `agentops doctor --evidence-pack` produces the readiness evidence consumed by the gate.

## Failure handling

- On PR gate failure: comment report.md on the PR, block merge.
- On deploy gate failure: stop promotion, notify owner, keep last good version.
```

The gate consumes the thresholds from the baseline plan (Lab 2) and emits the readiness
evidence package below.
