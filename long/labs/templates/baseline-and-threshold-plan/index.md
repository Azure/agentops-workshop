---
title: "Template: Baseline and threshold plan"
layout: default
nav_exclude: true
---

# Baseline and threshold plan

Produced in [Lab 2]({{ '/long/labs/lab-02-evaluation/' | relative_url }}). Defines what
"good enough to ship" means numerically, and which version is the baseline to compare
against.

```markdown
# Baseline and threshold plan

agent_id:
candidate_version:
baseline_version:
baseline_results:   # e.g. .agentops/baseline/results.json

## Thresholds

| Metric | Threshold | Hard gate? | Rationale |
|---|---|---|---|
| Intent resolution | >= 4.0 | yes |  |
| Task adherence | >= 4.0 | yes |  |
| Tool call accuracy | >= 0.90 | yes |  |
| Groundedness | >= 4.0 | yes |  |
| Content safety violations | == 0 | yes |  |
| p95 latency | <= ___ ms | no |  |
| Cost per request | <= $___ | no |  |

## Baseline comparison rule

- A candidate may not regress any hard-gate metric below its threshold.
- A candidate may not drop more than ___ points vs baseline on any quality metric.
- Latency / cost regressions above ___% require owner sign-off.

## Accelerator wiring

- Capture the first good run as baseline:
  `Copy-Item .agentops/results/latest/results.json .agentops/baseline/results.json`
- Compare: `agentops eval run --baseline .agentops/baseline/results.json`
- The report grows a `Comparison vs Baseline` section with per-metric deltas.
```

Hard-gate metrics block the CI/CD gate in Lab 3. Soft metrics (latency, cost) become
alerts in Lab 4 rather than hard blocks.
