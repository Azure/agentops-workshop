---
title: "Template: Incident response and continuous improvement plan"
layout: default
nav_exclude: true
---

# Incident response and continuous improvement plan

Produced in [Lab 6]({{ '/long/labs/lab-06-continuous-improvement/' | relative_url }}).
Defines how production signals become contained incidents, evidence-backed fixes, and
future evaluation coverage.

```markdown
# Incident response and continuous improvement plan

agent_id:
owner:
on_call_path:

## Severity model

| Severity | Example | First action |
|---|---|---|
| S1 Critical | Safety event or data leak in production | Stop gate, rollback to last good version |
| S2 High | Quality or grounding regression after deploy | Planned rollback or version pin |
| S3 Medium | Latency degradation or cost spike | Rate-limit, investigate, then act |
| S4 Low | Drift indicator on a single metric | Schedule analysis in next eval cycle |

## Triage flow

Detect -> Correlate trace -> Identify version -> Contain -> Analyze -> Fix ->
Re-evaluate -> Close with evidence

## Incident log

| Incident ID | Severity | Trace ID | Version | Root cause | Fix | New eval row? | Closed |
|---|---|---|---|---|---|---|---|

## Continuous improvement loop

- Reviewed production traces promoted to eval rows this cycle:
- Thresholds adjusted:
- Prompts / tools / policies changed:
- Next eval coverage gap to close:

## Accelerator wiring

- `agentops eval promote-traces --source <file> --apply` promotes reviewed traces into
  the eval dataset.
- The new rows feed the PR gate (Lab 3) so the same failure is caught next time.
```

This is where the four-pillar loop closes: Operate feeds the next Evaluate and Ship cycle.
Every closed incident should leave behind at least one new eval row.
