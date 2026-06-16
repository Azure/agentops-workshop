---
title: Speaker Script

layout: default

parent: Short Workshop

nav_order: 6

---

# Short Workshop Speaker Script (Dual-Voice)

Dual-voice narration for the AgentOps deck. Two speakers with an even split across the session.

## How to use this script

- **One primary speaker per slide.** Speaker turns are marked `**SP1:** ` and `**SP2:**`. The markers are parsed by `prep/tools/render_speech.py` and mapped to two distinct Azure Neural voices.

- **Target duration:** ~50 minutes of narration.

- **Pace:** ~145 wpm, measured and conversational.

- **Italics** indicate words to land hard.

- Section dividers are short transitions spoken by whichever speaker owns the next content slides.

- The original single-voice version of this script is preserved at `prep/short/speaker-script-single.md` for reference.
## Speaker assignment

| Section | Slides | Speaker | Duration | Running Total |
|---------|--------|---------|----------|---------------|
| Title + Agenda | 1-2 | SP2 | 1:30 | 1:30 |
| Foundations | 3-5 (gap, building blocks) | SP2 | 3:30 | 5:00 |
| Foundations | 6-8 (Foundry, checklist, operating model) | SP2 | 4:45 | 9:45 |
| Foundations | 9 (maturity model) | SP2 | 2:30 | 12:15 |
| Architecture | 10 (reference architecture) | SP1 | 4:30 (measured) | 15:09 |
| Evaluate | 11-13 | SP1 | 3:53 (estimate) | 19:02 |
| Demo - Evaluate | 14 | SP1 | 5:00 | 24:02 |
| Ship | 15-16 | SP1 | 2:41 (estimate) | 26:43 |
| Demo - Ship | 17 | SP1 | 5:00 | 31:43 |
| Observe | 18-20 | SP1 | 3:50 (estimate) | 35:33 |
| Demo - Observe | 21 | SP1 | 5:00 | 40:33 |
| Own | 22-25 | SP1 | 5:36 (estimate) | 46:09 |
| Demo - Own | 26 | SP1 | 5:00 | 51:09 |
| Your Next Steps | 27-28 | SP2 | 2:17 (estimate) | 53:26 |
| Thank You | 29 | SP2 | 0:22 (estimate) | 53:48 |
| Resources | 30 | SP2 | 0:20 (estimate) | 54:08 |

### names suggestions 
SP1 - Paulo
SP2 - Rick 

---

## Slide 1 - Title: AgentOps - From Agent Prototype to Production

**SP2:** 

Welcome everyone to the AgentOps webinar!

In this session, we're going to be talking about the central question for teams building AI agents today....

Not 'how to build the first demo' - we already know how to do that. 

The question now is harder. *Can we safely ship this agent? And where is the evidence?* 

That's what this session is about. The operating model we call - AgentOps. 

It's how we take the production engineering discipline we already trust for traditional software and apply it to AI agents, where behavior is probabilistic, tools have side effects, and yesterday's safe answer might not be safe tomorrow.

---

## Slide 2 - Agenda

**SP2:** We have a few sections for this session. 

First, AgentOps Foundations - introduction to why AI operations need a new discipline, what the four-pillar model looks like, and where teams feel they sit today. 

Then we'll go a a bit deeper into the four pillars themselves:

Evaluate - the release signal that tells us whether a new version is actually better, or just different.


Ship - the gates, approvals, and evidence that turn that signal into a release decision.


Observe - once the agent is live, how we see what it's doing through traces, metrics, and feedback.

Own - running the agent over time, incident response and model lifecycle. 

And we'll close on Adoption and your next steps - how to start, on Monday morning, with one agent.

Don't hestitate to put questions in the chat as we go.

---

## Slide 3 - Section: AgentOps Foundations

**SP2:** Let's start with foundations. 

Before we talk about evaluators, pipelines, or dashboards, we want to spend a few minutes on... why we need any of this.?? 

Why isn't traditional DevOps enough for agents? 

What changes happen when an agent can call tools, hold memory, and make decisions on its own, is it the same?? 

---

## Slide 4 - The production gap

**SP2:** Here's the contrast. On the left, prototype works. On the right, production needs proof.


A prototype is one happy-path demo. The product owner watched it answer three questions correctly and said yes, ship this.


Production needs repeatable evaluation across dozens or hundreds of cases.


A prototype gets a manual quality check. Production needs release evidence - something you can show to a security reviewer, a compliance officer, that says this version was tested against these criteria and it passed.


A prototype is a single-version snapshot. Production has versioned models, versioned prompts, versioned tool definitions. All three change. A new model ships. The prompt gets edited. A tool's API changes. Each one shifts behavior.

We have to know what we shipped, and when.

And the killer one - "it looked good last week." That's the most dangerous sentence in agent development.

The agent is probabilistic. The model can drift. The data behind retrieval can drift. User behavior changes. Yesterday's confident answer becomes tomorrow's hallucination.

*The bottleneck moved.* It used to be: can we build the first demo? Now it is: can we prove that the next version is safe to release?


Without the operating model, every change is a fire drill.

---

## Slide 5 - Building blocks of a production agent

**SP2:** Why does this need a new operating discipline? Why can't we just use the DevOps practices we already have?

**SP2:** Why does this need a new operating discipline? Why can't we just use the DevOps practices we already have?

The answer is in this table. As we move up, every tier adds new operational surface.

At the bottom: simple prompts. We send a question, we get an answer. The tradeoffs are quality and cost. Manageable.

Next tier up: RAG. Now we think about grounding, retrieval quality, data freshness, and permissions. Did the user have access to the data that informed the answer?

Next: tool-using agents. The model is calling functions, planning steps, each with side effects and auth boundaries. The blast radius of a wrong action gets much bigger.

Then single agents with memory. Multi-step traces become the unit of behavior. A bug might emerge on the seventh turn because of something remembered from the third.

At the top: multi-agent systems. Orchestrators coordinating sub-agents. Emergent behavior.

The point is that even simple agents put you several tiers above where DevOps practices were designed to operate. Multi-step plans and tool calls multiply the failure surface.

Snapshot testing is just not enough. We need a different kind of evidence.

---

## Slide 6 - Microsoft Foundry is the control plane

**SP2:** Let's clarify positioning, because this comes up in every conversation. Where does Foundry fit, and where does AgentOps fit on top?

Foundry is the control plane. Three layers.

The surfaces layer is how teams interact - the portal, the SDK, Azure CLI and REST APIs, and GitHub Actions. Same control plane, different ways in.

The capabilities layer is what Foundry does for agents. It manages agents and versions. It has built-in evaluators for quality, groundedness, fluency, coherence. It has agent-specific evaluators - intent resolution, task adherence, tool call accuracy. It hosts the AI Red Teaming Agent backed by PyRIT. It supports OpenTelemetry tracing natively. And it integrates with Content Safety for runtime policy checks.

The runtime layer is where the agent executes - Azure AI projects, model deployments, tool and MCP servers, Application Insights and Log Analytics.

*AgentOps is not a replacement for any of this.* It's the operating model that connects Foundry signals to release decisions and Day-2 action.

Foundry is the source of truth. AgentOps is what we do with that truth, to ship safely, every time.

---

## Slide 7 - Production readiness checklist

**SP2:** This is the slide we want you to take a note of.


The production readiness checklist. The release evidence contract for any agent you're about to put in front of users.


Seven items.


One: target and version are explicit. We know exactly which agent, which version, which prompt, which tools we're releasing.


Two: an eval dataset exists and thresholds are agreed. Minimum quality, groundedness, intent resolution. Below those, the release stops.


Three: the CI/CD gate actively blocks regressions. Not advisory. If eval drops, the pipeline fails. 


Four: telemetry and traces are wired. Application Insights collecting, OpenTelemetry spans flowing, trace IDs end to end.


Five: safety and red-team findings are tracked. The Red Teaming Agent has run at least once before release.


Six: release evidence is reviewable. Not in someone's head. In an artifact attached to the release. 


Seven: owners know what to do when signals fail. There's an on-call, a runbook, a triage flow. It turns "I think it works" into "we have evidence for this release."


Every section that follows fills out one or more items on this checklist.

---

## Slide 8 - AgentOps operating model

**SP2:** So we have the checklist - seven items that tell us what evidence a production release needs.

The question is: how do we produce that evidence repeatably, every release, without heroics?

That's what the operating model gives us. Four pillars. Evaluate, ship, observe, own.

Everything we talk about lives inside one of these four pillars.

First: *evaluate.* We have a curated golden dataset of representative user journeys. We run the current and candidate versions against it. We measure quality, groundedness, latency, cost, intent resolution, tool call accuracy. We don't ship blind. That's covering Datasets, rubrics for scoring, red teaming, thresholds for the decision to proceed or not, to Ship.

Second: *ship.* The evaluation result becomes a gate in CI/CD. If quality drops below threshold, the pipeline fails. If safety regresses, the pipeline fails. We promote with evidence - human approvals, environment promotion, and a canary rollout where model, prompt, and tools are versioned together. A failed gate is the strongest moment in the model - the point at which a bad version stops before users ever see it.

Third: *observe.* Once in production, we need traces. The full chain: prompt, plan, model call, tool call, retrieval, safety event, latency, cost, user feedback. We use Foundry observability and Application Insights together, correlated so the same trace question answers across release, runtime, and evaluation.

Fourth: *own.* This is where we operate the agent over time. Diagnose root cause from traces and evaluators on production samples. Run the incident runbook. Manage model lifecycle, cost, and capacity. And improve - reviewed traces from production become new rows in the eval dataset, so the next evaluation, tests against everything we've learned.

People, process, platform are key to this success. 

People means the agent is owned - there's an on-call, runbooks, reviewers.

Process means we follow the four pillars on every change. 
 
Platform means Foundry as the control plane with telemetry, traces, evaluators, and pipelines wired together.

The output is *release evidence* and *operational confidence*.

Now that we know the model, the question is: where does your team sit today?

---

## Slide 9 - Maturity model

**SP2:** Quick self-assessment. Where is your team right now?

Four levels, and we'd bet almost everyone is somewhere between the first two.

Level one - Initial. Ad hoc demos. Manual evaluation. Someone types five questions, looks at the answers, says yeah this seems fine. No gates, logs scattered. If you ask the team to explain a regression from last week, they can't.

Level two - Defined. Prompts are versioned. Agents are versioned. There's a pre-prod eval dataset. CI builds artifacts. The team can answer: what's the current version, what did we test it against? This is the minimum bar for any agent going in front of real users.

Level three - Managed. Quality and safety gates in CI. Continuous evaluation on production. Runbooks and SLOs. This is where most enterprise customers want to be within twelve months.

Level four - Optimised. Drift and cost guardrails. Canary plus auto-rollback. The feedback flywheel is real - every reviewed production trace becomes a new eval row within hours.

I'll pause these to let you have a think as to where you currently fit into this. 

Now let's look at what this model actually looks like as a reference architecture on Foundry.

---

## Slide 10 - AgentOps Architecture

**SP1:** This picture is the bridge between the operating model and the real implementation.


So instead of reading it box by box, let's follow one agent version as it moves from an idea to production.

It starts on the left, in the inner loop. This is where the team is still learning.


The sandbox Foundry Project is the safe place to design the agent: the instructions, the tools, the model choice, the knowledge sources, and the early behavior.


The developer is working in VS Code or Copilot CLI, using a framework like Microsoft Agent Framework or LangGraph when they need orchestration or MCP tools.


But the important point is this: even in the inner loop, the agent is already treated like a versioned product.


The prompt, tool definitions, configuration, CI workflow, and evaluation evidence live in source control, in GitHub or Azure DevOps.


That means the agent is not just something configured in a portal. It is something the team can review, compare, promote, and roll back.

Then the agent candidate moves to the right side: operationalizing.


This is the outer loop, where we stop asking "does it work on my machine?" and start asking "do we have enough evidence to promote it?"


Continuous delivery moves the same candidate through dev, qa, and prod.


Each environment has its own Foundry Project, because each environment has a different purpose.


Dev is shared development. It is where the team runs manual tests, quality evaluations, and safety evaluations quickly.


QA is where the bar gets higher. We add integration testing, red-team coverage, and the release evidence package.


And between QA and prod, there is a gated approval. That approval should not be a rubber stamp. It should be a human looking at the evidence and deciding whether the version is ready.

When the agent reaches prod, the goal changes again.


Prod is about safe rollout: smoke tests, blue-green or canary rollout, and controlled exposure.


We are not trying to rediscover the evaluation result in prod. The evaluation evidence was locked in QA.


Prod is where we prove the rollout is healthy and where we watch real user behavior carefully.

Now look at the runtime choices across the environments.


The same pattern works whether this is a Prompt Agent managed by Foundry, a Hosted Agent running as a container through Agent Service, or a BYO compute runtime on Container Apps or AKS.


That matters because AgentOps should not depend on one runtime shape.


The operating model is consistent: version the agent, evaluate it, gate it, observe it, and feed production learning back into the next version.

At the bottom is the control plane that keeps the loop connected.

Foundry gives us the operational view: overview, assets, compliance, quota, traces, and evaluations.

Application Insights and Log Analytics hold the detailed telemetry, and Azure Monitor turns important signals into alerts.

This is where a trace from production becomes more than a log line.

It tells us which version ran, which model call happened, which tool was invoked, what the latency and cost looked like, and whether there was a safety or quality signal.

The dashed feedback loop is the most important part of the diagram.

Production is not the end of the process. Production teaches the next evaluation set.

A failed trace becomes a regression case. A safety event becomes a red-team scenario. A latency or cost issue becomes a release criterion.

That is the AgentOps loop on Foundry: create, evaluate, promote with evidence, observe in production, and improve the next version from what we learned.

With that architecture in mind, let's dive into the first pillar: Evaluate.

---

## Slide 11 - Section: Evaluate

**SP1:** The first item on that checklist, probably the most important one, is evaluation.

The eval dataset, the thresholds, the release signal. That's where we go next.

---

## Slide 12 - Evaluation strategy

**SP1:** Three stages of evaluation across the whole life of the agent.

Stage one - base model selection. Before we write the agent, we pick the model with evidence. We test candidates against a representative dataset. We measure cost, latency, and quality on the actual use case. We choose with evidence, not excitement.

Stage two - pre-production evaluation. The candidate version runs against a golden dataset with built-in evaluators. We get scores. We compare against the previous version and against absolute thresholds. If we pass, we promote. If we fail, the regression has to be diagnosed before anything ships.

The golden dataset does not need to be huge. A few dozen carefully chosen cases tied to real user journeys beats zero cases by an enormous margin.

Foundry's built-in evaluators cover quality, groundedness, coherence, fluency. The agent-specific evaluators - intent resolution, task adherence, tool call accuracy - are critical if the agent calls functions or follows multi-step plans.

Stage three - post-production monitoring. We keep evaluating. We sample production traces. We run them through the same evaluators. We watch for drift, quality drops, new failure modes.

The interesting traces - regressions, weird tool calls, new behavior - become new rows in the golden dataset. *The dataset is alive.*

Don't wait for the perfect dataset. Start with twenty cases. Catch your first regression. Add the failing case as row twenty-one. That's how the team starts to trust the gate.

---

## Slide 13 - Red teaming and AI safety

**SP1:** *Quality and safety are different signals.*

A quality score tells you whether the answer was coherent, grounded, and useful. It will not tell you whether someone could jailbreak the agent into revealing secrets or trick it into sending a malicious email.

Those are different problems, with different test cases, and a different cadence.

Foundry ships an AI Red Teaming Agent backed by PyRIT. Instead of ad-hoc adversarial testing every six months, we automate it on a schedule.

Four risk categories.

First - harmful content. Hate speech, violence, things the agent should refuse no matter how cleverly someone asks.

Second - jailbreak. Prompt injection, role hijacking, getting the agent to ignore its system prompt. New techniques come out every month; the Red Teaming Agent maintains a library.

Third - hallucination. Ungrounded claims, fake citations. The adversarial framing is different from quality - we're asking can we *trick* the agent into making things up?

Fourth - data exfiltration. PII leakage, secrets echoed back, tool abuse. Especially important if the agent has access to internal systems.

Cadence: pre-release gate, scheduled weekly, and post-incident. Findings feed straight back into the eval dataset as adversarial rows. A jailbreak that worked once becomes a regression test. Next time, we catch it before users do.

One more piece announced at Build 2026 - *Adaptive Evaluations* paired with the *ASSERT* framework. ASSERT stands for Agent Security and Safety Evaluation Run-Time. The idea: take your governance policies and automatically convert them into eval test cases. Instead of hand-writing every adversarial scenario, the platform generates tests from your policies. It's in preview now.

Quality says the agent is good. Safety says the agent can't be abused. Both have to pass.

Now - how do we enforce these signals? That brings us to the Ship pillar, and CI/CD gates.

---

## Slide 14 - Demo - Evaluate

**SP1:** Let's see evaluation in action.

I'll walk through a golden dataset run on Foundry, the evaluator scores, and how the release signal is produced.

---

## Slide 15 - Section: Ship

**SP1:** We have evaluation. We have red teaming. We have a golden dataset.

Now we need to turn all of that into a release decision.

This is the Ship pillar. Pipelines and gates. CI/CD for agentic AI.

---

## Slide 16 - CI/CD gates for agentic AI

**SP1:** The pipeline pattern looks familiar - build, evaluate, gate decision, deploy - but the contents are agent-specific.

Build means we package the agent. The model version, prompt template, tool definitions, configuration. All versioned together as a single artifact. If the prompt changes, behavior changes. If the tool definition changes, behavior changes. We need a single thing we can roll forward or roll back.

Evaluate is the stage we just covered. The candidate runs against the golden dataset. The Red Teaming Agent runs. The evaluators produce scores. The result is an evidence pack - eval report, red team report, content safety scan, dependency check.

Gate decision is the moment of truth. Are scores above thresholds? Did red team find anything new? Is cost within budget? If all yes, the gate passes. If any no, the gate fails.

*The strongest moment in the whole pipeline is a failed gate.* That's the moment a bad version was about to reach users and instead it stopped.

Three kinds of gates.

PR gates - block bad prompts before merge. Fast, lightweight, on every pull request.

Deploy gates - block bad versions before the next environment. Full eval suite on every promotion.

Watchdogs - scheduled checks against production. Catch drift, tool failures, upstream model changes.

Each gate produces an artifact for the audit trail. When compliance asks "how do you know this was safe?" you point to the artifact.

And this extends beyond CI/CD now. The *Agent Control Specification* - ACS - announced at Build 2026 defines eight interception points in the agent's runtime: startup, input, pre-model-call, post-model-call, pre-tool-call, post-tool-call, output, and shutdown. Policies evaluated at each point, as code. It works across Foundry, Microsoft Agent Framework, and LangChain. Open-source under the Agent Governance Toolkit on GitHub.

Think of it as CI/CD gates that follow the agent into production - not just at deploy time, but on every single request.

GitHub Actions or Azure DevOps pipelines. Either works. The pattern is the same.

---

## Slide 17 - Demo - Ship

**SP1:** Let me show you a failed gate in action.

A prompt change triggers the pipeline, the evaluator scores drop below threshold, and the gate blocks the deployment. That's the strongest moment in the model.

---

## Slide 18 - Section: Observe

**SP1:** Pipelines and gates are the release-time part of the model. But the operating model doesn't stop at release.

This is the Observe pillar. We need to see what the agent is doing in production.

Traces, correlation, and the closed loop.

---

## Slide 19 - Observability for agents is more than monitoring

**SP1:** This distinction matters.

Monitoring asks: is the service healthy? Is the endpoint up? Is latency within target? Those questions matter, but they're not enough for an agent.

Observability asks a different question. *What did the agent do, and why did it do it?* Not did it respond in 800 milliseconds, but what was the prompt? What tools did it call? What documents did retrieval surface? What safety event fired? What was the chain of decisions?

For agents, the unit of understanding is the trace, not the endpoint status.

The Foundry observability stack has three pillars.

Pillar one - tracing. OpenTelemetry-based spans across the agent's execution. Every model call, tool call, retrieval, safety event. All correlated by trace ID. Native to Foundry, exportable to Application Insights, queryable in Log Analytics.

Pillar two - monitoring. The classic signals. Latency, error rate, token throughput, resource health. Still important, just no longer enough on its own.

Pillar three - continuous evaluation. The evaluators running on production samples. Quality scores on real conversations. Groundedness checks on actual responses. The eval pipeline is now also a runtime signal.

These three stack. Continuous evaluation gives you macro health. Monitoring gives you service health. Tracing gives you the explanation.

The required signals: prompt, plan, model call, retrieval, tool call, safety event, latency, cost, user feedback, release version.

The required correlation: trace ID, session ID, agent version, deployment, eval run, incident, owner.

Without correlation, observability is disconnected dashboards. With it, the same trace answers questions across release, runtime, evaluation, and Day-2.

*Correlation turns observability from dashboards into an operating signal.*

---

## Slide 20 - From telemetry to action

**SP1:** This is the connective tissue slide for the whole session. *Telemetry is not the goal. Action is.*

Let's walk through it signal by signal.

Latency spike - the trace shows a tool call taking ten times longer than baseline. Azure Monitor fires an alert. The on-call looks at the trace, sees the tool timing out, disables it, falls back to a manual path. The agent stays responsive.

Tool error rate climbs - thirty percent of calls returning 500s. Disable the tool. The agent gracefully degrades. Users still get value.

Safety violation - Content Safety blocks a response containing personal data. The trace is captured, a safety incident opened. The reviewed trace goes into the red team dataset. Next release, that exact attempt is part of the regression suite.

Eval score drop - continuous evaluation shows quality on a particular intent dropped from 0.92 to 0.78. Below threshold. The canary pauses. A ticket opens. We diagnose.

Cost anomaly - token usage on a tenant tripled overnight. APIM throttles. FinOps gets notified. We figure out if it's legitimate adoption or an attack.

Positive feedback - a user gave a thumbs-up on a tricky question. That trace gets sampled into the eval dataset as a positive example.

Every signal triggers a concrete operational response. Every response feeds back into the eval set, the gates, or the runbook.

*This is how Observe feeds Own, and how Own feeds the next Evaluate and Ship cycle.* The closed loop.

That's how we keep getting better, release after release.

---

## Slide 21 - Demo - Observe

**SP1:** Let's look at a real trace.

I'll show the trace waterfall, correlated spans across model calls and tool calls, and how a signal fires an alert and feeds back into the eval dataset.

---

## Slide 22 - Section: Own

**SP1:** The model runs every day after launch.

This is the Own pillar - Day-2 operations. Running agents in production.

Where most of the actual work lives, long after the launch demo.

---

## Slide 23 - Day-2 operations - four concerns

**SP1:** Day-2 is where most of the operational reality lives. The hard part is not getting the agent to launch. The hard part is keeping it useful, safe, and reliable on day ninety, day one-eighty, day three-sixty-five.

Four concerns on the quadrant, and they're interlocking.

Reliability and SLOs - availability, latency, error rate budgets. When a downstream tool fails, does the agent gracefully degrade or fall over? Tool dependency mapping matters. Agents often have ten or fifteen tool dependencies, each a potential failure mode.

Incident response - severity classes, runbooks, on-call rotations. When an agent misbehaves, we need a sequence, not improvisation. *Containment first, evidence-backed fix second.*

Model lifecycle - models get deprecated, new ones come out, prompts evolve, tools change. Every one of those is a release. Every release needs the same gates and evidence.

Cost and capacity - PTU versus pay-as-you-go, token budgets per tenant, tool call budgets, alerts on anomalies. Increasingly important as agents move into business-critical workflows where a single noisy user can spike a six-figure bill.

One more thing worth naming here. *Microsoft Agent 365* went generally available in May 2026 as the enterprise governance umbrella for agents. Three pillars: observe, govern, secure. The SDK is free and framework-agnostic - it works with Microsoft Agent Framework, OpenAI Agents SDK, LangChain, Semantic Kernel.

The point: whether you build your agent on Foundry or bring it from another framework, Agent 365 gives IT one place to see every agent in the tenant, enforce policies, and audit what they did. It pairs with Defender for runtime detection and Purview for data governance.

That's the Day-2 governance layer that sits above individual agent implementations.

These concerns are connected. An incident feeds the reliability roadmap. A model change runs through the same gates. A cost anomaly triggers an incident if severe enough. Every one feeds back into evaluation.

Let's go deeper into the two concerns customers struggle with most.

---

## Slide 24 - AI incident runbook

**SP1:** When something goes wrong in production, the runbook turns a fire drill into a sequence.

The severity table sets expectations.

S1 Critical - safety event or data leak. First action: stop gate, rollback to last known good version. We don't investigate first. *We contain first.*

S2 High - quality or grounding regression. Planned rollback or version pin. Give ourselves time to diagnose without users seeing degraded behavior.

S3 Medium - latency degradation or cost spike. Rate-limit, investigate, then act. We don't roll back yet. We measure, identify, decide.

S4 Low - drift indicator on a single metric. Schedule analysis in the next eval cycle. Monitor. If it worsens, escalate.

The triage flow: detect - the alert fires. Correlate trace - find the trace ID, the conversation, the version, the environment. Identify version - what was deployed, what changed? Contain - apply the first action from the severity table. Stop the bleeding.

Analyze - why did it happen? What evaluators do we run? Fix - implement the change.

Re-evaluate - the fix passes the gate, same as any other change. We don't ship fixes on a fast lane.

Close with evidence - postmortem to the artifact, failing case to the eval dataset, runbook updated if needed.

Every closed incident makes the operating model stronger. The eval dataset grows. The gate criteria tighten. The runbook gets tailored.

Build it. Use it. Update it after every incident.

---

## Slide 25 - Model lifecycle and canary upgrades

**SP1:** Model lifecycle is the second pain point. Every customer right now is having this conversation.

The model we depend on is being deprecated. A new model came out. The vendor changed terms. What do we do?

The answer: same gates, same evidence, as any other release candidate. *Treat every model change as a release.*

Triggers: deprecation, new model availability, cost or performance pressure, vendor change.

The canary process.

Step one - pin the current model as the baseline. Exact version, exact deployment, exact configuration. Pinned.

Step two - run the new model against the eval dataset offline. Same dataset, same evaluators, two models side by side. We see where the new one is better, where it's worse.

Step three - promote to a canary traffic slice. Five percent. Real production users, real conversations.

Step four - compare live quality, cost, latency, and safety against the baseline. The canary slice produces traces. We run evaluators on those traces.

Step five - roll forward or roll back, with evidence. Quality scores, cost comparison, safety findings. It's not a gut call. It's evidence-backed.

Ownership: the AI platform team coordinates the infrastructure, the application team validates against their use cases. Both sign off.

If you have the eval dataset and release contract from earlier slides, model lifecycle becomes a routine release. Not a crisis. Just another canary, with evidence.

---

## Slide 26 - Demo - Own

**SP1:** For this last demo, I'll show incident triage from a production trace, a model canary comparison side by side, and how production learnings feed back into the eval dataset to close the loop.

---

## Slide 27 - Section: Your Next Steps

**SP2:** We've covered foundations and the four pillars - evaluate, ship, observe, own. That's the operating model.

Now the question we get most often: where do I start?

Start small. Build the pattern.


---

## Slide 28 - Start with one production-candidate agent

**SP2:** Close with a practical path. *Don't start with every agent. Start with one.*

Lets recap and incorporate all that you've seen into your next steps......

Step one - pick one agent. One. Not your portfolio. One agent that is close to production today, with a real owner, real users in pilot, and real business value.

Step two - evaluate it. Define release criteria and a small eval dataset. Minimum quality, groundedness, no new harmful content findings. Build the dataset - even just twenty representative cases. Real user journeys, real edge cases, real mistakes the agent has made before.

Step three - ship it. Add PR and deploy gates and a readiness evidence pack. The eval runs on PR, runs on deploy. The gate blocks if scores drop. The first time a developer sees a failed PR because of an eval regression, you'll know it's working.

Step four - observe it. Wire telemetry, traces, dashboards, and alerts. Application Insights connected. OpenTelemetry spans flowing. At least one dashboard, at least one alert for the worst-case failure mode. Doesn't have to be perfect. Has to exist.

Step five - own it. Review readiness evidence weekly. A thirty-minute meeting. Walk through eval reports, safety findings, incidents, what's going into the dataset. The rhythm is what makes it stick.

Step six - feed production learnings back into the next evaluation cycle. Reviewed traces become eval rows. Postmortem findings become regression tests. Red team findings become adversarial coverage. The dataset grows. The next gate is stronger.

And step seven - revisit the maturity model. Identify where your team sits today. Set a concrete goal to reach the next level within ninety days. That's how you build momentum.

Thirty days. One agent. Four pillars.

*You'll have moved your one agent from "it works in testing" to "we can operate it safely."* 

You'll own the improvement cycle.

You'll have the pattern. The pattern that scales across your portfolio without re-inventing every decision.

---

## Slide 29 - Thank You

**SP2:** Thank you for your time today.

If you want to continue the conversation, reach out to your account team or find us after the session.

---

## Slide 30 - Resources

**SP2:** These are the Microsoft Learn resources behind the practices we covered today.

Use them as follow-up references for evaluation, agent lifecycle, observability, red teaming, and Application Insights monitoring.
