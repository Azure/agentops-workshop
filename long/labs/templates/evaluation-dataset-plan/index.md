---
title: "Template: Evaluation dataset plan"
layout: default
nav_exclude: true
---

# Evaluation dataset plan

Produced in [Lab 2]({{ '/long/labs/lab-02-evaluation/' | relative_url }}). Defines the
golden dataset and which evaluators run against it. Keep the dataset small and real - a
few dozen representative cases beat zero cases.

```markdown
# Evaluation dataset plan

agent_id:
agent_version:
owner:
dataset_name:
dataset_location:   # e.g. .agentops/data/eval.jsonl

## User journeys covered

| Journey | Why it matters | Example case count |
|---|---|---|
|  |  |  |

## Evaluators

| Evaluator | Type | What it measures | Pass criterion |
|---|---|---|---|
| Intent resolution | quality | Did the agent address the request? | >= 4/5 |
| Task adherence | quality | Did it follow instructions? | >= 4/5 |
| Tool call accuracy | agent | Correct tool, correct args | >= 0.9 |
| Groundedness | quality | Answer supported by sources | >= 4/5 |
| Relevance / coherence | quality | Useful, consistent answer | >= 4/5 |
| Content safety | safety | Harmful content blocked | 0 violations |

## Regression candidates from production

| Source trace ID | Failure mode | Added as case? |
|---|---|---|

## Accelerator wiring

- `agentops eval analyze` confirms readiness.
- `agentops eval run` produces `results.json` and `report.md`.
- Dataset rows live in the path referenced by `agentops.yaml`.
```

The dataset is a living artefact: every reviewed production trace from Lab 4 and Lab 6
can become a new row here. List which cases need production correlation so Lab 4 can wire
the trace-to-eval feedback loop.
