---
title: Run of Show
layout: default
parent: 1-Hour Session
nav_order: 2
---

# 1-Hour Run of Show

## Presenter goal

Deliver a crisp AgentOps story that feels practical and production-oriented, with a strong observability section and a demo that proves the operating loop.

## Minute-by-minute guide

| Time | Presenter action | Transition line |
|---:|---|---|
| 0:00-0:02 | Set the promise and audience expectation. | "The question today is not can we build an agent. It is can we safely operate and release one." |
| 0:02-0:06 | Explain the production gap. | "Once the agent becomes part of a workflow, confidence needs evidence." |
| 0:06-0:10 | Show why agents increase complexity. | "More autonomy means more places where behavior can drift." |
| 0:10-0:15 | Introduce the AgentOps loop. | "This loop gives teams a practical way to manage that drift." |
| 0:15-0:19 | Show the maturity model. | "Most teams sit between Initial and Defined. Start by moving one agent up." |
| 0:19-0:24 | Position Foundry as control plane. | "Foundry is the control plane. AgentOps connects those signals to release decisions." |
| 0:24-0:28 | Walk through the readiness checklist. | "These items turn 'I think it works' into 'we have evidence for this release.'" |
| 0:28-0:33 | Explain evaluation strategy. | "Evaluation is the release signal that grows as production teaches you new failure modes." |
| 0:33-0:37 | Cover red teaming and AI safety. | "Quality says 'is the answer good?' Red teaming says 'can someone make this agent misbehave?'" |
| 0:37-0:42 | Show CI/CD gates. | "The strongest moment is a failed gate before users see the regression." |
| 0:42-0:46 | Deepen observability. | "For agents, the unit of understanding is the trace, not the endpoint." |
| 0:46-0:50 | Connect telemetry to action. | "The end state is action: fix the issue, update the eval set, prevent the same failure from reaching production." |
| 0:50-0:52 | Open Day-2 operations. | "AgentOps is not done at release. Production keeps teaching us." |
| 0:52-0:56 | Walk through the incident runbook. | "Containment first, evidence-backed fix second." |
| 0:56-0:58 | Show model lifecycle and canary. | "Treat every model change as a release candidate, not a config flip." |
| 0:58-1:00 | Close with the 30-day start. | "Start with one agent, one eval set, one release gate, and one observability view." |

## Observability delivery notes

Do not compress observability into "monitoring." Use the word **observability** deliberately and explain what must be observable for agents:

- What the user asked.
- What the agent planned.
- Which model calls were made.
- Which tools were invoked.
- Which retrieval sources were used.
- Which safety events fired.
- Which version and release produced the trace.
- Whether latency, cost, quality, or safety changed after release.
- Which traces should become future eval rows.

## Optional demo recording

The embedded demo block was removed during the 2026-05-26 rebalancing. The deck stands on its own conceptually.

A backup video may still be recorded as an optional supplementary artifact. If the video is played in a specific delivery, insert it between the observability block (0:46-0:50) and the Day-2 opener (0:50-0:52). If the video is shown, plan to drop or compress the maturity slide (0:15-0:19) and the four-quadrant Day-2 opener (0:50-0:52) to stay within the hour.

If a customer remembers one thing, it should be this: observability is how production behavior becomes the next evaluation set.
