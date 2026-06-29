---
title: "Lab 3: Release Gates and Evidence"
layout: default
parent: Labs
nav_order: 3
---

# Lab 3: Release Gates and Evidence

{: .outcome }
> **Artefacts produced:** [CI/CD gate plan]({{ '/long/labs/templates/cicd-gate-plan/' | relative_url }})
> and [readiness evidence package]({{ '/long/labs/templates/readiness-evidence-package/' | relative_url }}).

**Pillar:** Ship. **Duration:** 60 minutes. **Level:** low-code / full-code.

## Objective

Turn the evaluation signal from Lab 2 into enforcement: PR and deployment gates that block
regressions, and a reviewable readiness evidence package behind a gated approval. By the
end you can answer: *what stops a bad version from reaching users, and where is the proof?*

## Why gates matter

Signals without enforcement are just reports nobody reads. The strongest moment in
AgentOps is a failed gate - if the prompt regresses, the pipeline stops before users
experience it. Every gate produces an artefact: an eval report, a readiness report,
release evidence.

## Prerequisites

- Labs 1 and 2 complete (contract, dataset, thresholds, baseline).
- A GitHub repository with Actions enabled (or Azure DevOps).
- AgentOps Accelerator installed.

## Concepts (10 min)

- **PR gate:** blocks bad prompts before merge.
- **Deploy gate:** blocks bad versions before they reach the next environment.
- **Environment promotion:** sandbox -> dev -> qa -> prod, with checks getting stricter
  per environment. Evidence is locked at qa; prod runs smoke tests plus blue-green /
  canary, no re-eval.
- **Readiness evidence:** the single record a human reviews to approve a release.

## Steps

### Step 1 - Recommend a CI/CD shape (10 min)

```text
agentops workflow analyze
```

This inspects your repo and config and recommends where gates belong. Read the
recommendation and decide which gates you need (PR gate is mandatory; deploy gates depend
on your environments).

### Step 2 - Generate the workflow (10 min)

```text
agentops workflow generate
```

This scaffolds the CI/CD workflow files (for GitHub Actions, under `.github/workflows/`).
Open them and confirm the PR gate runs `agentops eval run --baseline ...` and fails the
job when a hard-gate metric drops below threshold.

Fill in the [CI/CD gate plan template]({{ '/long/labs/templates/cicd-gate-plan/' | relative_url }})
with each gate, its trigger, its checks, and what it blocks on.

### Step 3 - Force a failed gate (15 min)

Open a pull request that intentionally regresses the agent (for example, a prompt that
paraphrases instead of answering exactly). Watch the PR gate run, fail, and comment the
eval report on the PR.

This is the lesson: the gate caught the regression before merge. Capture the workflow run
link for the evidence package.

### Step 4 - Produce the readiness evidence package (15 min)

```text
agentops doctor --evidence-pack
```

This runs readiness checks and writes `evidence.json` and `evidence.md` into
`.agentops/release/latest/`. Open the [readiness evidence package template]({{ '/long/labs/templates/readiness-evidence-package/' | relative_url }})
and map the generated evidence into its eight sections: target/version, evaluation, gate
result, observability, safety, known risks, owner, next improvements.

Leave observability and safety partial for now - Labs 4 and 5 complete them. The package
is what the qa -> prod gated approval reviews.

### Step 5 - Tie evidence back to the contract (10 min)

Return to your release-readiness contract (Lab 1). Mark criteria 4 (gate blocks
regressions) and 7 (evidence is reviewable) with links to the workflow run and the
evidence package.

## Artefacts

1. **CI/CD gate plan** - gates, triggers, promotion rules.
2. **Readiness evidence package** - the reviewable release record.

## Observability metadata captured

- `release_id` - the gate / release decision identifier.
- Workflow run link and gate result, attached to the evidence package so a production
  trace can be traced back to the release that shipped it.

## Time budget

| Step | Minutes |
|---|---:|
| Concepts | 10 |
| Workflow analyze | 10 |
| Workflow generate | 10 |
| Force a failed gate | 15 |
| Evidence package | 15 |

## Facilitator tips

- The failed-gate moment is the highlight of the morning - make sure everyone sees a red
  check on a PR, not just a passing one.
- If an attendee cannot run Actions in their tenant, walk the generated workflow file and
  the `evidence.md` output and discuss; the artefact still gets filled in.
- Stress that prod does not re-evaluate - the evidence is locked at qa. This surprises
  teams used to re-running everything everywhere.

## Discussion prompts

- Where in your current pipeline could a regressed prompt reach users today?
- Who signs the gated approval, and what do they actually look at?
- Is your release evidence reproducible six months later during an audit?

## References

- [Agent development lifecycle](https://learn.microsoft.com/azure/ai-foundry/agents/concepts/development-lifecycle)
- [AgentOps Accelerator](https://github.com/Azure/agentops) - `agentops workflow analyze | generate`, `agentops doctor --evidence-pack`.
