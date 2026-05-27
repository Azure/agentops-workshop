---
title: Speaker Script
layout: default
parent: Short Workshop
nav_order: 6
---

# Short Workshop Speaker Script (Verbatim)

This is the word-for-word narration for the 23-slide AgentOps deck, designed for a recorded video.

## How to use this script

- **Target duration:** ~50 minutes of narration (leaves margin for editing).
- **Target pace:** ~145 words per minute - measured, conversational, with natural pauses.
- **Cumulative timing** is shown next to each slide heading. Use it as a guardrail while recording.
- **Stage directions** appear in `[brackets]` - for emphasis, pauses, or visual cues. Do not read them aloud.
- **Italics** indicate words to land hard - the through-line phrases of the session.
- Section dividers (lead slides) are short transitions. The audience sees the title for a few seconds while you bridge into the next block - do not rush past them, but do not linger.

---

## Slide 1 - Title: AgentOps - From Agent Prototype to Production

*Cumulative: 0:00 - 0:42*

Welcome. In the next hour, we're going to talk about something that has become the central question for teams building AI agents today. Not how to build the first demo - we already know how to do that. The question now is harder. *Can we safely ship this agent? And where is the evidence?*

This session is about that operating model. We call it AgentOps. It is how we take the production engineering discipline we already trust for traditional software, and apply it to AI agents, where behavior is probabilistic, tools have side effects, and yesterday's safe answer might not be safe tomorrow.

---

## Slide 2 - Agenda

*Cumulative: 0:42 - 1:46*

We have six blocks for one hour. We will move quickly, but I want you to hold the shape of the conversation in your head as we go.

First, AgentOps foundations. Why AI operations need a new discipline. What the operating loop looks like. And how mature teams really are today.

Second, evaluation. The release signal that tells us whether a new version of the agent is actually better, or just different.

Third, CI/CD. The gates that turn that evaluation signal into a release decision.

Fourth, observability. Once the agent is in production, how do we see what it is actually doing, and how do we close the loop back to evaluation?

Fifth, Day-2 operations. Incident response and model lifecycle.

And we will close on adoption - how to start, on Monday morning, with one agent.

---

## Slide 3 - Section: AgentOps Foundations

*Cumulative: 1:46 - 2:11*

All right. Let us start with foundations. Before we talk about evaluators, pipelines, or dashboards, I want to spend a few minutes on why we need any of this. Why traditional DevOps is not enough for agents. What changes when an agent can call tools, hold memory, and make decisions on its own.

---

## Slide 4 - The production gap

*Cumulative: 2:11 - 4:53*

Here is the contrast. On the left, prototype works. On the right, production needs proof.

A prototype is one happy-path demo. The product owner sat next to a developer, watched it answer three questions correctly, and said yes, ship this. Production needs repeatable evaluation across many cases - dozens, hundreds, sometimes thousands.

A prototype gets a manual quality check. Production needs release evidence. Something I can show to a security reviewer, a compliance officer, or my own boss, that says yes, this version was tested against these criteria, and it passed.

A prototype is a single-version snapshot. Production has versioned models, versioned prompts, versioned tool definitions. All three of those things change. A new version of GPT-4 ships. The prompt gets edited. A tool's API changes. Each one of those can shift behavior. We have to know what we shipped, and when.

And the killer one - "it looked good last week." That is the most dangerous sentence in agent development. Because the agent is probabilistic. The model can drift. The data behind a retrieval source can drift. User behavior changes. Yesterday's confident answer becomes tomorrow's hallucination.

So we need trace-backed Day-2 operations. Not just dashboards - traces. The actual chain of reasoning the agent went through.

The quote at the bottom of the slide is the through-line for the whole session. *The bottleneck moved.* It used to be: can we build the first demo? Now it is: *can we prove that the next version is safe to release?*

Because if you build a good agent, more people are going to use it. As soon as it is in front of real users, every change is a release. Every change needs evidence. And without the operating model, every change is a fire drill.

That is the production gap. And it is why we need a new operating discipline - not a new tool.

---

## Slide 5 - Complexity from prompts to agents

*Cumulative: 4:53 - 7:39*

Why does this need a new operating discipline at all? Why can we not just use the DevOps practices we already have?

The answer is in this ladder. As we move up, every rung adds new operational surface.

At the bottom: simple prompts. We send a question, we get an answer. The tradeoffs are quality and cost. Was the response good? How many tokens did it use? Manageable. We have been doing this for two years.

Next rung: RAG. Retrieval-augmented generation. Now we have to think about grounding. Did the answer come from the right document? About retrieval quality. Did we pull the right chunk? About data freshness. Is the source up to date? And about permissions. Did the user have access to the data that informed the answer?

Next rung: tool-using agents. Now the model is calling functions. It is planning a sequence of steps. Each tool call has side effects - it sends an email, updates a record, queries a database. Each tool call has an auth boundary. Did we have permission? Did we leak data? The blast radius of a wrong action just got much, much bigger.

Next rung: single agents with memory. Now the agent remembers things between turns. It builds context over a conversation, sometimes over days. Multi-step traces become the unit of behavior - not single requests. A bug might emerge only on the seventh turn, because of something the agent remembered from the third turn.

And at the top: multi-agent systems. Orchestrators that coordinate sub-agents. Now we have emergent behavior. Two agents working together produce an outcome that neither one would produce alone. Coordination, traceability, governance - all multiply.

The point of this slide is not that everyone is doing multi-agent. The point is that even simple agents put you several rungs above where DevOps practices were designed to operate. Multi-step plans and tool calls multiply the failure surface. Snapshot testing - the way we have always tested code - is just not enough.

We need a different kind of evidence. Repeatable evaluation, on real cases, against current and previous versions. Tied to traces. Tied to releases. That is what the rest of the session is going to walk through.

---

## Slide 6 - AgentOps operating model

*Cumulative: 7:39 - 11:25*

This is the operating model itself. The AgentOps loop. Six steps. They are the heart of the session - everything we talk about for the next forty-five minutes is one of these six steps. So I want to take a minute on each.

First: *evaluate.* This happens before we ship anything. We have a curated dataset - what we call a golden dataset - of representative user journeys. We run the current and the candidate version against it. We measure quality, groundedness, latency, cost, and agent-specific things like intent resolution and tool call accuracy. We do not ship blind.

Second: *gate.* The evaluation result becomes a gate in CI/CD. If quality drops below threshold, the pipeline fails. If safety scores regress, the pipeline fails. If we want to override the gate, we add human approval and we leave an audit trail. The gate is the strongest moment in the loop. The point at which a bad version stops, before users ever see it.

Third: *observe.* Once the version is in production, we need to see what the agent is actually doing. Not just CPU and memory - we need traces. The full chain: prompt, plan, model call, tool call, retrieval, safety event, latency, cost, user feedback. All of that. We use Foundry observability and Application Insights together.

Fourth: *diagnose.* Observability is not the goal. The goal is to make sense of what we are seeing. So we run evaluators on production samples. We compare them against the baseline. We use the traces to find the root cause of regressions, of safety findings, of cost spikes. Diagnosis is what turns telemetry into actionable evidence.

Fifth: *ship.* When we know what is wrong and how to fix it, we ship the fix. Canary rollout. Five percent of traffic first, then fifty, then full. We version the model, the prompt, the tools - all three - together. So the release artifact is reproducible.

Sixth: *improve.* This is the part that closes the loop. The reviewed traces from production become new rows in the eval dataset. The dataset grows. Next time we run a gate, we test against everything we have learned so far. The eval set is a living artifact, not a one-time deliverable.

People - process - platform. The triangle in the center of the diagram. People means the operating model is owned. There is an on-call. There are runbooks. There are reviewers. Process means we follow the loop on every change, not just the big ones. Platform means we use Foundry as the control plane and we wire telemetry, traces, evaluators, and pipelines together.

The output of all six steps is two things. *Release evidence* - we can prove this version is safe to ship. And *operational confidence* - when something goes wrong, we know how to find it and fix it.

That is AgentOps. The rest of this session is how to actually do each step.

---

## Slide 7 - Maturity model

*Cumulative: 11:25 - 13:55*

Quick self-assessment. Where is your team right now? There are four levels, and I would bet that almost everyone in this room is somewhere between the first two.

Level one - Initial. Ad hoc demos. Manual evaluation - someone in the team types five questions, looks at the answers, says yeah, this seems fine. No gates. Logs are scattered across half a dozen places. If you ask the team to explain a regression from last week, they cannot. This is where most agent projects start, and it is perfectly fine for a prototype. But it does not scale.

Level two - Defined. Prompts are versioned. Agents are versioned. There is a pre-prod eval dataset, even if it is small. CI builds artifacts. The team can answer: what is the current version, where did it come from, what did we test it against. This is the minimum bar for any agent going in front of real users.

Level three - Managed. Now we have gates - quality gates, safety gates, in CI. Continuous evaluation runs on production. There are runbooks and SLOs. The team treats agent operations like they would treat any other production system. This is where most enterprise customers want to be within twelve months.

Level four - Optimised. Drift and cost guardrails. Canary plus auto-rollback. The feedback flywheel is real - every reviewed production trace becomes a new eval row within hours, not weeks. This is where the most mature customers are heading, and a small number are already there.

The honest message on this slide is the one in the call-out: *do not try to boil the ocean.* Do not try to move every agent across all four levels at once. Pick one production-candidate agent. Move it up one level. Build the pattern. Then scale it across the portfolio. That is the realistic path.

So before we go any further: think about which agent in your portfolio you would take through this in the next thirty days. We will come back to that thirty-day plan at the end.

---

## Slide 8 - Microsoft Foundry is the control plane

*Cumulative: 13:55 - 16:33*

Let me clarify positioning, because this comes up in every conversation. Where does Foundry fit, and where does AgentOps fit on top?

Foundry is the control plane. It has three layers, and they are all on the slide.

The surfaces layer is how teams interact with Foundry. There is the portal - the web UI. There is the SDK - Python, JavaScript, C-sharp - for embedding in applications. There is the Azure CLI and the REST APIs for automation. And there are GitHub Actions for putting Foundry inside a pipeline. Same control plane, different ways in.

The capabilities layer is what Foundry actually does for agents. It manages agents and versions. It has built-in evaluators for quality, groundedness, fluency, coherence. It has agent-specific evaluators - intent resolution, task adherence, tool call accuracy. It hosts the AI Red Teaming Agent, which is the PyRIT-based automated adversarial testing. It supports OpenTelemetry tracing natively. And it integrates with Content Safety for runtime policy checks.

The runtime layer is where the agent actually executes. Azure AI projects host the agents. Model deployments serve the models. Tool servers and MCP servers provide the actions. Application Insights and Log Analytics collect the telemetry.

That is Foundry. Now: *AgentOps is not a replacement for any of this.* It is not a new tool we are trying to sell you instead of Foundry. AgentOps is an operating model that connects Foundry signals to release decisions and to Day-2 action.

If Foundry tells you the eval failed, AgentOps is the practice that stops the pipeline. If Foundry tells you a trace had a safety event, AgentOps is the practice that pulls that trace into the eval dataset for next release. If Foundry tells you cost spiked, AgentOps is the practice that triggers the APIM throttle and notifies FinOps.

Foundry is the source of truth. AgentOps is what we do with that truth to ship safely, every time, in a repeatable way.

If you remember one thing from this slide: when we talk about AgentOps for the next forty minutes, we are not talking about replacing Foundry. We are talking about the operating discipline around it.

---

## Slide 9 - Production readiness checklist

*Cumulative: 16:33 - 18:54*

This is the slide I want you to take a picture of. The production readiness checklist. The release evidence contract for any agent you are about to put in front of users.

Seven items. Every one of them maps to slides we are about to walk through.

One: target and version are explicit. We know exactly which agent, exactly which version, with exactly which prompt and which tools, we are about to release.

Two: an eval dataset exists, and thresholds are agreed. A minimum quality score. A minimum groundedness score. A minimum on intent resolution. Below those, the release stops.

Three: the CI/CD gate actively blocks regressions. Not advisory. Not informational. If eval drops, the pipeline fails. The PR cannot merge. The deploy cannot proceed.

Four: telemetry and traces are wired. Application Insights is collecting. OpenTelemetry spans cover prompt, model call, tool call, retrieval. Trace IDs flow through end to end.

Five: safety and red-team findings are tracked. We have run the Red Teaming Agent at least once before release. The findings are recorded. The harmful content categories - jailbreak, hallucination, data exfiltration - are all being scored.

Six: the release evidence is reviewable. Not in someone's head. Not in a Slack thread. In an artifact. Eval reports, readiness reports, content safety scans - all attached to the release.

Seven: owners know what to do when signals fail. There is an on-call. There is a runbook. There is a triage flow. When something breaks - and something will break - we do not improvise. We follow the runbook.

The quote on this slide is the point of the whole list. *It turns "I think it works" into "we have evidence for this release."* The same way we do not ship code without unit tests, we should not ship agents without these seven things.

Every section that follows fills out one or more items on this checklist. So as we go, mentally check them off.

---

## Slide 10 - Section: Evaluation

*Cumulative: 18:54 - 19:11*

And the first item on that checklist - probably the most important one - is evaluation. The eval dataset, the thresholds, the release signal. That is where we go next. The release signal for agentic systems.

---

## Slide 11 - Evaluation strategy

*Cumulative: 19:11 - 22:39*

Three stages of evaluation. The whole life of the agent, not just the moment before release.

Stage one - base model selection. Before we even write the agent, before the prompt exists, we have to pick the model. And model choice is an evaluation problem. We do not just pick GPT-4, or pick Llama, or pick whatever the team is excited about this quarter. We test candidates against a small representative dataset. We measure cost per response. We measure latency. We measure quality on the actual use case. And we choose with evidence.

Stage two - pre-production evaluation. This is the gate I mentioned earlier. The candidate version of the agent runs against a golden dataset, with the built-in evaluators. We get scores. We compare against the previous version. We compare against absolute thresholds. If we pass, we promote. If we fail, the regression has to be diagnosed before anything ships.

The golden dataset - this is the part teams underestimate. It does not need to be huge. A few dozen carefully chosen cases, tied to real user journeys, beats zero cases by an enormous margin. Quality questions, edge cases, common mistakes the agent has made before, scenarios the product owner cares about. The goal is coverage of behavior, not statistical perfection.

Foundry's built-in evaluators cover most of what you need. Quality, groundedness, coherence, fluency. The agent-specific evaluators - intent resolution, task adherence, tool call accuracy - are particularly important if the agent is calling functions or following a multi-step plan. Those evaluators ask: did the agent actually do the right thing? Not just, did the answer read well.

Stage three - post-production monitoring. The eval is not done when we ship. We keep evaluating. We sample production traces. We run them through the same evaluators. We watch for drift. We watch for quality drops. We watch for new failure modes that did not exist in the golden dataset.

And here is the loop-closing part. The interesting production traces - the ones that surface new behavior, the ones that show a regression, the ones that catch a weird tool call - those become new rows in the golden dataset. Next time we run the gate, we test against everything we have learned. *The dataset is alive.*

The minimum viable eval is small but real. A few dozen rows. Run on every PR. Compared against the last release. With a clear pass-fail threshold. That is the bar.

Do not wait until you have the perfect dataset. Do not wait until you have a thousand cases. Start with twenty. Catch your first regression. Add the failing case as row twenty-one. That is how the eval set grows, and that is how the team starts to trust the gate.

---

## Slide 12 - Red teaming and AI safety

*Cumulative: 22:39 - 25:58*

*Quality and safety are different signals.* This is the most important sentence on this slide, and it is the part teams most often miss.

A quality score will tell you whether the answer was coherent, grounded, and useful. It will not tell you whether someone could jailbreak the agent into revealing secrets. It will not tell you whether a prompt injection could get the agent to send a malicious email. Those are different problems, with different test cases, and a different cadence.

So Foundry ships an AI Red Teaming Agent. It is backed by PyRIT, Microsoft's open-source framework for AI red teaming. Instead of doing adversarial testing ad-hoc - someone in security poking at the agent for a day every six months - we automate it. The agent runs against curated adversarial scenarios on a schedule.

The four risk categories on the slide cover the main attack surface.

First - harmful content. Hate speech, violence, sexual content, self-harm. Things the agent should refuse to produce, no matter how cleverly someone asks. Content Safety in Azure handles a lot of this at runtime, but red teaming verifies it works for new prompts and new models.

Second - jailbreak. Prompt injection. Role hijacking. Getting the agent to ignore its system prompt. Some of these techniques are public and well-known. New ones come out every month. The Red Teaming Agent maintains a library and tests them automatically.

Third - hallucination. Ungrounded claims. Fake citations. Confidently wrong answers. This overlaps with quality, but the adversarial framing is different. We are not asking, did the agent answer well? We are asking, can we trick the agent into making up a confident answer when it should not?

Fourth - data exfiltration. PII leakage. Secrets in system prompts being echoed back. Tool abuse - getting the agent to call a tool with parameters it should not. Especially important if your agent has any access to internal systems.

Cadence matters. We run red teaming as a release gate - same as quality eval, before merge. We run it on a schedule, typically weekly, to catch drift. And we run it post-incident, when something has gone wrong, to make sure we do not ship the same vulnerability again.

The findings from red teaming feed straight back into the eval dataset. A jailbreak that worked once becomes an adversarial row. Next time we run the gate, we test against that exact attack. If anyone tries it again, we catch it before users do.

Quality and safety together are the two columns of the release contract. Quality says the agent is good. Safety says the agent cannot be abused. Both have to pass.

---

## Slide 13 - Section: CI/CD for Agentic AI

*Cumulative: 25:58 - 26:19*

All right. We have evaluation. We have red teaming. We have a golden dataset. Now we need to turn all of that into a release decision. We need pipelines and gates. CI/CD for agentic AI. Gates that enforce the release evidence we just talked about.

---

## Slide 14 - CI/CD gates for agentic AI

*Cumulative: 26:19 - 29:30*

Here is where DevOps discipline meets agentic systems. The pipeline pattern looks familiar - build, evaluate, gate decision, deploy. But the contents are agent-specific.

Build, in this context, means we package the agent. The model version, the prompt template, the tool definitions, the configuration. All versioned together, as a single artifact. That is important - because if the prompt changes, the agent's behavior changes. If the tool definition changes, the agent's behavior changes. We need a single thing we can roll forward or roll back.

Evaluate is the stage we just talked about. The candidate artifact runs against the golden dataset. The Red Teaming Agent runs. The evaluators produce scores. The result is an evidence pack - eval report, red team report, content safety scan, dependency check.

Gate decision is the moment of truth. Are the scores above the thresholds? Did the red team find anything new? Is the cost projection within budget? If all yes, the gate passes. If any no, the gate fails. The pipeline stops.

This is the part I want to land hard. *The strongest moment in the whole pipeline is a failed gate.* Not a passed gate. A failed gate. Because that is the moment a bad version was about to reach users, and instead it stopped. The gate paid for itself, ten times over, in that one moment.

Three kinds of gates in practice.

PR gates - block bad prompts and bad config before merge. Fast, lightweight, focused on regression detection. Run on every pull request.

Deploy gates - block bad versions before they reach the next environment. Heavier, slower, with the full eval suite. Run on every promotion - dev to QA, QA to prod, prod canary to prod full.

Watchdogs - scheduled checks against production. Catch drift between releases. Catch tool dependency failures. Catch model behavior changes from upstream model updates. Run on a daily or hourly schedule.

Each gate produces an artifact. Eval report. Readiness report. Release evidence. These artifacts are not just for the pipeline - they are for the audit trail. When a compliance officer asks "how do you know this version was safe?", you can point to the artifact. When the customer asks "what was different about last month's release?", you can pull the report.

The artifacts are the evidence. The evidence is what gives the team the confidence to actually ship.

GitHub Actions is the easiest way to wire this up if you are already on GitHub. Azure DevOps Pipelines works the same way. Foundry's CLI plugs into either one. The mechanism is well understood. What is new is what we are measuring and gating on.

---

## Slide 15 - Section: Observability

*Cumulative: 29:30 - 29:47*

Pipelines and gates are the release-time part of the loop. But the operating model does not stop at release. We need to see what the agent is doing in production. Observability. Traces, correlation, and the closed loop.

---

## Slide 16 - Observability for agents is more than monitoring

*Cumulative: 29:47 - 33:06*

Observability for agents is more than monitoring. This distinction matters - I will spend a minute on it before we go any further.

Monitoring asks: is the service healthy? Is the endpoint up? Is latency within target? Is the error rate normal? Those questions matter. They will always matter. But they are not enough for an agent.

Observability asks a different question: *what did the agent do, and why did it do it?* Not, did it respond in 800 milliseconds? But, what was the prompt? What tools did it call? What documents did retrieval surface? What safety event fired? What was the chain of decisions?

For agents, the unit of understanding is the trace, not the endpoint status. The whole point of an agent is that it makes decisions. If we only see the endpoint, we have no idea what decisions were made. We only see the outcome.

The Foundry observability stack has three pillars, and the slide shows them.

Pillar one - tracing. OpenTelemetry-based spans across the agent's execution. Every model call, every tool call, every retrieval, every safety event - all spans, all correlated by trace ID. Native to Foundry, exportable to Application Insights, queryable in Log Analytics.

Pillar two - monitoring. The classic stuff. Latency, error rate, token throughput, resource health. Still important. Still needed. Just no longer enough on its own.

Pillar three - continuous evaluation. The evaluators we talked about earlier, but now running on production samples. Quality scores on real conversations. Groundedness checks on actual responses. Intent resolution on what users actually asked. The eval pipeline is now also a runtime signal.

These three pillars stack. Continuous evaluation gives you the macro health - is the agent still doing what it should? Monitoring gives you the service health - is the agent available? Tracing gives you the explanation - when something went wrong, what actually happened?

The required signals - what every agent trace should contain - are listed in my notes. Prompt, plan, model call, retrieval, tool call, safety event, latency, cost, user feedback, release version. Get those, and you have a real trace.

The required correlation - what links the trace to everything else - is even more important. Trace ID. Session ID. Agent version. Deployment. Eval run. Incident. Owner. Without correlation, you have a pile of dashboards that do not talk to each other. With correlation, the same trace can answer questions across release, runtime, evaluation, and Day-2 contexts.

I am going to repeat this because it is the foundation of the next slide. *Correlation is what turns observability from a set of dashboards into an operating signal.* Without it, you have data. With it, you have evidence.

---

## Slide 17 - From telemetry to action

*Cumulative: 33:06 - 36:29*

This is the connective tissue slide for the whole session. *Telemetry is not the goal. Action is.*

Let me walk through this concretely, signal by signal.

Latency spike. The trace shows that a particular tool call is taking ten times longer than baseline. Azure Monitor fires an alert. The on-call gets paged. They look at the trace. They see the tool is timing out. They disable that tool, fall back to a manual path, file the bug, and the agent stays responsive.

Tool error rate climbs. The monitoring dashboard shows that thirty percent of calls to a particular API are returning 500s. The on-call disables the tool. The agent gracefully degrades - "I cannot access that system right now, here is what I can help with instead." Users still get value. We are not down.

Safety violation. The Content Safety pipeline blocks a response because it would have contained personal data. The trace is captured. A safety incident is opened. The reviewed trace is added to the red team dataset. Next release, that exact attempt is part of the regression suite. The pattern does not recur.

Eval score drop. Continuous evaluation is running on production samples. Quality on a particular intent has dropped from 0.92 to 0.78. Below the threshold. The canary - if we are in the middle of a rollout - is paused. A ticket is opened. The trace data is pulled. The team diagnoses. Maybe it is a model change. Maybe it is a prompt change. Maybe it is a data shift. We find out.

Cost anomaly. Token usage on a particular tenant has tripled overnight. The APIM gateway throttles. FinOps gets notified. Maybe it is legitimate adoption. Maybe it is an attack. Either way, the cost does not run away while we figure it out.

Positive feedback. A user gave a thumbs-up on a particularly tricky question. That trace gets sampled into the eval dataset, as a positive example. We are building coverage of what good looks like.

That is the operating loop in action. Every signal triggers a concrete operational response, and every response feeds back into the eval set, the gates, or the runbook.

*This is how observability funds evaluation.* Reviewed traces become new eval rows. And *this is how evaluation funds release confidence.* The expanded eval set makes the next gate stronger.

If you only remember one slide from this session, this would be a good candidate. Telemetry by itself is just data. The discipline is to make it action. Every signal, every alert, every reviewed trace - feeds something. The dataset, the runbook, the gate, the canary decision. Always feeds something.

That is the closed loop. That is how we keep getting better, release after release.

---

## Slide 18 - Section: Day-2 Operations

*Cumulative: 36:29 - 36:44*

Speaking of release after release - the loop runs every day after launch. That is Day-2 operations. Running agents in production. Where most of the actual work lives, long after the launch demo.

---

## Slide 19 - Day-2 operations - four concerns

*Cumulative: 36:44 - 39:39*

Day-2 is where most of the operational reality lives. The hard part is not getting the agent to launch. The hard part is keeping it useful, safe, and reliable on day ninety, day one-eighty, day three-sixty-five.

Four concerns, on the quadrant. They are interlocking - not independent.

Reliability and SLOs. What is the agent's availability target? What is its latency target? What is its error rate budget? When a downstream tool fails, does the agent gracefully degrade, or does it fall over entirely? Tool dependency mapping matters here. A lot of agents have eight, ten, fifteen tool dependencies. Each one is a potential failure mode. Each one needs a degradation strategy.

Incident response. Severity classes, runbooks, on-call rotations. The next slide is going to walk through this in detail. The shortcut version: when an agent misbehaves, we need a sequence, not improvisation. *Containment first, evidence-backed fix second.*

Model lifecycle. Models get deprecated. New models come out. Prompts need to evolve. Tools change. Every one of those is a release. Every release needs the same gates and the same evidence. We will spend a slide on this too - it is one of the most common pain points we hear from customers right now.

Cost and capacity. PTU - provisioned throughput units - versus pay-as-you-go. Token budgets per tenant. Tool call budgets to prevent runaway costs. Alerts on anomalies. This is increasingly important as agents move into business-critical workflows, where a single noisy user can spike a six-figure bill.

The point of the quadrant is to show that these are connected. An incident produces a postmortem that feeds the reliability roadmap. A model lifecycle change runs through the same gates as any other release. A cost anomaly triggers an incident if it is bad enough. The quadrants flow into each other through the operating loop.

And every one of these concerns feeds back into evaluation. A reliability incident becomes an eval row. A model change becomes a baseline comparison run. A cost anomaly becomes a token-budget test. The four quadrants are not separate columns of work - they are four ways the same loop manifests in production.

The next two slides go deeper into the two concerns that I find customers struggle with most: incident response and model lifecycle.

---

## Slide 20 - AI incident runbook

*Cumulative: 39:39 - 43:15*

AI incident runbook. When something goes wrong in production, the runbook turns a fire drill into a sequence. The severity table sets expectations. The triage flow makes containment explicit.

Let us walk through the severity classes.

S1 Critical - safety event or data leak in production. Real harm or real exposure is happening, right now. First action: stop gate immediately, rollback to last known good version, contain. We do not investigate first. *We contain first.* The bleeding stops, then we diagnose.

S2 High - quality or grounding regression after deploy. The agent is still up, but it is giving worse answers than the previous version. Maybe it is hallucinating more. Maybe it is failing intent resolution on a key user journey. First action: planned rollback, or version pin. We give ourselves time to diagnose without users continuing to see degraded behavior.

S3 Medium - latency degradation or cost spike. The agent is functional, but it is slow, or it is expensive. First action: rate-limit, investigate, then act. We do not roll back yet. We measure, we identify, then we decide.

S4 Low - drift indicator on a single metric. Something to watch, not something to react to immediately. Schedule analysis in the next eval cycle. The eval set grows. The drift is monitored. If it gets worse, it escalates.

That is the severity table. Now the triage flow.

Eight steps. Detect - the alert fires or someone reports it. Correlate trace - we find the trace ID, we find the conversation, we know which user, which version, which environment. Identify version - what was deployed? What changed? When was the last successful release? Contain - we apply the first action from the severity table. Rollback, throttle, disable tool, pause canary. We stop the bleeding. Analyze - now we diagnose. Why did it happen? What evaluators do we run on the trace? What is the root cause? Fix - we implement the change. Re-evaluate - the fix has to pass the gate, same as any other change. We do not ship the fix on a fast lane. We run it through evaluation. Close with evidence - we add the postmortem to the artifact. We add the failing case to the eval dataset as a regression test. We update the runbook if needed.

*Containment first. Evidence-backed fix second.* That is the principle.

Every closed incident produces evidence. The eval dataset gets a new row. The gate criteria might get tightened. The runbook might get updated. The operating model gets stronger.

The runbook is a living artifact. The first version, on day one, can be very simple. By day ninety, it is tailored to the specific failure modes of your specific agent. By day one-eighty, it is how the on-call actually responds. Build it. Use it. Update it after every incident. That is how Day-2 stops being scary.

---

## Slide 21 - Model lifecycle and canary upgrades

*Cumulative: 43:15 - 46:47*

Model lifecycle is the second pain point I want to land. This is the conversation we have with every customer right now. "The model we depend on is being deprecated. A new model just came out. The vendor changed terms. What do we do?"

The answer is the same gates, the same evidence, as any other release candidate. *We treat the model change as a release.*

Triggers, on the slide. Deprecation - the existing model is end of life. New model availability - GPT-4 to GPT-4-turbo to the next thing. Cost or performance pressure - the same quality at lower cost is real money. Vendor change - we are switching from one provider to another.

The canary process - same DevOps pattern, applied to models.

Step one - pin the current model version as the baseline. We need to know exactly what we are comparing against. Not "the current production model." The exact version, exact deployment, exact configuration. Pinned.

Step two - run the new model against the eval dataset, offline. Before any production traffic touches it, we have a quality comparison. Same dataset, same evaluators, two model versions side by side. We see where the new model is better, where it is worse, where it is different.

Step three - promote the new model to a canary traffic slice. Five percent of traffic. Real production users. Real conversations. The previous ninety-five percent stays on the baseline. We cannot simulate user behavior - we have to measure it.

Step four - compare live quality, cost, latency, and safety against the baseline. The canary slice produces traces. We run the evaluators on those traces. We measure. We compare. If the new model is better, we promote. If it is worse, we pause and diagnose.

Step five - roll forward or roll back, with evidence. The decision is in the artifact. Quality scores. Cost comparison. Latency comparison. Safety findings. It is not a gut call - it is an evidence-backed decision.

Ownership matters. The AI platform team coordinates the model change. The application team validates against their specific use cases. Both have to sign off. The platform team makes sure the infrastructure is ready - new deployment, capacity, throttling. The application team makes sure the agent still does what it should.

Canary upgrades are not new to DevOps. We have been doing this for software for years. The reason it feels new for AI is that historically, model upgrades happened invisibly. The vendor pushed an update, we did not notice, sometimes we did notice when things broke. With agents in business-critical workflows, that is not acceptable.

If you have the eval dataset and the release contract from earlier slides, the model lifecycle becomes a routine release. Not a crisis. Not a fire drill. Just another canary, with evidence.

---

## Slide 22 - Section: Adoption

*Cumulative: 46:47 - 47:08*

All right. We have covered the foundations, evaluation, CI/CD, observability, and Day-2. That is the operating model. Now I want to close on adoption. Because the question I get most often, after a session like this, is: where do I start? Start small. Build the pattern.

---

## Slide 23 - Start with one production-candidate agent

*Cumulative: 47:08 - 50:07*

Close with a practical adoption path. *Do not start with every agent. Start with one.*

I want to be specific about this, because well-intentioned teams often try to do too much at once, and then nothing actually ships.

Step one - pick one agent. One. Not your portfolio. Not your roadmap. One agent that is close to production today. Probably one that has a real owner, real users in pilot or about to be, and real business value. Not a sandbox. Not a demo. Something that is actually about to go to production.

Step two - define release criteria and a small eval dataset. Write down the criteria. Minimum quality score. Minimum groundedness. No new harmful content findings. Build the eval dataset - even just twenty representative cases. The cases are real user journeys, real edge cases, real things you have already seen the agent get wrong. Twenty is fine for the first iteration.

Step three - wire telemetry, traces, dashboards, and alerts. Application Insights connected. OpenTelemetry spans flowing. Foundry observability turned on. At least one dashboard for the agent. At least one alert for the worst-case failure mode. Does not have to be perfect. Has to exist.

Step four - add PR and deploy gates. The eval runs on PR. The eval runs on deploy. The gate blocks if scores drop. The first time a developer sees a failed PR because of an eval regression, you will know it is working.

Step five - review readiness evidence weekly. Pick a thirty-minute meeting. Walk through the eval reports. Walk through the safety findings. Walk through the incidents. Walk through what is going into the eval dataset. The rhythm is what makes it stick.

Step six - promote production learnings into future evals. Reviewed traces become eval rows. Postmortem findings become regression tests. Red team findings become adversarial coverage. The dataset grows. The next gate is stronger.

Thirty days. Six steps. One agent. That is how it starts.

The call to action is the quote at the bottom. *Move one agent from "it works in testing" to "we can operate it safely."* Once you have done that, you have the pattern. The pattern scales across the portfolio without re-litigating every decision.

Thank you. I am happy to take questions.

---

## Recording notes

- Pace the script at ~145 words per minute. Slow down on the signature sentences in italics.
- Take a short breath at every paragraph break. The script is written so paragraph breaks line up with natural slide-reading rhythm.
- The six section dividers (slides 3, 10, 13, 15, 18, 22) are deliberate breathers. Show the title on screen for the full duration of the transition narration, then advance.
- For video editing chapter markers, the cumulative timestamps in each slide heading map to roughly where each slide should appear in the final cut.
- Total budget: ~50 minutes of narration. Leaves ~10 minutes of headroom for intro/outro frames, lower-thirds, and Q&A if recorded live.
