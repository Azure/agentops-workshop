---
title: Slide Plan
layout: default
parent: Short Workshop
nav_order: 3
---

# Short Workshop Slide Plan

## Recommendation

Use the GenAIOps deck as conceptual source material, not as the session structure. The original deck is training-oriented and too large for a short (~1-hour) delivery.

The session is a focused **AgentOps / production readiness** story:

> Agents are moving from prototypes to production. AgentOps provides the operating model for evaluation, release gates, observability, diagnostics, safety, governance, and continuous improvement on Microsoft Foundry.

Observability is a dedicated section of the deck, not a single bullet. The deck stands on its own as a short (~1-hour) webinar. An optional backup video can be recorded for specific deliveries, but the slides do not depend on it.

## Section taxonomy (parent program alignment)

The deck is organized to align with the parent program's six AgentOps sections, with a title and agenda up front and a section divider opening each major block:

| Block | Slides | Includes |
|---|---|---|
| Opening | 1-2 | Title, Agenda |
| AgentOps Foundations | 3-9 | Section divider + 6 content slides |
| Evaluation | 10-12 | Section divider + 2 content slides |
| CI/CD for Agentic AI | 13-14 | Section divider + 1 content slide |
| Observability | 15-17 | Section divider + 2 content slides |
| Day-2 Operations | 18-21 | Section divider + 3 content slides |
| Adoption / Close | 22-23 | Section divider + 1 content slide |

The Agent Development Lifecycle section is consciously deferred to the long workshop.

## Deck structure (23 slides)

The deck has 16 content slides plus 7 structural slides (1 title, 1 agenda, 5 section dividers and 1 closing divider). Lead/divider slides are short visual respites - useful as live presentation transitions and as chapter markers for video editing.

### Slide 1 - Title (lead): AgentOps - From Agent Prototype to Production

**Purpose:** Open with the production-readiness promise.

**On-slide content:**

- AgentOps
- From Agent Prototype to Production

**Speaker cue:** "This is the operating model for answering a simple production question: can we safely ship this agent?"

**Visual idea:** Dark title slide with a lifecycle ribbon: Prototype -> Evaluate -> Gate -> Observe -> Improve.

**Source mapping:** GenAIOps title/agenda material plus AgentOps session abstract.

**Status:** New (narrative framing).

---

### Slide 2 - Agenda

**Purpose:** Set the six-block flow so the audience can hold the structure in mind.

**On-slide content:**

1. AgentOps Foundations
2. Evaluation
3. CI/CD for Agentic AI
4. Observability
5. Day-2 Operations
6. Adoption

**Speaker cue:** "Six concise blocks for one hour. The story flows from why agents need a new operating model into how teams produce release evidence, observability, and Day-2 discipline."

**Visual idea:** Numbered list with subtle progress dots.

**Status:** New structural slide.

---

### Slide 3 - Section divider: AgentOps Foundations

**Purpose:** Open the Foundations block.

**On-slide content:**

- AgentOps Foundations
- Why AI operations need a new discipline

**Speaker cue:** Brief pause to signal the first section.

**Status:** New structural divider.

---

### Slide 4 - The production gap

**Purpose:** Create urgency.

**On-slide content:**

- Two-column contrast table: "Prototype works" vs. "Production needs proof".
- Pull-quote: "The bottleneck moved from building the first demo to proving that the next version is safe to release."

**Speaker cue:** "The bottleneck moved from building the first demo to proving that the next version is safe to release."

**Visual idea:** Clean comparison table; no chart.

**Source mapping:** GenAIOps PoC-to-production / adoption-friction material (slide 9).

**Status:** Direct reuse from GenAIOps.

---

### Slide 5 - Complexity from prompts to agents

**Purpose:** Explain why traditional DevOps and MLOps practices need to evolve for agentic systems.

**On-slide content:**

- Stair-step ladder diagram (`images/complexity-ladder.png`)
- Simple prompts -> RAG -> Tool-using agents -> Single agents -> Multi-agent
- Pull-quote: "The more autonomous the system, the more we need repeatable evidence."

**Speaker cue:** "The more autonomous the system becomes, the more we need repeatable evidence, not manual confidence."

**Visual idea:** Stair-step complexity ladder (matplotlib).

**Source mapping:** GenAIOps complexity-levels content (slide 6).

**Status:** Direct reuse - new visual.

---

### Slide 6 - AgentOps operating model

**Purpose:** Define the framework.

**On-slide content:**

- Six-step loop visual (`images/operating-loop.png`)
- Evaluate -> Gate -> Observe -> Diagnose -> Ship -> Improve
- Pull-quote: "People - Process - Platform working as one operating loop."

**Speaker cue:** "AgentOps is how teams apply DevOps discipline to AI agents, where behavior is probabilistic and releases need evidence."

**Visual idea:** Center triangle People / Process / Platform with the AgentOps loop around it.

**Source mapping:** GenAIOps people/process/platform; AgentOps signature loop.

**Status:** New (the operating loop is the session's identity).

---

### Slide 7 - Maturity model

**Purpose:** Help customers self-assess quickly.

**On-slide content:**

- Four-level ribbon (`images/maturity-ribbon.png`): Initial, Defined, Managed, Optimised
- Pull-quote: "Most teams sit between Initial and Defined."

**Speaker cue:** "Most teams are between Initial and Defined. The practical move is not to boil the ocean; it is to pick one agent and add release evidence."

**Visual idea:** Four-level maturity ribbon with a marker: "Start here: one production-candidate agent."

**Source mapping:** GenAIOps maturity model (slides 14-15).

**Status:** Direct reuse - new visual.

---

### Slide 8 - Microsoft Foundry is the control plane

**Purpose:** Clarify where AgentOps fits.

**On-slide content:**

- Stacked layer diagram (`images/foundry-control-plane.png`): Surfaces, Capabilities, Runtime
- Pull-quote: "Foundry stays the control plane. AgentOps connects Foundry signals to release decisions and Day-2 action."

**Speaker cue:** "Foundry remains the control plane. AgentOps connects Foundry signals to release decisions and Day-2 action."

**Visual idea:** Layered architecture.

**Source mapping:** GenAIOps Azure AI Foundry and monitoring material; AgentOps tutorial control-plane framing.

**Status:** Adaptation.

---

### Slide 9 - Production readiness checklist

**Purpose:** Give customers a concrete release-evidence contract.

**On-slide content:**

- Bullet list (7 items): target/version, eval dataset, CI/CD gate, telemetry, safety findings, release evidence, ownership
- Pull-quote: "The checklist turns 'I think it works' into 'we have evidence for this release.'"

**Speaker cue:** "These items turn 'I think it works' into 'we have evidence for this release.'"

**Visual idea:** Readiness checklist card with status tags.

**Source mapping:** GenAIOps best-practices content; AgentOps tutorial completion checklist.

**Status:** New (signature consolidation slide).

---

### Slide 10 - Section divider: Evaluation

**Purpose:** Open the Evaluation block.

**On-slide content:**

- Evaluation
- The release signal for agentic systems

**Speaker cue:** Brief pause; signal the shift from foundations to evidence production.

**Status:** New structural divider.

---

### Slide 11 - Evaluation strategy

**Purpose:** Make evaluation the first-class release signal.

**On-slide content:**

- Three-stage timeline (`images/evaluation-three-stages-timeline.png`): base model selection -> pre-production eval -> post-production monitoring
- Pull-quote: "Evaluation is not a one-time score."

**Speaker cue:** "Evaluation is not a one-time score. It is the release signal that grows as production teaches you new failure modes."

**Visual idea:** Dataset -> eval run -> metrics -> baseline comparison -> regression candidates.

**Source mapping:** GenAIOps evaluation slides 32-34.

**Status:** Adaptation - upstream PNG reused.

---

### Slide 12 - Red teaming and AI safety

**Purpose:** Separate safety from quality. Reach governance, security, and compliance stakeholders.

**On-slide content:**

- Four-quadrant risk taxonomy + probe process (`images/red-teaming-taxonomy.png`)
- Risk categories: harmful content, jailbreak, hallucination, data exfiltration
- Pull-quote: "Quality asks 'is the answer good?' Red teaming asks 'can someone make it misbehave?'"

**Speaker cue:** "Quality and safety are different signals. Both are required before release."

**Visual idea:** Two-axis taxonomy with the Foundry AI Red Teaming Agent (PyRIT) anchored to the four-step probe cycle.

**Source mapping:** GenAIOps slide 38 (PyRIT / AI Red Teaming Agent), slide 42 (Content Safety).

**Status:** Direct reuse plus new framing.

---

### Slide 13 - Section divider: CI/CD for Agentic AI

**Purpose:** Open the CI/CD block.

**On-slide content:**

- CI/CD for Agentic AI
- Gates that enforce release evidence

**Speaker cue:** Brief pause; signal the move to pipeline discipline.

**Status:** New structural divider.

---

### Slide 14 - CI/CD gates for agentic AI

**Purpose:** Show DevOps discipline applied to agents.

**On-slide content:**

- Pipeline diagram (`images/ci-cd-evaluation-gate-pipeline.png`): build -> evaluate -> gate decision -> deploy
- Pull-quote: "The strongest moment is a failed gate."

**Speaker cue:** "The strongest moment is a failed gate. If the prompt regresses, the pipeline stops before users experience it."

**Visual idea:** Pipeline lane with PR -> Dev -> QA -> Prod and quality gates between.

**Source mapping:** GenAIOps CI/CD content (slides 48, 50, 52); AgentOps end-to-end workflow generation.

**Status:** Adaptation - upstream PNG reused.

---

### Slide 15 - Section divider: Observability

**Purpose:** Open the Observability block.

**On-slide content:**

- Observability
- Traces, correlation, and the closed loop

**Speaker cue:** Brief pause; signal the move from release-time gates to runtime evidence.

**Status:** New structural divider.

---

### Slide 16 - Observability for agents is more than monitoring

**Purpose:** Deepen the observability message.

**On-slide content:**

- Three-pillar stack (`images/observability-stack-three-pillars.png`): tracing, monitoring, continuous evaluation
- Pull-quote: "Infrastructure monitoring asks 'is the service healthy?' Agent observability asks 'what did it do and why?'"

**Speaker cue:** "For agents, the unit of understanding is the trace. We need to see the chain of decisions, not just the endpoint status."

**Visual idea:** Trace waterfall.

**Source mapping:** GenAIOps monitoring slide 58; Foundry tracing concepts.

**Status:** Adaptation.

---

### Slide 17 - From telemetry to action

**Purpose:** Show how observability feeds the operating loop.

**On-slide content:**

- Waterfall + signals-to-actions table (`images/telemetry-to-action.png`)
- Pull-quote: "The end state is not a dashboard. The end state is action."

**Speaker cue:** "The end state is not a dashboard. The end state is action: fix the issue, update the eval set, and prevent the same failure from reaching production again."

**Visual idea:** Closed loop: Observe -> Diagnose -> Add eval case -> Gate -> Release evidence -> Observe.

**Source mapping:** GenAIOps monitoring and operations content; AgentOps tutorial trace learning.

**Status:** New (closed-loop framing).

---

### Slide 18 - Section divider: Day-2 Operations

**Purpose:** Open the Day-2 block.

**On-slide content:**

- Day-2 Operations
- Running agents in production

**Speaker cue:** Brief pause; signal the shift to post-release operating reality.

**Status:** New structural divider.

---

### Slide 19 - Day-2 operations - four concerns

**Purpose:** Open the Day-2 deep dive with the four ongoing concerns.

**On-slide content:**

- Four-quadrant diagram (`images/day2-quadrant.png`): Reliability + SLOs, Incident response, Model lifecycle, Cost + capacity
- Pull-quote: "AgentOps is not done at release."

**Speaker cue:** "AgentOps is not done when the release ships. Production traces, red-team findings, and cost signals feed the next evaluation set."

**Visual idea:** Four quadrants with cross-cutting arrows.

**Source mapping:** GenAIOps monitoring, gateway, governance, safety, and cost content.

**Status:** Adaptation.

---

### Slide 20 - AI incident runbook

**Purpose:** Make Day-2 operations tangible with a concrete response pattern.

**On-slide content:**

- Severity table (S1-S4 with example + first action)
- Triage flow: Detect -> Correlate trace -> Identify version -> Contain -> Analyze -> Fix -> Re-evaluate -> Close with evidence
- Pull-quote: "Containment first. Evidence-backed fix second."

**Speaker cue:** "When an agent misbehaves in production, the runbook turns a fire drill into a sequence. Containment first, evidence-backed fix second."

**Visual idea:** Severity table on the left, eight-step triage flow on the right.

**Source mapping:** New content. Cross-reference: AgentOps end-to-end tutorial incident handling notes.

**Status:** New.

---

### Slide 21 - Model lifecycle and canary upgrades

**Purpose:** Address the recurring "model X is deprecated, what now?" pain.

**On-slide content:**

- Lifecycle diagram (`images/model-lifecycle-upgrade-process.png`)
- Pull-quote: "Treat every model change as a release candidate, not a config flip."

**Speaker cue:** "Model lifecycle is not a one-off event. The same gates apply to every model change."

**Visual idea:** Timeline: pinned baseline -> offline eval -> 5% canary -> 50% canary -> full rollout.

**Source mapping:** GenAIOps slide 17 (model and version update), slides 22-24 (model selection).

**Status:** Adaptation plus new canary detail.

---

### Slide 22 - Section divider: Adoption

**Purpose:** Open the closing block.

**On-slide content:**

- Adoption
- Start small, build the pattern

**Speaker cue:** Brief pause before the practical call to action.

**Status:** New structural divider.

---

### Slide 23 - Start with one production-candidate agent

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

**Visual idea:** 30-day roadmap with week 1-4 markers.

**Source mapping:** GenAIOps key-takeaways content and AgentOps adoption blueprint.

**Status:** Direct reuse - new framing.

## Content creation effort (16 content slides)

| Status | Count | Slides |
|---|---:|---|
| Direct reuse from GenAIOps | 4 | 4, 5, 7, 23 |
| Adaptation (partial overlap) | 7 | 8, 11, 12, 14, 16, 19, 21 |
| New content | 5 | 1, 6, 9, 17, 20 |

Structural slides (title, agenda, dividers) - slides 2, 3, 10, 13, 15, 18, 22 - are all new.

## Coverage by section (content slides only)

| Section | Content slides | Share of content slides |
|---|---|---:|
| Opening (title only) | 1 | 6% |
| AgentOps Foundations | 4, 5, 6, 7, 8, 9 | 38% |
| Agent Development Lifecycle | (none) | 0% - deferred to long workshop |
| Evaluation | 11, 12 | 12% |
| CI/CD for Agentic AI | 14 | 6% |
| Observability | 16, 17 | 12% |
| Day-2 Operations | 19, 20, 21 | 19% |
| Closing | 23 | 6% |

## What to preserve from the GenAIOps deck

| Preserve | How to use it |
|---|---|
| PoC-to-production gap | Opening problem (slide 4). |
| People/process/platform | Define AgentOps operating discipline (slide 6). |
| Maturity model | Quick self-assessment (slide 7). |
| Evaluation framework | Core release signal (slide 11). |
| Red teaming and content safety | Dedicated slide in the evaluation block (slide 12). |
| Observability and tracing | Dedicated section connected to trace learning (slides 16-17). |
| Governance and cost | Day-2 quadrant (slide 19). |
| Model lifecycle | Dedicated slide in Day-2 with canary upgrade flow (slide 21). |
| AI gateway / APIM | Mention as part of production controls; appendix if needed. |

## What to cut or move to appendix

| Original content | Recommendation |
|---|---|
| Full agenda and training logistics | Cut from the short deck. |
| Repeated lifecycle slides | Keep only the operating loop; cut the four-phase enterprise lifecycle. |
| Deep model catalog walkthrough | Appendix or verbal mention only. |
| Detailed model comparison | Merge into the complexity or evaluation discussion. |
| Step-by-step RAG build slides | Appendix; not central to the AgentOps short workshop. |
| Full deployment option comparison | Appendix. |
| Multiple generic monitoring slides | Replaced by two focused observability slides (16-17). |
| Detailed APIM policy/gateway walkthrough | Appendix or separate technical session. |
| Long governance/cost details | Collapsed into Day-2 operations. |
| Embedded demo video and recap slides | Demo is optional / appendix; the deck stands on its own. |
