---
title: "Lab 6: Incident Response and Continuous Improvement"
layout: default
parent: Labs
nav_order: 6
---

# Lab 6: Incident Response and Continuous Improvement

{: .outcome }
> **Artefact produced:** [incident response and continuous improvement plan]({{ '/long/labs/templates/incident-and-improvement-plan/' | relative_url }}).

**Pillar:** Operate. **Duration:** 35 minutes. **Level:** no-code / low-code.

## Objective

Define how production signals become contained incidents, evidence-backed fixes, and -
crucially - future evaluation coverage. By the end you can answer: *when something goes
wrong, how do we respond, and how do we make sure it never happens the same way twice?*

## Why this closes the loop

Shipping is not the finish line; it is where the real operational work begins. The
four-pillar loop closes when Operate feeds the next Evaluate and Ship cycle. Every closed
incident should leave behind at least one new eval row.

## Prerequisites

- Labs 1-4 complete (traces correlated; alerts mapped to actions).
- The dashboard and alert plan from Lab 4.

## Concepts (8 min)

- **Severity model:** S1 critical (safety/data leak) through S4 low (single-metric drift),
  each with a defined first action.
- **Triage flow:** Detect -> Correlate trace -> Identify version -> Contain -> Analyze ->
  Fix -> Re-evaluate -> Close with evidence. Containment first, debugging second.
- **Continuous improvement:** reviewed production traces are promoted into eval rows;
  thresholds, prompts, tools, and policies are adjusted from what production taught you.

## Steps

### Step 1 - Define the severity model (10 min)

Open the [incident response and continuous improvement plan template]({{ '/long/labs/templates/incident-and-improvement-plan/' | relative_url }}).
Fill in the severity table for your agent with concrete examples and a first action per
severity. Tie each alert from Lab 4 to a severity so on-call knows how to react.

### Step 2 - Walk one incident end to end (12 min)

Take a real or sample failure and walk the triage flow:

1. **Detect** - which alert or signal fired.
2. **Correlate trace** - find the trace by `trace_id` (Lab 4).
3. **Identify version** - read `agent_version` / `release_id` off the trace.
4. **Contain** - rollback, version pin, or rate-limit per severity.
5. **Analyze** - which span broke and why.
6. **Fix** - prompt, tool, policy, or model change.
7. **Re-evaluate** - run the eval gate on the fix.
8. **Close with evidence** - record root cause and the new eval row.

Log it in the incident log table.

### Step 3 - Promote the trace into eval coverage (8 min)

```text
agentops eval promote-traces --source <trace-file> --apply
```

Confirm the new row is in the dataset and would be caught by the PR gate (Lab 3). Fill in
the continuous-improvement section: traces promoted this cycle, thresholds adjusted, next
coverage gap to close.

### Step 4 - Connect to model lifecycle (5 min)

Note in the plan how a model change (deprecation, new version, cost pressure) is handled:
treat it as a release candidate that goes back through Evaluate and Ship with the same
gates and evidence - not a config flip.

## Artefact

**Incident response and continuous improvement plan** - severity model, triage flow,
incident log, and the improvement loop.

## Observability metadata captured

- Incident records linked to `trace_id`, `agent_version`, and `release_id`.
- New eval rows tagged with the source trace so coverage is auditable.

## Time budget

| Step | Minutes |
|---|---:|
| Concepts | 8 |
| Severity model | 10 |
| Walk one incident | 12 |
| Promote trace | 8 |
| Model lifecycle | 5 |

## Facilitator tips

- This lab is short - keep it to one incident walked completely rather than several
  half-walked.
- The single most valuable habit to instill: an incident is not closed until it has a test.
- Reuse the trace promoted in Lab 4 if time is tight; the point is the repeatable loop.

## Discussion prompts

- What is your current mean time to identify the version behind a production failure?
- Do your postmortems produce test coverage, or just action items that decay?
- How would you handle your most-depended-on model being deprecated next quarter?

## References

- [AgentOps Accelerator](https://github.com/Azure/agentops) - `agentops eval promote-traces`.
- [Agent development lifecycle](https://learn.microsoft.com/azure/ai-foundry/agents/concepts/development-lifecycle)
