---
title: Slide Plan
layout: default
parent: 1-Hour Session
nav_order: 3
---

# 1-Hour Slide Plan

## Recommendation

Use the GenAIOps deck as conceptual source material, not as the session structure. The original deck is training-oriented and too large for a 1-hour delivery.

The session should be a focused **AgentOps / production readiness** story:

> Agents are moving from prototypes to production. AgentOps provides the operating model for evaluation, release gates, observability, diagnostics, safety, governance, and continuous improvement on Microsoft Foundry.

Observability should be a visible section of the deck, not a single bullet. AgentOps Toolkit may appear as one practical implementation component in the demo, but the deck should not be framed around the toolkit.

## Proposed 16-slide deck

### Slide 1 - From Agent Prototype to Production

**Purpose:** Open with the production-readiness promise.

**On-slide content:**

- From successful prototypes to production-ready agents
- Evaluation, gates, observability, and readiness evidence
- Built around Microsoft Foundry and Azure operations

**Speaker cue:** "This is the operating model for answering a simple production question: can we safely ship this agent?"

**Visual idea:** Dark title slide with a lifecycle ribbon: Prototype -> Evaluate -> Gate -> Observe -> Improve.

**Source mapping:** GenAIOps title/agenda material plus AgentOps session abstract.

---

### Slide 2 - The production gap for GenAI and agents

**Purpose:** Create urgency.

**On-slide content:**

- Teams can build GenAI prototypes quickly, but production introduces new risk.
- The hard questions are operational: quality, safety, monitoring, cost, ownership, and release confidence.
- Agents add non-determinism, tool-calling risk, prompt regression, and changing user behavior.

**Speaker cue:** "The bottleneck moved from building the first demo to proving that the next version is safe to release."

**Visual idea:** Two-column contrast: "Prototype works" vs. "Production needs proof".

**Source mapping:** GenAIOps adoption-friction material.

---

### Slide 3 - Complexity increases from prompts to agents

**Purpose:** Explain why traditional DevOps/MLOps practices need to evolve for agentic systems.

**On-slide content:**

- Simple prompts: quality and cost tradeoffs
- RAG applications: grounding, retrieval quality, data freshness, permissions
- Agents: planning, tools, memory, orchestration, multi-step failure modes
- Multi-agent systems: coordination, traceability, and governance complexity

**Speaker cue:** "The more autonomous the system becomes, the more we need repeatable evidence, not manual confidence."

**Visual idea:** Stair-step complexity ladder from prompt to RAG to agent to multi-agent.

**Source mapping:** GenAIOps complexity-levels material.

---

### Slide 4 - AgentOps operating model

**Purpose:** Define the framework.

**On-slide content:**

- AgentOps brings people, process, and platform together for production AI agents.
- The operating loop: **Evaluate, Gate, Observe, Diagnose, Ship, Improve**.
- The goal: continuous value with controlled operational risk.
- The output: release evidence and operational confidence.

**Speaker cue:** "AgentOps is how teams apply DevOps discipline to AI agents, where behavior is probabilistic and releases need evidence."

**Visual idea:** Center triangle People / Process / Platform with the AgentOps loop around it.

**Source mapping:** GenAIOps people/process/platform and operating-model content.

---

### Slide 5 - Enterprise lifecycle: build, augment, operationalize, manage

**Purpose:** Preserve the strongest lifecycle concept from the original deck, but use it only once.

**On-slide content:**

- Ideate and explore: use case, model, prompt, data
- Build and augment: RAG, tools, orchestration, safety
- Operationalize: deploy, evaluate, monitor, alert
- Manage: governance, security, compliance, cost

**Speaker cue:** "The lifecycle is not linear. Production systems loop through these stages continuously."

**Visual idea:** Circular lifecycle with an outer management and governance ring.

**Source mapping:** GenAIOps lifecycle slides.

---

### Slide 6 - Maturity model: where most teams are today

**Purpose:** Help customers self-assess quickly.

**On-slide content:**

| Level | What it looks like |
|---|---|
| Initial | Manual testing, ad-hoc prompts, limited telemetry |
| Defined | Standard datasets, documented release criteria |
| Managed | CI/CD gates, monitoring, ownership, incident response |
| Optimized | Continuous evals, trace learning, red-team cadence, cost optimization |

**Speaker cue:** "Most teams are between Initial and Defined. The practical move is not to boil the ocean; it is to pick one agent and add release evidence."

**Visual idea:** Four-level maturity ladder with a marker: "Start here: one production-candidate agent."

**Source mapping:** GenAIOps maturity model content.

---

### Slide 7 - Microsoft Foundry is the control plane

**Purpose:** Clarify where AgentOps fits.

**On-slide content:**

- Foundry: agent lifecycle, models, evaluation, tracing, safety, governance
- Azure Monitor / Application Insights: runtime telemetry, traces, alerts, health
- AgentOps: operating practices across repo, CI/CD, readiness checks, release evidence, and continuous improvement

**Speaker cue:** "Foundry remains the control plane. AgentOps connects Foundry signals to release decisions and Day-2 action."

**Visual idea:** Layered architecture: Foundry control plane at center, Azure Monitor on the operate side, repo/CI/CD/evidence loop around it.

**Source mapping:** GenAIOps Azure AI Foundry and monitoring material; AgentOps end-to-end tutorial control-plane framing.

---

### Slide 8 - Production readiness checklist

**Purpose:** Give customers a concrete checklist.

**On-slide content:**

Before release, prove:

- Target/version is explicit
- Eval dataset and thresholds exist
- CI/CD gate blocks regressions
- Telemetry and traces are wired
- Safety and red-team findings are tracked
- Release evidence exists for review
- Owners know what to do when signals fail

**Speaker cue:** "The checklist turns 'I think it works' into 'we have evidence for this release.'"

**Visual idea:** Readiness checklist card with green/yellow/red status tags.

**Source mapping:** GenAIOps best-practices and challenges content; AgentOps end-to-end completion checklist.

---

### Slide 9 - Evaluation strategy: quality, safety, and behavior

**Purpose:** Make evaluation the first-class production practice.

**On-slide content:**

- Start with a small golden dataset tied to real user journeys.
- Evaluate quality, groundedness, safety, latency/cost, and agent behavior.
- Compare against baselines and previous versions.
- Promote reviewed production traces into future regression candidates.

**Speaker cue:** "Evaluation is not a one-time score. It is the release signal that grows as production teaches you new failure modes."

**Visual idea:** Dataset -> eval run -> metrics -> baseline comparison -> regression candidates.

**Source mapping:** GenAIOps evaluation and safety slides.

---

### Slide 10 - CI/CD gates for agentic AI

**Purpose:** Show DevOps discipline applied to agents.

**On-slide content:**

- PR gate: evaluate candidate changes before merge
- Deploy gate: validate target version before environment promotion
- Watchdog: scheduled readiness checks
- Artifacts: eval report, readiness report, release evidence

**Speaker cue:** "The strongest moment is a failed gate. If the prompt regresses, the pipeline stops before users experience it."

**Visual idea:** Pipeline lane with PR -> Dev -> QA -> Prod and quality gates in between.

**Source mapping:** GenAIOps CI/CD content and AgentOps end-to-end workflow generation.

---

### Slide 11 - Observability for agents is more than monitoring

**Purpose:** Deepen the observability message.

**On-slide content:**

- Infrastructure monitoring answers: is the service healthy?
- Agent observability answers: what did the agent do, why, and what changed?
- Required signals: prompt, plan, model call, retrieval, tool call, safety event, latency, cost, user feedback, release version
- Required correlation: trace ID, session ID, agent version, deployment, eval run, incident, owner

**Speaker cue:** "For agents, the unit of understanding is the trace. We need to see the chain of decisions, not just the endpoint status."

**Visual idea:** Trace waterfall: user request -> reasoning/plan -> model call -> retrieval -> tool call -> response -> feedback.

**Source mapping:** GenAIOps monitoring and observability material; Foundry tracing concepts.

---

### Slide 12 - From telemetry to action

**Purpose:** Show how observability feeds the operating loop.

**On-slide content:**

- Dashboards show quality, safety, latency, cost, errors, and adoption.
- Alerts route runtime failures to owners.
- Traces explain failures and regressions.
- Reviewed traces become new eval rows.
- Release evidence links telemetry back to the shipped version.

**Speaker cue:** "The end state is not a dashboard. The end state is action: fix the issue, update the eval set, and prevent the same failure from reaching production again."

**Visual idea:** Closed loop: Observe -> Diagnose -> Add eval case -> Gate -> Release evidence -> Observe.

**Source mapping:** GenAIOps monitoring and operations content; AgentOps tutorial trace learning sections.

---

### Slide 13 - Demo video: end-to-end release readiness

**Purpose:** Play the video and make the operating model tangible.

**On-slide content:**

Demo story:

1. Foundry Travel Agent target exists
2. Repo release contract is configured
3. Eval runner is selected
4. A deliberate regression fails the gate
5. The fix passes the same gate
6. Readiness evidence summarizes the release
7. Observability links traces, telemetry, and next actions

**Speaker cue:** "Watch for the failure. That is the production value: the gate catches a real regression and gives the team evidence to act."

**Visual idea:** Horizontal storyboard with seven numbered frames and a play button.

**Source mapping:** `C:\Users\paulolacerda\workspace\agentops\docs\tutorial-end-to-end.md`.

**Subtle component note:** AgentOps Toolkit can be used in the recording for CLI, Doctor, and Cockpit because those components make the AgentOps practices concrete.

---

### Slide 14 - What the demo proved

**Purpose:** Convert the demo into takeaways.

**On-slide content:**

- Foundry is the control plane for the agent.
- AgentOps creates a release-readiness loop.
- Evals create comparable evidence across versions.
- CI/CD gates block regressions.
- Observability explains runtime behavior and drives future evals.
- Diagnostics and evidence connect signals to next actions.

**Speaker cue:** "The demo is not about commands. It proves the operating loop: evaluate, gate, observe, diagnose, ship, improve."

**Visual idea:** Six proof cards: Control plane, Contract, Evidence, Gate, Observability, Operations.

**Source mapping:** GenAIOps benefits/key-takeaways content and AgentOps tutorial evidence sections.

---

### Slide 15 - Day-2 operations: observe, govern, and improve

**Purpose:** Keep monitoring, governance, safety, and cost visible without turning them into separate deep dives.

**On-slide content:**

- Observability: traces, metrics, alerts, health, latency, errors, feedback
- Governance: owners, RBAC, auditability, release evidence
- Safety: content safety, red-team scans, adversarial eval rows
- Cost: model usage, gateway controls, budgets, optimization

**Speaker cue:** "AgentOps is not done when the release ships. Production traces, red-team findings, and cost signals feed the next evaluation set."

**Visual idea:** Four quadrants: Observe, Govern, Protect, Optimize.

**Source mapping:** GenAIOps monitoring, gateway, governance, safety, and cost content.

---

### Slide 16 - Start with one production-candidate agent

**Purpose:** Close with a practical adoption path.

**On-slide content:**

30-day start:

1. Pick one agent that is close to production.
2. Define release criteria and a small eval dataset.
3. Wire telemetry, traces, dashboards, and alerts.
4. Add PR and deploy gates.
5. Review readiness evidence weekly.
6. Promote production learnings into future evals.

**CTA:** "Move one agent from 'it works in testing' to 'we can operate it safely.'"

**Speaker cue:** "Do not start with every agent. Start with one production-candidate agent and build the repeatable pattern."

**Visual idea:** 30-day roadmap with week 1, week 2, week 3, week 4.

**Source mapping:** GenAIOps key-takeaways content and AgentOps adoption blueprint.

## What to preserve from the GenAIOps deck

| Preserve | How to use it |
|---|---|
| POC-to-production gap | Use as the opening problem. |
| People/process/platform | Use to define AgentOps operating discipline. |
| Non-linear lifecycle | Keep one lifecycle slide only. |
| Maturity model | Use as a quick self-assessment. |
| Evaluation | Make it the core release signal. |
| Red teaming and safety | Keep visible as enterprise requirements. |
| AI gateway / APIM | Mention as part of production controls; move details to appendix if needed. |
| Observability and tracing | Give it a dedicated section and connect it to trace learning. |
| Governance and cost | Collapse into Day-2 operations. |

## What to cut or move to appendix

| Original content | Recommendation |
|---|---|
| Full agenda and training logistics | Cut from the 1-hour deck. |
| Repeated lifecycle slides | Keep only one lifecycle slide. |
| Deep model catalog walkthrough | Appendix or verbal mention only. |
| Detailed model comparison | Merge into the complexity or evaluation discussion. |
| Step-by-step RAG build slides | Appendix; not central to the AgentOps 1-hour session. |
| Full deployment option comparison | Appendix. |
| Multiple generic monitoring slides | Replace with two focused observability slides. |
| Detailed APIM policy/gateway walkthrough | Appendix or separate technical session. |
| Long governance/cost details | Collapse into Day-2 operations. |
