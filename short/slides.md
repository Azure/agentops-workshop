---
marp: true
theme: default
paginate: true
header: "Production Readiness Workshop"
footer: "Topic 4 - AgentOps"
style: |
  section.lead h1 {
    font-size: 2.5em;
    text-align: center;
  }
  section.lead h2 {
    text-align: center;
  }
  section.lead {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  table {
    font-size: 0.85em;
  }
  blockquote {
    font-size: 0.9em;
  }
---

<!-- _class: lead -->

# AgentOps
## From Agent Prototype to Production

<!-- Speaker notes: Every team building with GenAI hits the same question - can we safely ship this, and where is the evidence? That is what this session addresses: the operating model for moving AI agents from prototype to production on Microsoft Foundry. The question we keep coming back to is simple - can we safely ship this version of the agent, and where is the evidence? Audience: AI application builders, architects, DevOps and platform teams, AI governance stakeholders, and technical decision makers responsible for production AI systems. Prerequisites in the broader program: Topic 2 (AI Landing Zones) and Topic 3 (Agent Architectures). Let us look at the agenda. -->

---

# Agenda

1. **AgentOps Foundations** - why AI ops is different and the operating loop
2. **Evaluation** - quality, grounding, behavior, and red teaming
3. **CI/CD for Agentic AI** - gates, evidence, and environment promotion
4. **Observability** - traces, correlation, and the closed loop
5. **Day-2 Operations** - incident runbook and model lifecycle
6. **Adoption** - start with one production-candidate agent

<!-- Speaker notes: We have six blocks to cover in one hour - here is how we have structured the story. The flow moves from why agents need a new operating model, through how teams produce release evidence, into how observability and Day-2 operations close the loop. The session ends with a practical 30-day starting path. Let us start with Foundations. -->

---

<!-- _class: lead -->

# AgentOps Foundations
## Why AI operations need a new discipline

---

# The production gap

![Two-column contrast: prototype works vs production needs proof, with arrows showing the shift from manual to evidence-based](images/production-gap.png)

> The bottleneck moved from building the first demo to proving that the next version is safe to release.

<!-- Speaker notes: Teams can stand up a GenAI prototype in days - but getting to production is a different story. That gap between demo and production-ready is what we call the production gap. Teams can build GenAI prototypes quickly. Production introduces new operational risk. The hard questions are no longer about building the first demo - they are about quality, safety, monitoring, cost, ownership, and release confidence. Agents add non-determinism, tool-calling risk, prompt regression, and changing user behavior. So what exactly are we managing? The next slide breaks open the components that make an agent a production concern. -->

---

# Building blocks of a production agent

![Progressive table showing how components and operational surface accumulate from prompts through multi-agent systems](images/anatomy-complexity.png)

> Each tier adds components and complexity. A production agent manages all of these simultaneously.

<!-- Speaker notes: So what exactly makes an agent a production concern? It is not just a prompt and a model - there are layers of capability that each bring their own operational surface. This slide shows the building blocks of a production agent. It combines the anatomy and the complexity story into one visual. At the bottom: simple prompts. You have a system prompt and a model. The operational surface is versioning, quality eval, and cost. Add RAG: now you also manage knowledge sources, freshness, permissions, groundedness. Add tools: now you have MCP servers, guardrails, auth boundaries, side effects, failure modes. Add agent-level autonomy: memory, orchestration, approval points, multi-step traces, loop prevention, escalation. Add multi-agent: orchestrator, sub-agents, emergent behaviour, coordination, cost spikes. The point is not that everyone is doing multi-agent. The point is that even a simple tool-using agent puts you at tier 3, managing all of those components simultaneously. Each one is a versioned asset, an evaluation target, and an operational dependency. So we need a platform that can manage all of this - that is Foundry. Cross-reference: Topic 3 covers agent architectures in detail. So what does Foundry give us as the control plane? -->

---

# Microsoft Foundry is the control plane

![Foundry control plane stack with Surfaces, Capabilities, and Runtime layers](images/foundry-control-plane.png)

> Foundry stays the control plane. AgentOps connects Foundry signals to release decisions and Day-2 action.

<!-- Speaker notes: We have all these components to manage - so we need a platform that orchestrates them. That platform is Microsoft Foundry, and it acts as the control plane. Foundry surfaces include the portal, SDK, Azure CLI / REST, and GitHub Actions. Foundry capabilities cover agents and versions, quality + safety evaluators, agent-specific evaluators, the Red Teaming agent, OpenTelemetry tracing, and Content Safety. The runtime is Azure AI projects, model deployments, tool / MCP servers, plus App Insights and Log Analytics for runtime observability. AgentOps adds the repeatable operating loop around them - it is not a replacement for Foundry. Now that we know the components and the platform, the question becomes: what evidence do we need to prove a version is safe to ship? That is the production readiness checklist. -->

---

# Production readiness checklist

- Target and version are explicit
- Eval dataset and thresholds exist
- CI/CD gate blocks regressions
- Telemetry and traces are wired
- Safety and red-team findings are tracked
- Release evidence is reviewable
- Owners know what to do when signals fail

> The checklist turns "I think it works" into "we have evidence for this release."

<!-- Speaker notes: We know the components and the platform - but how do we know a version is actually safe to ship? That is what the production readiness checklist answers. It is the contract for any production-candidate agent. Every item maps to one or more later slides. Walk the audience through each item briefly so they can hold it as the mental model for the rest of the session. The question is: how do we produce this evidence repeatably, every release, without heroics? That is what the operating model gives us. -->

---

# AgentOps operating model

![Six-step AgentOps loop: Evaluate, Gate, Observe, Diagnose, Ship, Improve, with Foundry as the control plane](images/operating-loop.png)

> People - Process - Platform working as one operating loop. The six steps are the heart of the session.

<!-- Speaker notes: The checklist tells us what evidence we need - the operating model tells us how to produce it repeatably. This is the AgentOps operating model. AgentOps applies DevOps discipline to AI agents, where behavior is probabilistic and releases need evidence. The loop is the heart of the session - everything that follows is one of these six steps. Evaluate pre-prod on golden datasets. Gate at CI/CD with policy thresholds and human approval. Observe traces, metrics, logs, content safety in Foundry plus App Insights. Diagnose root cause via traces and evaluators on production samples. Ship via canary, with model + prompt + tool versioned together. Improve by feeding production learnings into the next evaluation set. The goal is continuous value with controlled operational risk. The output is release evidence and operational confidence. Let us start with the first step in the loop - Evaluation. -->

---

<!-- _class: lead -->

# Evaluation
## The release signal for agentic systems

---

# Evaluation strategy

![Three-stage evaluation timeline: base model selection, pre-production evaluation, post-production monitoring](images/evaluation-three-stages-timeline.png)

> Evaluation is not a one-time score. It is the release signal that grows as production teaches you new failure modes.

<!-- Speaker notes: The first step in the loop is evaluation - because without a quality signal, there is nothing to gate on. Let us talk about evaluation strategy. Start with a small golden dataset tied to real user journeys. Evaluate quality, groundedness, latency, cost, and behavior. Compare against baselines and previous versions. Promote reviewed production traces into future regression cases. The minimum viable evaluation is small but real. A few dozen representative cases beat zero cases. Use Foundry's built-in evaluators for quality, groundedness, and agent metrics like intent resolution and tool call accuracy. The eval dataset is a living artifact - every reviewed production trace can become a new test row. But quality evaluation alone is not enough - we also need to test adversarial scenarios. -->

---

# Red teaming and AI safety

![Red teaming taxonomy: four risk categories (harmful content, jailbreak, hallucination, data exfiltration) plus the four-step probe process](images/red-teaming-taxonomy.png)

> Quality asks "is the answer good?" Red teaming asks "can someone make it misbehave?" Both are required.

<!-- Speaker notes: Quality evaluation tells us if the answer is good - but it will not tell us if someone can make the agent misbehave. That is where red teaming and AI safety come in. Safety and quality are different signals. Quality scoring will not catch a jailbreak. Foundry ships an AI Red Teaming Agent backed by Microsoft's PyRIT framework so teams can automate adversarial testing rather than doing it ad-hoc. Four risk categories: harmful content (hate, violence, sexual, self-harm), jailbreak (prompt injection, role hijacking), hallucination (ungrounded claims, fake citations), and data exfiltration (PII leakage, tool abuse). Cadence: pre-release gate, scheduled weekly, post-incident. Findings feed the eval dataset as adversarial rows for future regression coverage. Now that we have evaluation and red teaming producing signals, how do we enforce them? That brings us to CI/CD gates. -->

---

<!-- _class: lead -->

# CI/CD for Agentic AI
## Gates that enforce release evidence

---

# CI/CD gates for agentic AI

![CI/CD pipeline with evaluation gates: build, evaluate, gate decision, deploy](images/ci-cd-evaluation-gate-pipeline.png)

> The strongest moment is a failed gate. If the prompt regresses, the pipeline stops before users experience it.

<!-- Speaker notes: Evaluation and red teaming produce the signals - but signals without enforcement are just reports nobody reads. CI/CD gates for agentic AI are where DevOps discipline meets agentic systems. PR gates block bad prompts before merge. Deploy gates block bad versions before they reach the next environment. Watchdogs catch drift between releases. Every gate produces an artifact that becomes part of the release evidence: eval report, readiness report, release evidence. With gates enforcing quality, the next question is: what happens after we ship? That is where observability comes in. -->

---

<!-- _class: lead -->

# Observability
## Traces, correlation, and the closed loop

---

# Observability for agents is more than monitoring

![Foundry observability stack with three pillars: tracing, monitoring, continuous evaluation](images/observability-stack-three-pillars.png)

> Infrastructure monitoring asks "is the service healthy?" Agent observability asks "what did it do and why?"

<!-- Speaker notes: Gates enforce quality before release - but what happens once the agent is live? We need to understand what it is doing and why. That is observability for agents, and it is more than traditional monitoring. For agents, the unit of understanding is the trace. We need to see the chain of decisions, not just the endpoint status. Required signals: prompt, plan, model call, retrieval, tool call, safety event, latency, cost, user feedback, release version. Required correlation: trace ID, session ID, agent version, deployment, eval run, incident, owner. Without correlation across version, deployment, eval, and incident, observability is just a set of disconnected dashboards. With correlation, the same trace can answer questions across release, runtime, evaluation, and Day-2 contexts. But signals alone are not the goal - what matters is what you do with them. -->

---

# From telemetry to action

![Trace waterfall plus a signals-to-actions table showing how each telemetry signal triggers a concrete operational response](images/telemetry-to-action.png)

> The end state is not a dashboard. The end state is action: observe, diagnose, add eval case, gate, ship.

<!-- Speaker notes: Collecting signals is not the end goal - what matters is turning those signals into action. From telemetry to action is the connective tissue of the whole session. Telemetry is not the goal - action is. A trace explains a failure. A reviewed trace becomes a new eval row. The new eval row enters the gate. The gate prevents the same failure from reaching production again. Latency spike -> Azure Monitor alert -> on-call. Tool error rate -> disable tool, fall back to manual. Safety violation -> block plus content safety incident. Eval score drop -> pause canary, open ticket. Cost anomaly -> throttle via APIM, notify FinOps. Positive feedback -> sample into eval dataset. This is how observability funds evaluation, and evaluation funds release confidence. That closed loop is what Day-2 operations are built on. -->

---

<!-- _class: lead -->

# Day-2 Operations
## Running agents in production

---

# Day-2 operations - four concerns

![Day-2 quadrant: Reliability + SLOs, Incident response, Model lifecycle, Cost + capacity](images/day2-quadrant.png)

> AgentOps is not done at release. Production traces and red-team findings feed the next evaluation set.

<!-- Speaker notes: Shipping is not the finish line - it is where the real operational work begins. Day-2 operations has four concerns that teams need to own. Day-2 is where most of the operational reality lives - long after the launch demo. Reliability and SLOs: availability, latency, error rate budgets; tool dependency failure modes; graceful degradation. Incident response: runbooks per severity; on-call rotation that knows the agent; postmortems with model plus prompt context. Model lifecycle: canary rollout for upgrades; prompt and tool versioned alongside model; rollback drills. Cost and capacity: PTU vs pay-as-you-go decisions; token and tool call budgets per tenant; alerting on cost anomalies. The four concerns are interlocking, not independent. Each one creates signals that feed back into evaluation and the next release. The next two slides go deeper into incident response and model lifecycle. -->

---

# AI incident runbook

| Severity | Example | First action |
|---|---|---|
| S1 Critical | Safety event or data leak in production | Stop gate, rollback to last good version |
| S2 High | Quality or grounding regression after deploy | Planned rollback or version pin |
| S3 Medium | Latency degradation or cost spike | Rate-limit, investigate, then act |
| S4 Low | Drift indicator on a single metric | Schedule analysis in the next eval cycle |

Triage flow:
**Detect -> Correlate trace -> Identify version -> Contain -> Analyze -> Fix -> Re-evaluate -> Close with evidence**

> Containment first. Evidence-backed fix second.

<!-- Speaker notes: When something goes wrong in production, you need a structured response - not a fire drill. That is what the AI incident runbook provides. When an agent misbehaves in production, the runbook turns a fire drill into a sequence. The severity table sets expectations so teams do not over-react or under-react. The triage flow makes containment explicit - stop the bleed before debugging. Every closed incident produces evidence that updates the eval dataset, the gate criteria, or the operating model. The other recurring Day-2 challenge is model lifecycle - let us look at that next. -->

---

# Model lifecycle and canary upgrades

![Model lifecycle and canary upgrade process through an API gateway](images/model-lifecycle-upgrade-process.png)

> Treat every model change as a release candidate, not a config flip.

<!-- Speaker notes: The other recurring Day-2 challenge is when the model itself changes - deprecation, new versions, cost pressure. That is model lifecycle and canary upgrades. Model lifecycle is the recurring pain point we hear from customers - "the model we depend on is being deprecated, what now?" The answer is the same gates and evidence as any other release candidate. Triggers: deprecation, new model availability, cost or performance pressure, vendor change. Canary process: pin current model version as baseline; run new model against the eval dataset offline; promote to a canary traffic slice; compare live quality, cost, latency, safety against baseline; roll forward or roll back with evidence. Ownership: AI platform team coordinates, application team validates. Canary upgrades are not new to DevOps, but they map cleanly to model changes if the eval dataset and release contract are already in place. So we have covered the full loop - now the question is: where do you start? -->

---

<!-- _class: lead -->

# Adoption
## Start small, build the pattern

---

# Maturity model

![AgentOps maturity ribbon with four levels: Initial, Defined, Managed, Optimised](images/maturity-ribbon.png)

> Most teams sit between Initial and Defined. Start by moving one production-candidate agent up one level.

<!-- Speaker notes: We have covered the full operating loop - the question now is where does your team sit today? This maturity model provides a quick self-assessment. Where is your team right now? Initial: ad hoc demos, manual eval, no gates, scattered logs. Defined: versioned prompts and agents, pre-prod eval datasets, CI builds artefacts. Managed: quality and safety gates in CI, continuous evaluation in production, runbooks and SLOs. Optimised: drift and cost guardrails, canary plus auto-rollback, feedback flywheel. The practical move is not to boil the ocean. Pick one production-candidate agent and move it up one level. Here is a concrete 30-day starting path. -->

---

# Start with one production-candidate agent

30-day start:

1. **Pick one agent** that is close to production
2. Define **release criteria** and a small **eval dataset**
3. Wire **telemetry, traces, dashboards, alerts**
4. Add **PR and deploy gates**
5. Review **readiness evidence** weekly
6. Promote **production learnings** into future evals

> Move one agent from "it works in testing" to "we can operate it safely."

<!-- Speaker notes: You do not need to boil the ocean - the practical move is to start with one production-candidate agent and build the repeatable pattern. Here is a 30-day adoption path. Do not start with every agent. Start with one production-candidate agent and build the repeatable pattern. Once the pattern is proven on one agent, it scales across the portfolio without re-litigating every decision. Thank you - we are happy to take questions. -->
