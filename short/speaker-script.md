---
title: Speaker Script
layout: default
parent: Short Workshop
nav_order: 6
---

# Short Workshop Speaker Script (Dual-Voice)

Dual-voice narration for the AgentOps deck. One primary speaker per slide, with an even split across the session.

## How to use this script

- **One primary speaker per slide.** Speaker turns are marked `**SP1:**` and `**SP2:**`. The markers are parsed by `prep/tools/render_speech.py` and mapped to two distinct Azure Neural voices.
- **Target duration:** ~50 minutes of narration.
- **Pace:** ~145 wpm, measured and conversational.
- **Italics** indicate words to land hard.
- Section dividers are short transitions spoken by whichever speaker owns the next content slides.
- The original single-voice version of this script is preserved at `prep/short/speaker-script-single.md` for reference.

## Speaker assignment

| Section | Slides | Speaker |
|---------|--------|---------|
| Title + Agenda | 1-2 | SP1, SP2 |
| Foundations | 3-5 (gap, building blocks) | SP1 |
| Foundations | 6-8 (Foundry, checklist, maturity) | SP2 |
| Foundations | 9 (operating model) | SP1 |
| Evaluation | 10-12 | SP2 |
| CI/CD | 13-14 | SP1 |
| Observability | 15-17 | SP2 |
| Day-2 Operations | 18-21 | SP1 |
| Adoption | 22-23 | SP2 |

---

## Slide 1 - Title: AgentOps - From Agent Prototype to Production

**SP1:** Welcome. In the next hour we're going to talk about the central question for teams building AI agents today. Not how to build the first demo - we already know how to do that. The question now is harder. *Can we safely ship this agent? And where is the evidence?* That's what this session is about. The operating model we call AgentOps. It's how we take the production engineering discipline we already trust for traditional software and apply it to AI agents, where behavior is probabilistic, tools have side effects, and yesterday's safe answer might not be safe tomorrow.

---

## Slide 2 - Agenda

**SP2:** We have six blocks for one hour. First, AgentOps Foundations - why AI operations need a new discipline, what the operating loop looks like, and where teams really sit today. Second, Evaluation - the release signal that tells us whether a new version is actually better, or just different. Third, CI/CD - the gates that turn that evaluation signal into a release decision. Fourth, Observability - once the agent is live, how do we see what it's doing and close the loop back to evaluation? Fifth, Day-2 Operations - incident response and model lifecycle. And we'll close on Adoption - how to start, on Monday morning, with one agent.

---

## Slide 3 - Section: AgentOps Foundations

**SP1:** Let's start with foundations. Before we talk about evaluators, pipelines, or dashboards, we want to spend a few minutes on why we need any of this. Why traditional DevOps isn't enough for agents. What changes when an agent can call tools, hold memory, and make decisions on its own.

---

## Slide 4 - The production gap

**SP1:** Here's the contrast. On the left, prototype works. On the right, production needs proof. A prototype is one happy-path demo. The product owner watched it answer three questions correctly and said yes, ship this. Production needs repeatable evaluation across dozens or hundreds of cases. A prototype gets a manual quality check. Production needs release evidence - something you can show to a security reviewer, a compliance officer, that says this version was tested against these criteria and it passed. A prototype is a single-version snapshot. Production has versioned models, versioned prompts, versioned tool definitions. All three change. A new model ships. The prompt gets edited. A tool's API changes. Each one shifts behavior. We have to know what we shipped, and when. And the killer one - "it looked good last week." That's the most dangerous sentence in agent development. The agent is probabilistic. The model can drift. The data behind retrieval can drift. User behavior changes. Yesterday's confident answer becomes tomorrow's hallucination. *The bottleneck moved.* It used to be: can we build the first demo? Now it is: can we prove that the next version is safe to release? Without the operating model, every change is a fire drill.

---

## Slide 5 - Building blocks of a production agent

**SP1:** Why does this need a new operating discipline? Why can't we just use the DevOps practices we already have? The answer is in this ladder. As we move up, every rung adds new operational surface. At the bottom: simple prompts. We send a question, we get an answer. The tradeoffs are quality and cost. Manageable. Next rung: RAG. Now we think about grounding, retrieval quality, data freshness, and permissions. Did the user have access to the data that informed the answer? Next: tool-using agents. The model is calling functions, planning steps, each with side effects and auth boundaries. The blast radius of a wrong action gets much bigger. Then single agents with memory. Multi-step traces become the unit of behavior. A bug might emerge on the seventh turn because of something remembered from the third. At the top: multi-agent systems. Orchestrators coordinating sub-agents. Emergent behavior. The point is that even simple agents put you several rungs above where DevOps practices were designed to operate. Multi-step plans and tool calls multiply the failure surface. Snapshot testing is just not enough. We need a different kind of evidence.

---

## Slide 6 - Microsoft Foundry is the control plane

**SP2:** Let's clarify positioning, because this comes up in every conversation. Where does Foundry fit, and where does AgentOps fit on top? Foundry is the control plane. Three layers. The surfaces layer is how teams interact - the portal, the SDK, Azure CLI and REST APIs, and GitHub Actions. Same control plane, different ways in. The capabilities layer is what Foundry does for agents. It manages agents and versions. It has built-in evaluators for quality, groundedness, fluency, coherence. It has agent-specific evaluators - intent resolution, task adherence, tool call accuracy. It hosts the AI Red Teaming Agent backed by PyRIT. It supports OpenTelemetry tracing natively. And it integrates with Content Safety for runtime policy checks. The runtime layer is where the agent executes - Azure AI projects, model deployments, tool and MCP servers, Application Insights and Log Analytics. *AgentOps is not a replacement for any of this.* It's the operating model that connects Foundry signals to release decisions and Day-2 action. Foundry is the source of truth. AgentOps is what we do with that truth, to ship safely, every time.

---

## Slide 7 - Production readiness checklist

**SP2:** This is the slide we want you to take a picture of. The production readiness checklist. The release evidence contract for any agent you're about to put in front of users. Seven items. One: target and version are explicit. We know exactly which agent, which version, which prompt, which tools we're releasing. Two: an eval dataset exists and thresholds are agreed. Minimum quality, groundedness, intent resolution. Below those, the release stops. Three: the CI/CD gate actively blocks regressions. Not advisory. If eval drops, the pipeline fails. Four: telemetry and traces are wired. Application Insights collecting, OpenTelemetry spans flowing, trace IDs end to end. Five: safety and red-team findings are tracked. The Red Teaming Agent has run at least once before release. Six: release evidence is reviewable. Not in someone's head. In an artifact attached to the release. Seven: owners know what to do when signals fail. There's an on-call, a runbook, a triage flow. It turns "I think it works" into "we have evidence for this release." Every section that follows fills out one or more items on this checklist.

---

## Slide 8 - Maturity model

**SP2:** Quick self-assessment. Where is your team right now? Four levels, and we'd bet almost everyone is somewhere between the first two. Level one - Initial. Ad hoc demos. Manual evaluation. Someone types five questions, looks at the answers, says yeah this seems fine. No gates, logs scattered. If you ask the team to explain a regression from last week, they can't. Level two - Defined. Prompts are versioned. Agents are versioned. There's a pre-prod eval dataset. CI builds artifacts. The team can answer: what's the current version, what did we test it against? This is the minimum bar for any agent going in front of real users. Level three - Managed. Quality and safety gates in CI. Continuous evaluation on production. Runbooks and SLOs. This is where most enterprise customers want to be within twelve months. Level four - Optimised. Drift and cost guardrails. Canary plus auto-rollback. The feedback flywheel is real - every reviewed production trace becomes a new eval row within hours. *Don't try to boil the ocean.* Pick one production-candidate agent. Move it up one level. Build the pattern. Then scale it. The question now is: how do we produce this evidence repeatably? That's what the operating model gives us.

---

## Slide 9 - AgentOps operating model

**SP1:** This is the operating model itself. The AgentOps loop. Six steps. They're the heart of the session. Everything we talk about for the next forty-five minutes is one of these six steps. First: *evaluate.* We have a curated golden dataset of representative user journeys. We run the current and candidate versions against it. We measure quality, groundedness, latency, cost, intent resolution, tool call accuracy. We don't ship blind. Second: *gate.* The evaluation result becomes a gate in CI/CD. If quality drops below threshold, the pipeline fails. If safety regresses, the pipeline fails. The gate is the strongest moment in the loop - the point at which a bad version stops before users ever see it. Third: *observe.* Once in production, we need traces. The full chain: prompt, plan, model call, tool call, retrieval, safety event, latency, cost, user feedback. We use Foundry observability and Application Insights together. Fourth: *diagnose.* We run evaluators on production samples, compare against baselines, use traces to find root cause. Diagnosis turns telemetry into actionable evidence. Fifth: *ship.* Canary rollout. Five percent first, then fifty, then full. Model, prompt, and tools versioned together so the release artifact is reproducible. Sixth: *improve.* Reviewed traces from production become new rows in the eval dataset. The dataset grows. Next time we run a gate, we test against everything we've learned. People, process, platform. People means the model is owned - there's an on-call, runbooks, reviewers. Process means we follow the loop on every change. Platform means Foundry as the control plane with telemetry, traces, evaluators, and pipelines wired together. The output is *release evidence* and *operational confidence*. Let's start with the first step - Evaluation.

---

## Slide 10 - Section: Evaluation

**SP2:** The first item on that checklist, probably the most important one, is evaluation. The eval dataset, the thresholds, the release signal. That's where we go next.

---

## Slide 11 - Evaluation strategy

**SP2:** Three stages of evaluation across the whole life of the agent. Stage one - base model selection. Before we write the agent, we pick the model with evidence. We test candidates against a representative dataset. We measure cost, latency, and quality on the actual use case. We choose with evidence, not excitement. Stage two - pre-production evaluation. The candidate version runs against a golden dataset with built-in evaluators. We get scores. We compare against the previous version and against absolute thresholds. If we pass, we promote. If we fail, the regression has to be diagnosed before anything ships. The golden dataset does not need to be huge. A few dozen carefully chosen cases tied to real user journeys beats zero cases by an enormous margin. Foundry's built-in evaluators cover quality, groundedness, coherence, fluency. The agent-specific evaluators - intent resolution, task adherence, tool call accuracy - are critical if the agent calls functions or follows multi-step plans. Stage three - post-production monitoring. We keep evaluating. We sample production traces. We run them through the same evaluators. We watch for drift, quality drops, new failure modes. The interesting traces - regressions, weird tool calls, new behavior - become new rows in the golden dataset. *The dataset is alive.* Don't wait for the perfect dataset. Start with twenty cases. Catch your first regression. Add the failing case as row twenty-one. That's how the team starts to trust the gate.

---

## Slide 12 - Red teaming and AI safety

**SP2:** *Quality and safety are different signals.* A quality score tells you whether the answer was coherent, grounded, and useful. It will not tell you whether someone could jailbreak the agent into revealing secrets or trick it into sending a malicious email. Those are different problems, with different test cases, and a different cadence. Foundry ships an AI Red Teaming Agent backed by PyRIT. Instead of ad-hoc adversarial testing every six months, we automate it on a schedule. Four risk categories. First - harmful content. Hate speech, violence, things the agent should refuse no matter how cleverly someone asks. Second - jailbreak. Prompt injection, role hijacking, getting the agent to ignore its system prompt. New techniques come out every month; the Red Teaming Agent maintains a library. Third - hallucination. Ungrounded claims, fake citations. The adversarial framing is different from quality - we're asking can we *trick* the agent into making things up? Fourth - data exfiltration. PII leakage, secrets echoed back, tool abuse. Especially important if the agent has access to internal systems. Cadence: pre-release gate, scheduled weekly, and post-incident. Findings feed straight back into the eval dataset as adversarial rows. A jailbreak that worked once becomes a regression test. Next time, we catch it before users do. Quality says the agent is good. Safety says the agent can't be abused. Both have to pass. Now - how do we enforce these signals? That brings us to CI/CD gates.

---

## Slide 13 - Section: CI/CD for Agentic AI

**SP1:** We have evaluation. We have red teaming. We have a golden dataset. Now we need to turn all of that into a release decision. Pipelines and gates. CI/CD for agentic AI.

---

## Slide 14 - CI/CD gates for agentic AI

**SP1:** The pipeline pattern looks familiar - build, evaluate, gate decision, deploy - but the contents are agent-specific. Build means we package the agent. The model version, prompt template, tool definitions, configuration. All versioned together as a single artifact. If the prompt changes, behavior changes. If the tool definition changes, behavior changes. We need a single thing we can roll forward or roll back. Evaluate is the stage we just covered. The candidate runs against the golden dataset. The Red Teaming Agent runs. The evaluators produce scores. The result is an evidence pack - eval report, red team report, content safety scan, dependency check. Gate decision is the moment of truth. Are scores above thresholds? Did red team find anything new? Is cost within budget? If all yes, the gate passes. If any no, the gate fails. *The strongest moment in the whole pipeline is a failed gate.* That's the moment a bad version was about to reach users and instead it stopped. Three kinds of gates. PR gates - block bad prompts before merge. Fast, lightweight, on every pull request. Deploy gates - block bad versions before the next environment. Full eval suite on every promotion. Watchdogs - scheduled checks against production. Catch drift, tool failures, upstream model changes. Each gate produces an artifact for the audit trail. When compliance asks "how do you know this was safe?" you point to the artifact. GitHub Actions or Azure DevOps Pipelines, Foundry's CLI plugs into either. The mechanism is well understood. What's new is what we're measuring and gating on. Now - what happens after we ship? That's where observability comes in.

---

## Slide 15 - Section: Observability

**SP2:** Pipelines and gates are the release-time part of the loop. But the operating model doesn't stop at release. We need to see what the agent is doing in production. Traces, correlation, and the closed loop.

---

## Slide 16 - Observability for agents is more than monitoring

**SP2:** This distinction matters. Monitoring asks: is the service healthy? Is the endpoint up? Is latency within target? Those questions matter, but they're not enough for an agent. Observability asks a different question. *What did the agent do, and why did it do it?* Not did it respond in 800 milliseconds, but what was the prompt? What tools did it call? What documents did retrieval surface? What safety event fired? What was the chain of decisions? For agents, the unit of understanding is the trace, not the endpoint status. The Foundry observability stack has three pillars. Pillar one - tracing. OpenTelemetry-based spans across the agent's execution. Every model call, tool call, retrieval, safety event. All correlated by trace ID. Native to Foundry, exportable to Application Insights, queryable in Log Analytics. Pillar two - monitoring. The classic signals. Latency, error rate, token throughput, resource health. Still important, just no longer enough on its own. Pillar three - continuous evaluation. The evaluators running on production samples. Quality scores on real conversations. Groundedness checks on actual responses. The eval pipeline is now also a runtime signal. These three stack. Continuous evaluation gives you macro health. Monitoring gives you service health. Tracing gives you the explanation. The required signals: prompt, plan, model call, retrieval, tool call, safety event, latency, cost, user feedback, release version. The required correlation: trace ID, session ID, agent version, deployment, eval run, incident, owner. Without correlation, observability is disconnected dashboards. With it, the same trace answers questions across release, runtime, evaluation, and Day-2. *Correlation turns observability from dashboards into an operating signal.*

---

## Slide 17 - From telemetry to action

**SP2:** This is the connective tissue slide for the whole session. *Telemetry is not the goal. Action is.* Let's walk through it signal by signal. Latency spike - the trace shows a tool call taking ten times longer than baseline. Azure Monitor fires an alert. The on-call looks at the trace, sees the tool timing out, disables it, falls back to a manual path. The agent stays responsive. Tool error rate climbs - thirty percent of calls returning 500s. Disable the tool. The agent gracefully degrades. Users still get value. Safety violation - Content Safety blocks a response containing personal data. The trace is captured, a safety incident opened. The reviewed trace goes into the red team dataset. Next release, that exact attempt is part of the regression suite. Eval score drop - continuous evaluation shows quality on a particular intent dropped from 0.92 to 0.78. Below threshold. The canary pauses. A ticket opens. We diagnose. Cost anomaly - token usage on a tenant tripled overnight. APIM throttles. FinOps gets notified. We figure out if it's legitimate adoption or an attack. Positive feedback - a user gave a thumbs-up on a tricky question. That trace gets sampled into the eval dataset as a positive example. Every signal triggers a concrete operational response. Every response feeds back into the eval set, the gates, or the runbook. *This is how observability funds evaluation. And evaluation funds release confidence.* The closed loop. That's how we keep getting better, release after release.

---

## Slide 18 - Section: Day-2 Operations

**SP1:** The loop runs every day after launch. That's Day-2 operations. Running agents in production. Where most of the actual work lives, long after the launch demo.

---

## Slide 19 - Day-2 operations - four concerns

**SP1:** Day-2 is where most of the operational reality lives. The hard part is not getting the agent to launch. The hard part is keeping it useful, safe, and reliable on day ninety, day one-eighty, day three-sixty-five. Four concerns on the quadrant, and they're interlocking. Reliability and SLOs - availability, latency, error rate budgets. When a downstream tool fails, does the agent gracefully degrade or fall over? Tool dependency mapping matters. Agents often have ten or fifteen tool dependencies, each a potential failure mode. Incident response - severity classes, runbooks, on-call rotations. When an agent misbehaves, we need a sequence, not improvisation. *Containment first, evidence-backed fix second.* Model lifecycle - models get deprecated, new ones come out, prompts evolve, tools change. Every one of those is a release. Every release needs the same gates and evidence. Cost and capacity - PTU versus pay-as-you-go, token budgets per tenant, tool call budgets, alerts on anomalies. Increasingly important as agents move into business-critical workflows where a single noisy user can spike a six-figure bill. These concerns are connected. An incident feeds the reliability roadmap. A model change runs through the same gates. A cost anomaly triggers an incident if severe enough. Every one feeds back into evaluation. Let's go deeper into the two concerns customers struggle with most.

---

## Slide 20 - AI incident runbook

**SP1:** When something goes wrong in production, the runbook turns a fire drill into a sequence. The severity table sets expectations. S1 Critical - safety event or data leak. First action: stop gate, rollback to last known good version. We don't investigate first. *We contain first.* S2 High - quality or grounding regression. Planned rollback or version pin. Give ourselves time to diagnose without users seeing degraded behavior. S3 Medium - latency degradation or cost spike. Rate-limit, investigate, then act. We don't roll back yet. We measure, identify, decide. S4 Low - drift indicator on a single metric. Schedule analysis in the next eval cycle. Monitor. If it worsens, escalate. The triage flow: detect - the alert fires. Correlate trace - find the trace ID, the conversation, the version, the environment. Identify version - what was deployed, what changed? Contain - apply the first action from the severity table. Stop the bleeding. Analyze - why did it happen? What evaluators do we run? Fix - implement the change. Re-evaluate - the fix passes the gate, same as any other change. We don't ship fixes on a fast lane. Close with evidence - postmortem to the artifact, failing case to the eval dataset, runbook updated if needed. Every closed incident makes the operating model stronger. The eval dataset grows. The gate criteria tighten. The runbook gets tailored. Build it. Use it. Update it after every incident.

---

## Slide 21 - Model lifecycle and canary upgrades

**SP1:** Model lifecycle is the second pain point. Every customer right now is having this conversation. The model we depend on is being deprecated. A new model came out. The vendor changed terms. What do we do? The answer: same gates, same evidence, as any other release candidate. *Treat every model change as a release.* Triggers: deprecation, new model availability, cost or performance pressure, vendor change. The canary process. Step one - pin the current model as the baseline. Exact version, exact deployment, exact configuration. Pinned. Step two - run the new model against the eval dataset offline. Same dataset, same evaluators, two models side by side. We see where the new one is better, where it's worse. Step three - promote to a canary traffic slice. Five percent. Real production users, real conversations. Step four - compare live quality, cost, latency, and safety against the baseline. The canary slice produces traces. We run evaluators on those traces. Step five - roll forward or roll back, with evidence. Quality scores, cost comparison, safety findings. It's not a gut call. It's evidence-backed. Ownership: the AI platform team coordinates the infrastructure, the application team validates against their use cases. Both sign off. If you have the eval dataset and release contract from earlier slides, model lifecycle becomes a routine release. Not a crisis. Just another canary, with evidence.

---

## Slide 22 - Section: Adoption

**SP2:** We've covered foundations, evaluation, CI/CD, observability, and Day-2. That's the operating model. Now the question we get most often: where do I start? Start small. Build the pattern.

---

## Slide 23 - Start with one production-candidate agent

**SP2:** Close with a practical adoption path. *Don't start with every agent. Start with one.* Step one - pick one agent. One. Not your portfolio. One agent that is close to production today, with a real owner, real users in pilot, and real business value. Step two - define release criteria and a small eval dataset. Write down the criteria. Minimum quality, groundedness, no new harmful content findings. Build the dataset - even just twenty representative cases. Real user journeys, real edge cases, real mistakes the agent has made before. Step three - wire telemetry, traces, dashboards, and alerts. Application Insights connected. OpenTelemetry spans flowing. At least one dashboard, at least one alert for the worst-case failure mode. Doesn't have to be perfect. Has to exist. Step four - add PR and deploy gates. The eval runs on PR, runs on deploy. The gate blocks if scores drop. The first time a developer sees a failed PR because of an eval regression, you'll know it's working. Step five - review readiness evidence weekly. Thirty-minute meeting. Walk through eval reports, safety findings, incidents, what's going into the dataset. The rhythm is what makes it stick. Step six - promote production learnings into future evals. Reviewed traces become eval rows. Postmortem findings become regression tests. Red team findings become adversarial coverage. The dataset grows. The next gate is stronger. Thirty days. Six steps. One agent. *Move one agent from "it works in testing" to "we can operate it safely."* Once you've done that, you have the pattern. The pattern scales across the portfolio without re-litigating every decision. Thank you for watching.
