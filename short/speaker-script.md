---
title: Speaker Script
layout: default
parent: Short Workshop
nav_order: 6
---

# Short Workshop Speaker Script (Dual-Voice)

Dual-voice narration for the 23-slide AgentOps deck, designed for a recorded video with two alternating presenters.

## How to use this script

- **Two voices alternating, no names spoken.** Speaker turns are marked `**SP1:**` and `**SP2:**`. The markers are parsed by `prep/tools/render_speech.py` and mapped to two distinct Azure Neural voices.
- **Target duration:** ~50 minutes of narration.
- **Pace:** ~145 wpm, measured and conversational.
- **Italics** indicate words to land hard.
- Section dividers (slides 3, 10, 13, 15, 18, 22) are intentionally short transitions - one or two turns each.
- The original single-voice version of this script is preserved at `prep/short/speaker-script-single.md` for reference.

---

## Slide 1 - Title: AgentOps - From Agent Prototype to Production

**SP1:** Welcome! In the next hour, we're going to talk about something that's become the central question for teams building AI agents today.

**SP2:** Not how to build the first demo - we already know how to do that. The question now is harder.

**SP1:** *Can we safely ship this agent? And where is the evidence?*

**SP2:** That's what this session is about. The operating model we call AgentOps.

**SP1:** It's how we take the production engineering discipline we already trust for traditional software, and apply it to AI agents, where behavior is probabilistic, tools have side effects, and yesterday's safe answer might not be safe tomorrow.

---

## Slide 2 - Agenda

**SP2:** We have six blocks for one hour. We'll move quickly, but hold the shape of the conversation in your head as we go.

**SP1:** First, AgentOps foundations. Why AI operations need a new discipline. What the operating loop looks like. And how mature teams really are today.

**SP2:** Second, evaluation. The release signal that tells us whether a new version of the agent is actually better, or just different.

**SP1:** Third, CI/CD. The gates that turn that evaluation signal into a release decision.

**SP2:** Fourth, observability. Once the agent is in production, how do we see what it's actually doing - and how do we close the loop back to evaluation?

**SP1:** Fifth, Day-2 operations. Incident response and model lifecycle.

**SP2:** And we'll close on adoption. How to start, on Monday morning, with one agent.

---

## Slide 3 - Section: AgentOps Foundations

**SP1:** All right. Let's start with foundations.

**SP2:** Before we talk about evaluators, pipelines, or dashboards, we want to spend a few minutes on why we need any of this. Why traditional DevOps isn't enough for agents. What changes when an agent can call tools, hold memory, and make decisions on its own.

---

## Slide 4 - The production gap

**SP2:** Here's the contrast. On the left, prototype works. On the right, production needs proof.

**SP1:** A prototype is one happy-path demo. The product owner sat next to a developer, watched it answer three questions correctly, and said yes, ship this.

**SP2:** Production needs repeatable evaluation across many cases. Dozens, hundreds, sometimes thousands.

**SP1:** A prototype gets a manual quality check. Production needs release evidence. Something you can show to a security reviewer, a compliance officer, or your own boss, that says yes - this version was tested against these criteria, and it passed.

**SP2:** A prototype is a single-version snapshot. Production has versioned models, versioned prompts, versioned tool definitions.

**SP1:** All three of those things change. A new version of GPT-4 ships. The prompt gets edited. A tool's API changes. Each one of those can shift behavior. We have to know what we shipped, and when.

**SP2:** And the killer one - "it looked good last week."

**SP1:** That's the most dangerous sentence in agent development. Because the agent is probabilistic. The model can drift. The data behind a retrieval source can drift. User behavior changes. Yesterday's confident answer becomes tomorrow's hallucination.

**SP2:** So we need trace-backed Day-2 operations. Not just dashboards. Traces. The actual chain of reasoning the agent went through.

**SP1:** The quote at the bottom is the through-line for the whole session. *The bottleneck moved.* It used to be: can we build the first demo? Now it is: can we prove that the next version is safe to release?

**SP2:** Because if you build a good agent, more people are going to use it. As soon as it's in front of real users, every change is a release. Every change needs evidence.

**SP1:** And without the operating model, every change is a fire drill.

**SP2:** That's the production gap. And it's why we need a new operating discipline, not a new tool.

---

## Slide 5 - Complexity from prompts to agents

**SP1:** Why does this need a new operating discipline at all? Why can't we just use the DevOps practices we already have?

**SP2:** The answer is in this ladder. As we move up, every rung adds new operational surface.

**SP1:** At the bottom: simple prompts. We send a question, we get an answer. The tradeoffs are quality and cost. Was the response good? How many tokens did it use? Manageable. We've been doing this for two years.

**SP2:** Next rung: RAG. Retrieval-augmented generation. Now we have to think about grounding. Did the answer come from the right document? About retrieval quality. Did we pull the right chunk?

**SP1:** About data freshness. Is the source up to date? And about permissions. Did the user have access to the data that informed the answer?

**SP2:** Next rung: tool-using agents. Now the model is calling functions. It's planning a sequence of steps. Each tool call has side effects - it sends an email, updates a record, queries a database.

**SP1:** Each tool call has an auth boundary. Did we have permission? Did we leak data? The blast radius of a wrong action just got much, much bigger.

**SP2:** Next rung: single agents with memory. Now the agent remembers things between turns. It builds context over a conversation, sometimes over days.

**SP1:** Multi-step traces become the unit of behavior, not single requests. A bug might emerge only on the seventh turn, because of something the agent remembered from the third turn.

**SP2:** And at the top: multi-agent systems. Orchestrators that coordinate sub-agents. Now we have emergent behavior. Two agents working together produce an outcome that neither one would produce alone.

**SP1:** Coordination, traceability, governance. All multiply.

**SP2:** The point of this slide is not that everyone's doing multi-agent. The point is that even simple agents put you several rungs above where DevOps practices were designed to operate.

**SP1:** Multi-step plans and tool calls multiply the failure surface. Snapshot testing, the way we've always tested code, is just not enough.

**SP2:** We need a different kind of evidence. Repeatable evaluation, on real cases, against current and previous versions. Tied to traces. Tied to releases.

**SP1:** That's what the rest of the session is going to walk through.

---

## Slide 6 - AgentOps operating model

**SP2:** This is the operating model itself. The AgentOps loop. Six steps. They're the heart of the session. Everything we talk about for the next forty-five minutes is one of these six steps.

**SP1:** So we want to take a minute on each.

**SP2:** First: *evaluate.* This happens before we ship anything. We have a curated dataset, what we call a golden dataset, of representative user journeys.

**SP1:** We run the current and the candidate version against it. We measure quality, groundedness, latency, cost, and agent-specific things like intent resolution and tool call accuracy. We don't ship blind.

**SP2:** Second: *gate.* The evaluation result becomes a gate in CI/CD. If quality drops below threshold, the pipeline fails. If safety scores regress, the pipeline fails.

**SP1:** If we want to override the gate, we add human approval and we leave an audit trail. The gate is the strongest moment in the loop. The point at which a bad version stops, before users ever see it.

**SP2:** Third: *observe.* Once the version is in production, we need to see what the agent is actually doing. Not just CPU and memory. We need traces.

**SP1:** The full chain: prompt, plan, model call, tool call, retrieval, safety event, latency, cost, user feedback. All of that. We use Foundry observability and Application Insights together.

**SP2:** Fourth: *diagnose.* Observability is not the goal. The goal is to make sense of what we're seeing.

**SP1:** So we run evaluators on production samples. We compare them against the baseline. We use the traces to find the root cause of regressions, of safety findings, of cost spikes. Diagnosis is what turns telemetry into actionable evidence.

**SP2:** Fifth: *ship.* When we know what's wrong and how to fix it, we ship the fix. Canary rollout. Five percent of traffic first, then fifty, then full.

**SP1:** We version the model, the prompt, the tools, all three, together. So the release artifact is reproducible.

**SP2:** Sixth: *improve.* This is the part that closes the loop. The reviewed traces from production become new rows in the eval dataset. The dataset grows.

**SP1:** Next time we run a gate, we test against everything we've learned so far. The eval set is a living artifact, not a one-time deliverable.

**SP2:** People, process, platform. The triangle in the center of the diagram. People means the operating model is owned. There's an on-call. There are runbooks. There are reviewers.

**SP1:** Process means we follow the loop on every change, not just the big ones. Platform means we use Foundry as the control plane and we wire telemetry, traces, evaluators, and pipelines together.

**SP2:** The output of all six steps is two things. *Release evidence* - we can prove this version is safe to ship. And *operational confidence* - when something goes wrong, we know how to find it and fix it.

**SP1:** That's AgentOps. The rest of this session is how to actually do each step.

---

## Slide 7 - Maturity model

**SP1:** Quick self-assessment. Where is your team right now?

**SP2:** There are four levels, and we'd bet that almost everyone in this room is somewhere between the first two.

**SP1:** Level one - Initial. Ad hoc demos. Manual evaluation. Someone in the team types five questions, looks at the answers, says yeah, this seems fine. No gates. Logs scattered across half a dozen places.

**SP2:** If you ask the team to explain a regression from last week, they can't. This is where most agent projects start, and it's perfectly fine for a prototype. But it doesn't scale.

**SP1:** Level two - Defined. Prompts are versioned. Agents are versioned. There's a pre-prod eval dataset, even if it's small. CI builds artifacts.

**SP2:** The team can answer: what's the current version, where did it come from, what did we test it against? This is the minimum bar for any agent going in front of real users.

**SP1:** Level three - Managed. Now we have gates. Quality gates, safety gates, in CI. Continuous evaluation runs on production. There are runbooks and SLOs.

**SP2:** The team treats agent operations like they would treat any other production system. This is where most enterprise customers want to be within twelve months.

**SP1:** Level four - Optimised. Drift and cost guardrails. Canary plus auto-rollback. The feedback flywheel is real. Every reviewed production trace becomes a new eval row within hours, not weeks.

**SP2:** This is where the most mature customers are heading, and a small number are already there.

**SP1:** The honest message on this slide is the one in the call-out. *Don't try to boil the ocean.* Don't try to move every agent across all four levels at once.

**SP2:** Pick one production-candidate agent. Move it up one level. Build the pattern. Then scale it across the portfolio. That's the realistic path.

**SP1:** So before we go any further, think about which agent in your portfolio you'd take through this in the next thirty days. We'll come back to that thirty-day plan at the end.

---

## Slide 8 - Microsoft Foundry is the control plane

**SP2:** Let's clarify positioning, because this comes up in every conversation. Where does Foundry fit, and where does AgentOps fit on top?

**SP1:** Foundry is the control plane. It has three layers, and they're all on the slide.

**SP2:** The surfaces layer is how teams interact with Foundry. There's the portal, the web UI. There's the SDK, Python, JavaScript, C-sharp, for embedding in applications.

**SP1:** There's the Azure CLI and the REST APIs for automation. And there are GitHub Actions for putting Foundry inside a pipeline. Same control plane, different ways in.

**SP2:** The capabilities layer is what Foundry actually does for agents. It manages agents and versions. It has built-in evaluators for quality, groundedness, fluency, coherence.

**SP1:** It has agent-specific evaluators. Intent resolution, task adherence, tool call accuracy. It hosts the AI Red Teaming Agent, which is the PyRIT-based automated adversarial testing. It supports OpenTelemetry tracing natively. And it integrates with Content Safety for runtime policy checks.

**SP2:** The runtime layer is where the agent actually executes. Azure AI projects host the agents. Model deployments serve the models. Tool servers and MCP servers provide the actions. Application Insights and Log Analytics collect the telemetry.

**SP1:** That's Foundry. Now, *AgentOps is not a replacement for any of this.* It's not a new tool we're trying to sell you instead of Foundry.

**SP2:** AgentOps is an operating model that connects Foundry signals to release decisions and to Day-2 action.

**SP1:** If Foundry tells you the eval failed, AgentOps is the practice that stops the pipeline. If Foundry tells you a trace had a safety event, AgentOps is the practice that pulls that trace into the eval dataset for next release. If Foundry tells you cost spiked, AgentOps is the practice that triggers the APIM throttle and notifies FinOps.

**SP2:** Foundry is the source of truth. AgentOps is what we do with that truth, to ship safely, every time, in a repeatable way.

**SP1:** If you remember one thing from this slide: when we talk about AgentOps for the next forty minutes, we're not talking about replacing Foundry. We're talking about the operating discipline around it.

---

## Slide 9 - Production readiness checklist

**SP2:** This is the slide we want you to take a picture of. The production readiness checklist. The release evidence contract for any agent you're about to put in front of users.

**SP1:** Seven items. Every one of them maps to slides we're about to walk through.

**SP2:** One: target and version are explicit. We know exactly which agent, exactly which version, with exactly which prompt and which tools, we're about to release.

**SP1:** Two: an eval dataset exists, and thresholds are agreed. A minimum quality score. A minimum groundedness score. A minimum on intent resolution. Below those, the release stops.

**SP2:** Three: the CI/CD gate actively blocks regressions. Not advisory. Not informational. If eval drops, the pipeline fails. The PR cannot merge. The deploy cannot proceed.

**SP1:** Four: telemetry and traces are wired. Application Insights is collecting. OpenTelemetry spans cover prompt, model call, tool call, retrieval. Trace IDs flow through end to end.

**SP2:** Five: safety and red-team findings are tracked. We've run the Red Teaming Agent at least once before release. The findings are recorded. The harmful content categories, jailbreak, hallucination, data exfiltration, are all being scored.

**SP1:** Six: the release evidence is reviewable. Not in someone's head. Not in a Slack thread. In an artifact. Eval reports, readiness reports, content safety scans, all attached to the release.

**SP2:** Seven: owners know what to do when signals fail. There's an on-call. There's a runbook. There's a triage flow. When something breaks, and something will break, we don't improvise. We follow the runbook.

**SP1:** The quote on this slide is the point of the whole list. It turns "I think it works" into "we have evidence for this release."

**SP2:** The same way we don't ship code without unit tests, we shouldn't ship agents without these seven things.

**SP1:** Every section that follows fills out one or more items on this checklist. So as we go, mentally check them off.

---

## Slide 10 - Section: Evaluation

**SP1:** And the first item on that checklist, probably the most important one, is evaluation.

**SP2:** The eval dataset, the thresholds, the release signal. That's where we go next. The release signal for agentic systems.

---

## Slide 11 - Evaluation strategy

**SP1:** Three stages of evaluation. The whole life of the agent, not just the moment before release.

**SP2:** Stage one - base model selection. Before we even write the agent, before the prompt exists, we have to pick the model. And model choice is an evaluation problem.

**SP1:** We don't just pick GPT-4, or pick Llama, or pick whatever the team is excited about this quarter. We test candidates against a small representative dataset. We measure cost per response. We measure latency. We measure quality on the actual use case.

**SP2:** And we choose with evidence.

**SP1:** Stage two - pre-production evaluation. This is the gate we mentioned earlier. The candidate version of the agent runs against a golden dataset, with the built-in evaluators.

**SP2:** We get scores. We compare against the previous version. We compare against absolute thresholds. If we pass, we promote. If we fail, the regression has to be diagnosed before anything ships.

**SP1:** The golden dataset. This is the part teams underestimate. It does not need to be huge. A few dozen carefully chosen cases, tied to real user journeys, beats zero cases by an enormous margin.

**SP2:** Quality questions, edge cases, common mistakes the agent has made before, scenarios the product owner cares about. The goal is coverage of behavior, not statistical perfection.

**SP1:** Foundry's built-in evaluators cover most of what you need. Quality, groundedness, coherence, fluency.

**SP2:** The agent-specific evaluators, intent resolution, task adherence, tool call accuracy, are particularly important if the agent is calling functions or following a multi-step plan. Those evaluators ask: did the agent actually do the right thing? Not just, did the answer read well.

**SP1:** Stage three - post-production monitoring. The eval is not done when we ship. We keep evaluating. We sample production traces. We run them through the same evaluators. We watch for drift. We watch for quality drops. We watch for new failure modes that didn't exist in the golden dataset.

**SP2:** And here's the loop-closing part. The interesting production traces, the ones that surface new behavior, the ones that show a regression, the ones that catch a weird tool call, those become new rows in the golden dataset.

**SP1:** Next time we run the gate, we test against everything we've learned. *The dataset is alive.*

**SP2:** The minimum viable eval is small but real. A few dozen rows. Run on every PR. Compared against the last release. With a clear pass-fail threshold. That's the bar.

**SP1:** Don't wait until you have the perfect dataset. Don't wait until you have a thousand cases. Start with twenty. Catch your first regression. Add the failing case as row twenty-one.

**SP2:** That's how the eval set grows, and that's how the team starts to trust the gate.

---

## Slide 12 - Red teaming and AI safety

**SP2:** *Quality and safety are different signals.* This is the most important sentence on this slide, and it's the part teams most often miss.

**SP1:** A quality score will tell you whether the answer was coherent, grounded, and useful. It will not tell you whether someone could jailbreak the agent into revealing secrets.

**SP2:** It will not tell you whether a prompt injection could get the agent to send a malicious email. Those are different problems, with different test cases, and a different cadence.

**SP1:** So Foundry ships an AI Red Teaming Agent. It's backed by PyRIT, Microsoft's open-source framework for AI red teaming.

**SP2:** Instead of doing adversarial testing ad-hoc, someone in security poking at the agent for a day every six months, we automate it. The agent runs against curated adversarial scenarios on a schedule.

**SP1:** The four risk categories on the slide cover the main attack surface.

**SP2:** First - harmful content. Hate speech, violence, sexual content, self-harm. Things the agent should refuse to produce, no matter how cleverly someone asks.

**SP1:** Content Safety in Azure handles a lot of this at runtime, but red teaming verifies it works for new prompts and new models.

**SP2:** Second - jailbreak. Prompt injection. Role hijacking. Getting the agent to ignore its system prompt.

**SP1:** Some of these techniques are public and well known. New ones come out every month. The Red Teaming Agent maintains a library and tests them automatically.

**SP2:** Third - hallucination. Ungrounded claims. Fake citations. Confidently wrong answers. This overlaps with quality, but the adversarial framing is different.

**SP1:** We're not asking, did the agent answer well? We're asking, can we trick the agent into making up a confident answer when it shouldn't?

**SP2:** Fourth - data exfiltration. PII leakage. Secrets in system prompts being echoed back. Tool abuse. Getting the agent to call a tool with parameters it shouldn't.

**SP1:** Especially important if your agent has any access to internal systems.

**SP2:** Cadence matters. We run red teaming as a release gate, same as quality eval, before merge. We run it on a schedule, typically weekly, to catch drift. And we run it post-incident, when something has gone wrong, to make sure we don't ship the same vulnerability again.

**SP1:** The findings from red teaming feed straight back into the eval dataset. A jailbreak that worked once becomes an adversarial row. Next time we run the gate, we test against that exact attack.

**SP2:** If anyone tries it again, we catch it before users do.

**SP1:** Quality and safety together are the two columns of the release contract. Quality says the agent is good. Safety says the agent can't be abused.

**SP2:** Both have to pass.

---

## Slide 13 - Section: CI/CD for Agentic AI

**SP2:** All right. We have evaluation. We have red teaming. We have a golden dataset. Now we need to turn all of that into a release decision.

**SP1:** We need pipelines and gates. CI/CD for agentic AI. Gates that enforce the release evidence we just talked about.

---

## Slide 14 - CI/CD gates for agentic AI

**SP1:** Here's where DevOps discipline meets agentic systems. The pipeline pattern looks familiar. Build, evaluate, gate decision, deploy. But the contents are agent-specific.

**SP2:** Build, in this context, means we package the agent. The model version, the prompt template, the tool definitions, the configuration. All versioned together, as a single artifact.

**SP1:** That's important. Because if the prompt changes, the agent's behavior changes. If the tool definition changes, the agent's behavior changes. We need a single thing we can roll forward or roll back.

**SP2:** Evaluate is the stage we just talked about. The candidate artifact runs against the golden dataset. The Red Teaming Agent runs. The evaluators produce scores.

**SP1:** The result is an evidence pack. Eval report, red team report, content safety scan, dependency check.

**SP2:** Gate decision is the moment of truth. Are the scores above the thresholds? Did the red team find anything new? Is the cost projection within budget?

**SP1:** If all yes, the gate passes. If any no, the gate fails. The pipeline stops.

**SP2:** This is the part we want to land hard. *The strongest moment in the whole pipeline is a failed gate.* Not a passed gate. A failed gate.

**SP1:** Because that's the moment a bad version was about to reach users, and instead it stopped. The gate paid for itself, ten times over, in that one moment.

**SP2:** Three kinds of gates in practice.

**SP1:** PR gates. Block bad prompts and bad config before merge. Fast, lightweight, focused on regression detection. Run on every pull request.

**SP2:** Deploy gates. Block bad versions before they reach the next environment. Heavier, slower, with the full eval suite. Run on every promotion. Dev to QA, QA to prod, prod canary to prod full.

**SP1:** Watchdogs. Scheduled checks against production. Catch drift between releases. Catch tool dependency failures. Catch model behavior changes from upstream model updates. Run on a daily or hourly schedule.

**SP2:** Each gate produces an artifact. Eval report. Readiness report. Release evidence. These artifacts are not just for the pipeline. They're for the audit trail.

**SP1:** When a compliance officer asks "how do you know this version was safe?", you can point to the artifact. When the customer asks "what was different about last month's release?", you can pull the report.

**SP2:** The artifacts are the evidence. The evidence is what gives the team the confidence to actually ship.

**SP1:** GitHub Actions is the easiest way to wire this up if you're already on GitHub. Azure DevOps Pipelines works the same way. Foundry's CLI plugs into either one. The mechanism is well understood.

**SP2:** What's new is what we're measuring and gating on.

---

## Slide 15 - Section: Observability

**SP1:** Pipelines and gates are the release-time part of the loop. But the operating model doesn't stop at release. We need to see what the agent is doing in production.

**SP2:** Observability. Traces, correlation, and the closed loop.

---

## Slide 16 - Observability for agents is more than monitoring

**SP2:** Observability for agents is more than monitoring. This distinction matters. We want to spend a minute on it before going any further.

**SP1:** Monitoring asks: is the service healthy? Is the endpoint up? Is latency within target? Is the error rate normal? Those questions matter. They will always matter.

**SP2:** But they're not enough for an agent.

**SP1:** Observability asks a different question. *What did the agent do, and why did it do it?* Not, did it respond in 800 milliseconds? But, what was the prompt? What tools did it call? What documents did retrieval surface? What safety event fired? What was the chain of decisions?

**SP2:** For agents, the unit of understanding is the trace, not the endpoint status. The whole point of an agent is that it makes decisions. If we only see the endpoint, we have no idea what decisions were made. We only see the outcome.

**SP1:** The Foundry observability stack has three pillars, and the slide shows them.

**SP2:** Pillar one - tracing. OpenTelemetry-based spans across the agent's execution. Every model call, every tool call, every retrieval, every safety event. All spans, all correlated by trace ID.

**SP1:** Native to Foundry, exportable to Application Insights, queryable in Log Analytics.

**SP2:** Pillar two - monitoring. The classic stuff. Latency, error rate, token throughput, resource health. Still important. Still needed.

**SP1:** Just no longer enough on its own.

**SP2:** Pillar three - continuous evaluation. The evaluators we talked about earlier, but now running on production samples. Quality scores on real conversations. Groundedness checks on actual responses. Intent resolution on what users actually asked.

**SP1:** The eval pipeline is now also a runtime signal.

**SP2:** These three pillars stack. Continuous evaluation gives you the macro health. Is the agent still doing what it should? Monitoring gives you the service health. Is the agent available? Tracing gives you the explanation. When something went wrong, what actually happened?

**SP1:** The required signals, what every agent trace should contain, are in the notes. Prompt, plan, model call, retrieval, tool call, safety event, latency, cost, user feedback, release version. Get those, and you have a real trace.

**SP2:** The required correlation, what links the trace to everything else, is even more important. Trace ID. Session ID. Agent version. Deployment. Eval run. Incident. Owner.

**SP1:** Without correlation, you have a pile of dashboards that don't talk to each other. With correlation, the same trace can answer questions across release, runtime, evaluation, and Day-2 contexts.

**SP2:** We'll repeat this because it's the foundation of the next slide. *Correlation is what turns observability from a set of dashboards into an operating signal.*

**SP1:** Without it, you have data. With it, you have evidence.

---

## Slide 17 - From telemetry to action

**SP1:** This is the connective tissue slide for the whole session. *Telemetry is not the goal. Action is.*

**SP2:** Let's walk through this concretely, signal by signal.

**SP1:** Latency spike. The trace shows that a particular tool call is taking ten times longer than baseline. Azure Monitor fires an alert. The on-call gets paged.

**SP2:** They look at the trace. They see the tool is timing out. They disable that tool, fall back to a manual path, file the bug, and the agent stays responsive.

**SP1:** Tool error rate climbs. The monitoring dashboard shows that thirty percent of calls to a particular API are returning 500s. The on-call disables the tool. The agent gracefully degrades. "I can't access that system right now, here's what I can help with instead." Users still get value. We're not down.

**SP2:** Safety violation. The Content Safety pipeline blocks a response because it would have contained personal data. The trace is captured. A safety incident is opened.

**SP1:** The reviewed trace is added to the red team dataset. Next release, that exact attempt is part of the regression suite. The pattern doesn't recur.

**SP2:** Eval score drop. Continuous evaluation is running on production samples. Quality on a particular intent has dropped from 0.92 to 0.78. Below the threshold.

**SP1:** The canary, if we're in the middle of a rollout, is paused. A ticket is opened. The trace data is pulled. The team diagnoses. Maybe it's a model change. Maybe it's a prompt change. Maybe it's a data shift. We find out.

**SP2:** Cost anomaly. Token usage on a particular tenant has tripled overnight. The APIM gateway throttles. FinOps gets notified.

**SP1:** Maybe it's legitimate adoption. Maybe it's an attack. Either way, the cost doesn't run away while we figure it out.

**SP2:** Positive feedback. A user gave a thumbs-up on a particularly tricky question. That trace gets sampled into the eval dataset, as a positive example. We're building coverage of what good looks like.

**SP1:** That's the operating loop in action. Every signal triggers a concrete operational response, and every response feeds back into the eval set, the gates, or the runbook.

**SP2:** *This is how observability funds evaluation.* Reviewed traces become new eval rows. *And this is how evaluation funds release confidence.* The expanded eval set makes the next gate stronger.

**SP1:** If you only remember one slide from this session, this would be a good candidate. Telemetry by itself is just data. The discipline is to make it action.

**SP2:** Every signal, every alert, every reviewed trace, feeds something. The dataset, the runbook, the gate, the canary decision. Always feeds something.

**SP1:** That's the closed loop. That's how we keep getting better, release after release.

---

## Slide 18 - Section: Day-2 Operations

**SP2:** Speaking of release after release. The loop runs every day after launch.

**SP1:** That's Day-2 operations. Running agents in production. Where most of the actual work lives, long after the launch demo.

---

## Slide 19 - Day-2 operations - four concerns

**SP1:** Day-2 is where most of the operational reality lives. The hard part is not getting the agent to launch. The hard part is keeping it useful, safe, and reliable on day ninety, day one-eighty, day three-sixty-five.

**SP2:** Four concerns, on the quadrant. They're interlocking, not independent.

**SP1:** Reliability and SLOs. What's the agent's availability target? What's its latency target? What's its error rate budget? When a downstream tool fails, does the agent gracefully degrade, or does it fall over entirely?

**SP2:** Tool dependency mapping matters here. A lot of agents have eight, ten, fifteen tool dependencies. Each one is a potential failure mode. Each one needs a degradation strategy.

**SP1:** Incident response. Severity classes, runbooks, on-call rotations. The next slide is going to walk through this in detail.

**SP2:** The shortcut version: when an agent misbehaves, we need a sequence, not improvisation. *Containment first, evidence-backed fix second.*

**SP1:** Model lifecycle. Models get deprecated. New models come out. Prompts need to evolve. Tools change. Every one of those is a release.

**SP2:** Every release needs the same gates and the same evidence. We'll spend a slide on this too. It's one of the most common pain points we hear from customers right now.

**SP1:** Cost and capacity. PTU, provisioned throughput units, versus pay-as-you-go. Token budgets per tenant. Tool call budgets to prevent runaway costs. Alerts on anomalies.

**SP2:** This is increasingly important as agents move into business-critical workflows, where a single noisy user can spike a six-figure bill.

**SP1:** The point of the quadrant is to show that these are connected. An incident produces a postmortem that feeds the reliability roadmap. A model lifecycle change runs through the same gates as any other release. A cost anomaly triggers an incident if it's bad enough.

**SP2:** The quadrants flow into each other through the operating loop.

**SP1:** And every one of these concerns feeds back into evaluation. A reliability incident becomes an eval row. A model change becomes a baseline comparison run. A cost anomaly becomes a token-budget test.

**SP2:** The four quadrants are not separate columns of work. They're four ways the same loop manifests in production.

**SP1:** The next two slides go deeper into the two concerns that customers struggle with most. Incident response and model lifecycle.

---

## Slide 20 - AI incident runbook

**SP2:** AI incident runbook. When something goes wrong in production, the runbook turns a fire drill into a sequence. The severity table sets expectations. The triage flow makes containment explicit.

**SP1:** Let's walk through the severity classes.

**SP2:** S1 Critical - safety event or data leak in production. Real harm or real exposure is happening, right now. First action: stop gate immediately, rollback to last known good version, contain.

**SP1:** We don't investigate first. *We contain first.* The bleeding stops, then we diagnose.

**SP2:** S2 High - quality or grounding regression after deploy. The agent is still up, but it's giving worse answers than the previous version. Maybe it's hallucinating more. Maybe it's failing intent resolution on a key user journey.

**SP1:** First action: planned rollback, or version pin. We give ourselves time to diagnose without users continuing to see degraded behavior.

**SP2:** S3 Medium - latency degradation or cost spike. The agent is functional, but it's slow, or it's expensive. First action: rate-limit, investigate, then act.

**SP1:** We don't roll back yet. We measure, we identify, then we decide.

**SP2:** S4 Low - drift indicator on a single metric. Something to watch, not something to react to immediately. Schedule analysis in the next eval cycle.

**SP1:** The eval set grows. The drift is monitored. If it gets worse, it escalates.

**SP2:** That's the severity table. Now the triage flow.

**SP1:** Eight steps. Detect, the alert fires or someone reports it. Correlate trace, we find the trace ID, we find the conversation, we know which user, which version, which environment.

**SP2:** Identify version. What was deployed? What changed? When was the last successful release?

**SP1:** Contain. We apply the first action from the severity table. Rollback, throttle, disable tool, pause canary. We stop the bleeding.

**SP2:** Analyze. Now we diagnose. Why did it happen? What evaluators do we run on the trace? What's the root cause?

**SP1:** Fix. We implement the change.

**SP2:** Re-evaluate. The fix has to pass the gate, same as any other change. We don't ship the fix on a fast lane. We run it through evaluation.

**SP1:** Close with evidence. We add the postmortem to the artifact. We add the failing case to the eval dataset as a regression test. We update the runbook if needed.

**SP2:** *Containment first. Evidence-backed fix second.* That's the principle.

**SP1:** Every closed incident produces evidence. The eval dataset gets a new row. The gate criteria might get tightened. The runbook might get updated. The operating model gets stronger.

**SP2:** The runbook is a living artifact. The first version, on day one, can be very simple. By day ninety, it's tailored to the specific failure modes of your specific agent. By day one-eighty, it's how the on-call actually responds.

**SP1:** Build it. Use it. Update it after every incident. That's how Day-2 stops being scary.

---

## Slide 21 - Model lifecycle and canary upgrades

**SP1:** Model lifecycle is the second pain point we want to land. This is the conversation we have with every customer right now.

**SP2:** The model we depend on is being deprecated. A new model just came out. The vendor changed terms. What do we do?

**SP1:** The answer is the same gates, the same evidence, as any other release candidate. *We treat the model change as a release.*

**SP2:** Triggers, on the slide. Deprecation, the existing model is end of life. New model availability, GPT-4 to GPT-4-turbo to the next thing.

**SP1:** Cost or performance pressure, the same quality at lower cost is real money. Vendor change, we're switching from one provider to another.

**SP2:** The canary process. Same DevOps pattern, applied to models.

**SP1:** Step one. Pin the current model version as the baseline. We need to know exactly what we're comparing against. Not "the current production model." The exact version, exact deployment, exact configuration. Pinned.

**SP2:** Step two. Run the new model against the eval dataset, offline. Before any production traffic touches it, we have a quality comparison.

**SP1:** Same dataset, same evaluators, two model versions side by side. We see where the new model is better, where it's worse, where it's different.

**SP2:** Step three. Promote the new model to a canary traffic slice. Five percent of traffic. Real production users. Real conversations.

**SP1:** The previous ninety-five percent stays on the baseline. We can't simulate user behavior. We have to measure it.

**SP2:** Step four. Compare live quality, cost, latency, and safety against the baseline. The canary slice produces traces. We run the evaluators on those traces. We measure. We compare.

**SP1:** If the new model is better, we promote. If it's worse, we pause and diagnose.

**SP2:** Step five. Roll forward or roll back, with evidence. The decision is in the artifact. Quality scores. Cost comparison. Latency comparison. Safety findings.

**SP1:** It's not a gut call. It's an evidence-backed decision.

**SP2:** Ownership matters. The AI platform team coordinates the model change. The application team validates against their specific use cases. Both have to sign off.

**SP1:** The platform team makes sure the infrastructure is ready. New deployment, capacity, throttling. The application team makes sure the agent still does what it should.

**SP2:** Canary upgrades are not new to DevOps. We've been doing this for software for years. The reason it feels new for AI is that historically, model upgrades happened invisibly.

**SP1:** The vendor pushed an update, we didn't notice, sometimes we did notice when things broke. With agents in business-critical workflows, that's not acceptable.

**SP2:** If you have the eval dataset and the release contract from earlier slides, the model lifecycle becomes a routine release. Not a crisis. Not a fire drill.

**SP1:** Just another canary, with evidence.

---

## Slide 22 - Section: Adoption

**SP1:** All right. We've covered the foundations, evaluation, CI/CD, observability, and Day-2. That's the operating model.

**SP2:** Now we want to close on adoption. Because the question we get most often, after a session like this, is: where do I start? Start small. Build the pattern.

---

## Slide 23 - Start with one production-candidate agent

**SP2:** Close with a practical adoption path. *Don't start with every agent. Start with one.*

**SP1:** We want to be specific about this, because well-intentioned teams often try to do too much at once, and then nothing actually ships.

**SP2:** Step one - pick one agent. One. Not your portfolio. Not your roadmap. One agent that is close to production today.

**SP1:** Probably one that has a real owner, real users in pilot or about to be, and real business value. Not a sandbox. Not a demo. Something that's actually about to go to production.

**SP2:** Step two - define release criteria and a small eval dataset. Write down the criteria. Minimum quality score. Minimum groundedness. No new harmful content findings.

**SP1:** Build the eval dataset. Even just twenty representative cases. The cases are real user journeys, real edge cases, real things you've already seen the agent get wrong. Twenty is fine for the first iteration.

**SP2:** Step three - wire telemetry, traces, dashboards, and alerts. Application Insights connected. OpenTelemetry spans flowing. Foundry observability turned on.

**SP1:** At least one dashboard for the agent. At least one alert for the worst-case failure mode. Doesn't have to be perfect. Has to exist.

**SP2:** Step four - add PR and deploy gates. The eval runs on PR. The eval runs on deploy. The gate blocks if scores drop.

**SP1:** The first time a developer sees a failed PR because of an eval regression, you'll know it's working.

**SP2:** Step five - review readiness evidence weekly. Pick a thirty-minute meeting. Walk through the eval reports. Walk through the safety findings. Walk through the incidents. Walk through what's going into the eval dataset.

**SP1:** The rhythm is what makes it stick.

**SP2:** Step six - promote production learnings into future evals. Reviewed traces become eval rows. Postmortem findings become regression tests. Red team findings become adversarial coverage.

**SP1:** The dataset grows. The next gate is stronger.

**SP2:** Thirty days. Six steps. One agent. That's how it starts.

**SP1:** The call to action is the quote at the bottom. *Move one agent from "it works in testing" to "we can operate it safely."*

**SP2:** Once you've done that, you have the pattern. The pattern scales across the portfolio without re-litigating every decision.

**SP1:** Thank you for watching. We hope this gave you the operating model to take one agent from prototype to production with confidence.
