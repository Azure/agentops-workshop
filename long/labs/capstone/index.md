---
title: "Capstone: Production-Readiness Review"
layout: default
parent: Labs
nav_order: 7
---

# Capstone: Production-Readiness Review

{: .outcome }
> **Artefact produced:** a composed release-readiness review and a go / no-go decision,
> built from all ten lab artefacts.

**Format:** facilitated review and discussion. **Duration:** 30 minutes.

## Objective

Compose every artefact from the day into one release-readiness narrative for your
production-candidate agent, and make a go / no-go decision with evidence. This is the
moment the four pillars become one story.

## The capstone question

> If this agent produces a bad answer in production tomorrow, can we find the trace,
> understand what happened, identify the shipped version, route it to the right owner, and
> prevent the same failure in the next release?

If you can answer yes with evidence, the agent is ready. If not, the gaps are your 30-day
plan.

## Prerequisites

All ten artefacts at least partially filled in:

| Pillar | Artefacts |
|---|---|
| Foundations | agent target inventory, release-readiness contract |
| Evaluate | evaluation dataset plan, baseline and threshold plan |
| Ship | CI/CD gate plan, readiness evidence package |
| Observe | observability correlation model, dashboard and alert plan |
| Operate | safety and red-team follow-through plan, incident and improvement plan |

## Steps

### Step 1 - Assemble the evidence (10 min)

Open the readiness evidence package (Lab 3) and confirm each of its eight sections now
links to a real artefact:

1. Target and version - from the inventory.
2. Evaluation evidence - `eval_run_id`, dataset, baseline comparison.
3. Gate result - workflow run, `release_id`.
4. Observability - App Insights link, dashboards wired, correlation keys present.
5. Safety and red team - findings with follow-through status.
6. Known risks - with mitigations and owners.
7. Owner and escalation - from the inventory and RACI map.
8. Next eval improvements - rows queued from promoted traces.

### Step 2 - Walk a single trace end to end (10 min)

Pick one trace and demonstrate the thread: from `trace_id` to `agent_version` to
`eval_run_id` to `release_id` to `owner`. If any link is missing, that is a concrete gap,
not an abstract one. This is the proof that the observability thread is real, not
aspirational.

### Step 3 - Make the decision (5 min)

Walk the eight criteria of the release-readiness contract. For each, mark met / not met
with its evidence link. Record the go / no-go decision and the approver.

### Step 4 - Write the 30-day plan (5 min)

For every "not met" criterion, write one concrete action with an owner and a date. This is
what the attendee leaves with: not a finished system, but a proven pattern on one agent
and a short list of the next moves.

## What "done" looks like

- The readiness evidence package has no empty sections.
- One trace has been walked from interaction to owner without a missing link.
- The contract has a recorded decision.
- The 30-day plan has an owner and a date per open item.

## Facilitator tips

- Have one or two attendees present their thread to the room - peer review surfaces gaps
  faster than self-review.
- Resist the urge to "pass" everyone. A no-go with a clear 30-day plan is a successful
  outcome; a hand-waved go is not.
- Tie back to the maturity model from the kickoff: most teams move one level on one agent,
  and that is the win.

## Discussion prompts

- Which pillar was strongest for your agent, and which was the real gap?
- What is the single most important item on your 30-day plan?
- How would you replicate this pattern on your next agent without re-litigating every
  decision?

## References

- [Lab roadmap]({{ '/long/lab-roadmap' | relative_url }})
- [Observability strategy]({{ '/long/observability-strategy' | relative_url }})
- [AgentOps Accelerator](https://github.com/Azure/agentops)
