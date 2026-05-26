---
title: Demo Video Plan
layout: default
parent: 1-Hour Session
nav_order: 5
---

# Demo Video Plan

## Purpose

Create an 8-10 minute edited video that makes the AgentOps operating model tangible.

The video should show a production-readiness flow, not a tool installation walkthrough. AgentOps Toolkit components can be used in the recording where useful, but the story should remain about AgentOps practices.

## Source of truth

Use:

`C:\Users\paulolacerda\workspace\agentops\docs\tutorial-end-to-end.md`

## Demo storyline

| Time | Segment | Show | Message |
|---:|---|---|---|
| 0:00-0:45 | Setup | Foundry project and Travel Agent target | The agent exists; the question is whether this version is safe to release. |
| 0:45-2:00 | Release contract | Eval dataset, target reference, repo configuration | Production readiness starts with an explicit target, dataset, and release criteria. |
| 2:00-3:00 | Eval path | Runner analysis and first clean eval | The team gets a baseline signal. |
| 3:00-4:45 | Regression | Bad prompt version or regressed endpoint; failed gate | The release gate catches a real behavior regression before users see it. |
| 4:45-5:45 | Fix | Restore behavior; rerun; gate passes | The same evidence path validates the fix. |
| 5:45-6:45 | CI/CD | PR, dev, QA, prod, watchdog workflow pattern | AgentOps turns evaluation into release discipline. |
| 6:45-8:15 | Observability checkpoint | Foundry/Azure Monitor traces, telemetry, readiness report, release evidence | Operations signals are connected to release review and future evals. |
| 8:15-9:30 | Close | Local command center with eval status, readiness findings, evidence, Foundry links, next actions | The team can answer "can we ship, and where is the proof?" |

## Required beats

1. Show the Foundry control plane first.
2. State the release-readiness question.
3. Show a small eval dataset.
4. Show the intentional regression.
5. Show the failed gate.
6. Show trace or telemetry context for the failure.
7. Show the fix and passing gate.
8. Show release evidence.
9. End with Foundry/Azure Monitor links and next actions.

## Observability shots to capture

- Trace list or trace detail for the evaluated agent interaction.
- Model call latency and token/cost signal, if available.
- Tool call or retrieval event that helps explain behavior.
- Release/version metadata associated with the run.
- Dashboard or query showing health, errors, latency, safety events, or usage.
- A final evidence view connecting eval results, readiness checks, and telemetry links.

## What to avoid

- Do not spend time on package installation.
- Do not show every wizard prompt.
- Do not walk YAML line by line.
- Do not present AgentOps Toolkit as the topic of the video.
- Do not claim AgentOps replaces Foundry observability, red teaming, or governance.

## Voiceover close

"The point is not the commands. The point is the operating loop: evaluate the agent, gate the release, observe production, diagnose readiness gaps, ship with evidence, and feed what we learn back into the next evaluation set."
