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
| 0:00-0:03 | Set the promise and audience expectation. | "The question today is not can we build an agent. It is can we safely operate and release one." |
| 0:03-0:08 | Explain the production gap. | "Once the agent becomes part of a workflow, confidence needs evidence." |
| 0:08-0:13 | Show why agents increase complexity. | "More autonomy means more places where behavior can drift." |
| 0:13-0:18 | Introduce the AgentOps loop. | "This loop gives teams a practical way to manage that drift." |
| 0:18-0:24 | Cover lifecycle and maturity. | "Most teams do not need a giant program first. They need one production-candidate agent with release criteria." |
| 0:24-0:30 | Show Foundry, Azure Monitor, repo, and CI/CD roles. | "Foundry is the control plane. AgentOps connects those signals to release decisions." |
| 0:30-0:36 | Explain evaluation and gates. | "The most important demo moment is the gate failing before users see the regression." |
| 0:36-0:44 | Deepen observability. | "Now we need to operate after release, and for agents that means traces, not just CPU charts." |
| 0:44-0:53 | Play or narrate the demo video. | "Watch for the evidence chain: target, eval, gate, trace, readiness report." |
| 0:53-0:57 | Summarize proof points. | "The demo is not about commands. It is about the operating model." |
| 0:57-1:00 | Close with next steps. | "Start with one agent, one eval set, one release gate, and one observability view." |

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

## Demo handoff

Before the video:

> "The video uses tooling only to make the operating model visible. The important part is the evidence path: evaluate, gate, observe, diagnose, ship, improve."

After the video:

> "If a customer remembers one thing, it should be this: observability is how production behavior becomes the next evaluation set."
