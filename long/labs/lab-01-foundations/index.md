---
title: "Lab 1: Foundations and Control Plane"
layout: default
parent: Labs
nav_order: 1
---

# Lab 1: Foundations and Control Plane

{: .outcome }
> **Artefacts produced:** [agent target inventory]({{ '/long/labs/templates/agent-target-inventory/' | relative_url }})
> and [release-readiness contract]({{ '/long/labs/templates/release-readiness-contract/' | relative_url }}).

**Pillar:** Foundations. **Duration:** 60 minutes. **Level:** no-code / low-code.

## Objective

Pick one production-candidate agent, map it onto the Microsoft Foundry control plane and
your repository, and write the release-readiness contract that the rest of the day fills
in. By the end you can answer: *what are we trying to ship, and what evidence will prove
it is safe?*

## Why this lab is first

Everything downstream - evaluation, gates, observability, Day-2 - needs a concrete target
and a stable identity. This lab defines the `agent_id`, `agent_version`, owner, and the
correlation keys that thread through every other artefact and every production trace.

## Prerequisites

- A Microsoft Foundry project you can open (see [prerequisites]({{ '/long/prerequisites' | relative_url }})).
- A sample or real agent in that project.
- A GitHub repository you control.
- AgentOps Accelerator installed: `python -m pip install agentops-accelerator`.

## Concepts (10 min)

- **The four-pillar AgentOps model:** Evaluate -> Ship -> Observe -> Operate. AgentOps is
  the operating model; Foundry is the control plane; the AgentOps Accelerator is one
  concrete implementation path.
- **Foundry as the control plane:** agents and versions, evaluators, tracing, content
  safety, and red teaming live here. AgentOps connects those signals to release decisions.
- **Agent target and version identity:** an agent is a versioned asset (`name:version`),
  an evaluation target, and an operational dependency at the same time.
- **Repo-side release contract:** the repository holds the release candidate, the CI
  workflow, the eval evidence, and `agentops.yaml`.
- **Environment ladder:** sandbox -> dev -> qa -> prod. Sandbox is the authoring space
  with a local eval gate before a pull request.

## Steps

### Step 1 - Inventory your agents (15 min)

Open the [agent target inventory template]({{ '/long/labs/templates/agent-target-inventory/' | relative_url }}).
List the agents your team is considering for production. For each, capture purpose, type
(Prompt / Hosted / HTTP), Foundry project, owner, knowledge sources, tools, and known
risks.

Pick exactly **one** production-candidate agent to carry through the day. Prefer an agent
that is close to production and has a real user journey - not your most ambitious
prototype.

### Step 2 - Map the control plane (10 min)

In the Foundry portal, locate for your chosen agent:

- The agent and its current version (`name:version`).
- The project endpoint (looks like `https://<resource>.services.ai.azure.com/api/projects/<project>`).
- The linked Application Insights resource (you will need it in Lab 4).

Record the project endpoint and version in the inventory.

### Step 3 - Bootstrap the repo-side workspace (10 min)

In your repository, initialize the accelerator:

```text
agentops init
```

This guided setup creates `agentops.yaml` and the `.agentops/` workspace. Point the
Foundry target at your agent using either `project_endpoint:` in `agentops.yaml` or the
`AZURE_AI_FOUNDRY_PROJECT_ENDPOINT` environment variable, and set `agent: name:version`.

Confirm the identity matches the inventory: the `agent_id` / `name:version` in
`agentops.yaml` must equal what you recorded in Step 1.

### Step 4 - Write the release-readiness contract (15 min)

Open the [release-readiness contract template]({{ '/long/labs/templates/release-readiness-contract/' | relative_url }}).
Fill in:

- The release-readiness question, in your own words, for this agent.
- The eight criteria, with an owner for each.
- What is explicitly out of scope for the first release.

Leave the evidence links blank for now - later labs fill them in. The contract is the
spine of the capstone.

## Artefact

Two artefacts, both committed to your repo (for example under `docs/agentops/`):

1. **Agent target inventory** with one production-candidate selected.
2. **Release-readiness contract** with the eight criteria and owners assigned.

## Observability metadata captured

This lab defines the correlation keys every later trace must carry:

- `agent_id` and `agent_version`
- `deployment_id` / environment
- Trace ID convention (how you will find a single interaction)
- `owner` and escalation path

Carry these identical across all artefacts. Lab 4 makes them present on every production
trace; the capstone uses them to walk a trace back to its version, evaluation, release,
and owner.

## Time budget

| Step | Minutes |
|---|---:|
| Concepts | 10 |
| Inventory agents | 15 |
| Map the control plane | 10 |
| Bootstrap repo workspace | 10 |
| Release-readiness contract | 15 |

## Facilitator tips

- The most common stall is analysis paralysis on agent selection. Time-box Step 1 hard
  and tell attendees the choice is reversible - the point is to practice the pattern.
- If an attendee has no agent at all, pair them with the shared sample agent from the
  [instructor guide]({{ '/long/instructor-guide' | relative_url }}).
- Watch for `agentops init` failures caused by a missing project endpoint - have the
  endpoint format on a slide.

## Discussion prompts

- Which of the eight contract criteria is your team weakest on today?
- Who actually owns "the agent is safe to ship" in your organization right now?
- What is the smallest version increment you could ship with confidence this quarter?

## References

- [AgentOps Accelerator](https://github.com/Azure/agentops) - `agentops init`, `agentops.yaml`.
- [Agent development lifecycle](https://learn.microsoft.com/azure/ai-foundry/agents/concepts/development-lifecycle)
