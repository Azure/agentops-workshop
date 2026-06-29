---
title: "Lab 2: Evaluation Design"
layout: default
parent: Labs
nav_order: 2
---

# Lab 2: Evaluation Design

{: .outcome }
> **Artefacts produced:** [evaluation dataset plan]({{ '/long/labs/templates/evaluation-dataset-plan/' | relative_url }})
> and [baseline and threshold plan]({{ '/long/labs/templates/baseline-and-threshold-plan/' | relative_url }}).

**Pillar:** Evaluate. **Duration:** 75 minutes. **Level:** low-code.

## Objective

Build the release signal for your agent: a small golden dataset, the evaluators that run
against it, numeric thresholds, and a baseline comparison. By the end you can answer:
*has this version regressed, and against what?*

## Why evaluation is the release signal

Without a quality signal there is nothing to ship with confidence. Evaluation is not a
one-time score - it is the signal that grows as production teaches you new failure modes.
A few dozen representative cases beat zero cases.

## Prerequisites

- Lab 1 complete (`agentops.yaml` points at your agent; contract written).
- Azure access for evaluation:
  - `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT`
  - `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`
  - `az login`

## Concepts (10 min)

- **Golden dataset:** a small set of cases tied to real user journeys.
- **Foundry evaluators:** quality (intent resolution, task adherence, relevance,
  coherence), groundedness, agent-specific (tool call accuracy), and content safety.
- **Thresholds:** the numeric bar each metric must clear to ship.
- **Baseline comparison:** the candidate is measured against the last good version, not
  just against an absolute bar.
- **Living dataset:** reviewed production traces become future regression rows (the loop
  closed in Labs 4 and 6).

## Steps

### Step 1 - Map user journeys to cases (15 min)

Open the [evaluation dataset plan template]({{ '/long/labs/templates/evaluation-dataset-plan/' | relative_url }}).
List the two or three user journeys that matter most for your agent. For each, write a
handful of representative cases (input + expected behavior). Aim for 20-40 cases total -
real and small beats large and synthetic.

### Step 2 - Check eval readiness (10 min)

```text
agentops eval analyze
```

This checks that your dataset, config, and Foundry connection are ready. Fix anything it
flags (missing endpoint, empty dataset, unmapped evaluator) before running.

### Step 3 - Run the first evaluation (15 min)

```text
agentops eval run
```

Outputs land in `.agentops/results/latest/`:

- `results.json` - machine-readable, stable schema.
- `report.md` - human-readable, PR-friendly.

Open `report.md` and read the per-evaluator scores. Decide which metrics are hard gates
(quality, safety) and which are soft signals (latency, cost).

### Step 4 - Capture a baseline (10 min)

Capture this first good run as the baseline:

```text
New-Item -ItemType Directory -Force .agentops/baseline | Out-Null
Copy-Item .agentops/results/latest/results.json .agentops/baseline/results.json
```

### Step 5 - Make a change and compare (15 min)

Publish a new agent version with a small prompt change (for example, a paraphrased
instruction). Update `agentops.yaml` to the new `name:version` and compare:

```text
agentops eval run --baseline .agentops/baseline/results.json
```

The report grows a `Comparison vs Baseline` section with per-metric deltas. Fill in the
[baseline and threshold plan template]({{ '/long/labs/templates/baseline-and-threshold-plan/' | relative_url }})
with your thresholds and the comparison rule (no hard-gate metric below threshold; no
quality drop greater than your chosen delta).

### Step 6 - Note production-correlation needs (10 min)

In the dataset plan, mark which cases need production correlation. Lab 4 wires those
traces back so real failures can become new rows.

## Artefacts

1. **Evaluation dataset plan** - journeys, cases, evaluators, pass criteria.
2. **Baseline and threshold plan** - thresholds, baseline version, comparison rule.

## Observability metadata captured

- `eval_run_id` for the run that produces the shipping evidence.
- Dataset name and version, so a production trace can be matched to the eval that covered
  (or missed) it.

## Time budget

| Step | Minutes |
|---|---:|
| Concepts | 10 |
| Map journeys to cases | 15 |
| Eval readiness | 10 |
| First evaluation | 15 |
| Capture baseline | 10 |
| Change and compare | 15 |

(Steps overlap; total ~75 min with facilitation.)

## Facilitator tips

- Push attendees away from hundreds of synthetic cases. Twenty real ones are worth more.
- If `agentops eval run` is slow or quota-limited, run a reduced dataset and discuss the
  full one - the learning is in the threshold and baseline design, not the wait.
- Make the failed comparison the highlight: a visible regression delta is the whole point.

## Discussion prompts

- Which metric, if it regressed silently, would hurt your users most?
- What is your baseline today - is there even a "last good version" recorded anywhere?
- Which production failure would you most want to turn into an eval row?

## References

- [Evaluation approach in Foundry](https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai)
- [Agent evaluators](https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators)
- [AgentOps Accelerator](https://github.com/Azure/agentops) - `agentops eval analyze | run | promote-traces`.
