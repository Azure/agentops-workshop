# MS Build 2026 - AgentOps Deck Cross-Check

Source: [Microsoft Build 2026 Recap - All AI Announcements](https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/)

---

## High-priority incorporations (directly strengthen existing slides)

| Build 2026 Announcement | Our slide/section | Recommended change |
|---|---|---|
| **Agent Control Specification (ACS)** - open spec with 8 runtime interception points (startup, input, pre/post-model-call, pre/post-tool-call, output, shutdown). Published under Agent Governance Toolkit on GitHub. Works across Foundry, MAF, LangChain. | CI/CD Gates + Day-2 | Mention ACS as the policy-as-code layer that enforces gates at runtime, not just in CI. Pairs with ASSERT for policy-driven evaluation. |
| **Adaptive Evaluations** (preview) - converts policies into automated tests for agent behaviour | Evaluation Strategy | Name-drop as Foundry's new mechanism for automating eval from policies. Strengthens our "eval dataset is a living artifact" message. |
| **Hosted Agents GA** - hypervisor isolation, per-agent Entra ID, **built-in OpenTelemetry tracing**, built-in content safety, source-deploy via `azd` | Foundry Control Plane + Observability | Update the Foundry capabilities bullet to show tracing is now built-in (not bolted on). Strengthens our observability narrative - "the platform ships with OTel by default." |
| **Copilot Credits** ($0.01/credit pay-as-you-go or prepaid packs) - the named consumption meter for agent work | Day-2 Operations (Cost quadrant) | The consumption meter now has a name. Our cost bullet should reference "Copilot Credits" and the fact that a poorly-scoped agent that loops is now a cost event, not just a quality event. |
| **Agent Optimizer** (preview) - closed-loop: eval -> auto-generate better instructions -> rank -> deploy winner | Operating Model (Improve step) | Perfect proof point for the "Improve" step of our loop. One sentence in speaker notes. |
| **Microsoft Agent Framework 1.0 GA** - agent harness with skills, context, memory, middleware as production-ready building blocks | Building blocks slide | Validates our tier model. Worth a speaker note: "MAF 1.0 went GA at Build - the harness concept formalises what we show on this slide." |

---

## Medium-priority (strengthen narrative without new slides)

| Announcement | Opportunity |
|---|---|
| **Agent 365** (observe / govern / secure umbrella, SDK GA free + framework-agnostic) | Add as the governance layer reference on our safety/red-teaming slide. Agent 365 is where runtime governance lives across Foundry, MAF, and LangChain. |
| **ASSERT** (Agent Security and Safety Evaluation Run-Time) | Pairs with ACS. Worth a speaker note on the red teaming slide: "Foundry now ships ASSERT for policy-driven safety evaluation." |
| **Procedural memory** (preview - agents learn "how" across runs) | Relevant to our Improve step and potentially the building blocks slide (adds a new operational surface). |
| **Frontier Tuning** (RL-based model customisation within compliance boundary) | Strengthens our model lifecycle slide: beyond swapping models, enterprises can now tune within their boundary. Speaker note addition. |
| **Foundry Toolkit for VS Code (GA)** - debug with trace visualisation | Strengthens our observability "inner loop" narrative. Developers can see traces locally before shipping. |
| **Agent ROI dashboard** in Foundry | Good proof point for "telemetry to action" slide - Foundry now shows ROI metrics natively. |

---

## Low-priority / out of scope for short deck

- Microsoft IQ / Web IQ (grounding layer - more of a Topic 3 / architecture concern)
- Microsoft Scout / Autopilots (consumer product, not our audience's build concern)
- Project Solara (device form factors - irrelevant to ops)
- Windows Agent Runtime / MXC (endpoint containment - IT admin concern, not builder ops)
- MAI model family / GPT-5.5 pricing (model catalogue, not operations)
- Surface hardware / NVIDIA collaboration
- Rayfin / Fabric Data Warehouse GPU acceleration

---

## Recommended action

The highest-value updates are:

1. **ACS** on the CI/CD gates slide (speaker notes + possibly one bullet)
2. **Copilot Credits** named on the Day-2 cost quadrant (speaker notes)
3. **Adaptive Evaluations** on the evaluation slide (speaker notes)
4. **Built-in OTel tracing** on the observability slide (validates our message)
5. **Agent Optimizer** on the operating model slide under "Improve" (speaker notes)

These are all speaker-note-level updates that strengthen credibility with "this just shipped at Build" without requiring new slides or restructuring.

---

## Key references

- [Microsoft Build Live (replaces Book of News)](https://news.microsoft.com/build-2026-live-blog)
- [Microsoft Foundry Build 2026 recap](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026)
- [Agent Control Specification (Command Line blog)](https://commandline.microsoft.com/agent-control-specification-runtime-governance/)
- [Agent Governance Toolkit (GitHub)](https://github.com/microsoft/agent-governance-toolkit)
- [Microsoft Agent Framework 1.0 GA](https://learn.microsoft.com/en-us/agent-framework/overview)
- [Hosted Agents in Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents)
- [Frontier Tuning blog](https://aka.ms/frontiertuningblog)
- [Open Trust Stack for AI Agents](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents)
