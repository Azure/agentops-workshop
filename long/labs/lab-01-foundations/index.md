---
title: "Lab 1: Foundations and Control Plane"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 1
---

# Lab 1: Foundations and Control Plane

This lab turns the AgentOps story into a concrete target: one agent, one release decision, one owner model, and one traceability contract.

## Duration

60 minutes

## Outcome

Attendees identify the production-candidate agent, map the Foundry control plane, and define the release-readiness question.

## Concepts

- AgentOps four-pillar model: Evaluate, Ship, Observe, Operate
- Microsoft Foundry as the control plane
- Agent target and version identity
- Repo-side release-readiness contract
- Ownership and environment boundaries

## Artifact

An agent readiness profile:

- Agent name
- Foundry project
- Environment
- Owner
- Target version
- Release-readiness question
- Initial telemetry expectations

## Exercise flow

1. **Pick the agent.** Choose one agent or agent scenario that is closest to production value.
2. **Draw the control plane.** Identify Foundry project, models, tools, data sources, safety controls, repo, deployment environments, and telemetry destination.
3. **Name the release decision.** Write the exact decision the team wants evidence for, such as "Can version 0.7 move from pilot to production?"
4. **Define identity.** Decide how agent version, prompt version, model deployment, tool version, dataset, eval run, release ID, and trace ID will be linked.
5. **Assign owners.** Name the application owner, platform owner, safety reviewer, telemetry owner, and incident responder.

## Facilitator prompts

- What would make this agent unsafe or not ready to release?
- Which assets can change independently and therefore need versioning?
- If the agent fails tomorrow, who owns diagnosis and who owns rollback?
- Which signals must exist before the team can call the release observable?

## Observability angle

This lab defines the identifiers required for later observability:

- Agent ID
- Version or deployment ID
- Environment
- Trace ID convention
- Owner and escalation path

## Completion criteria

- The team can name the target agent and version.
- The release-readiness question is written in one sentence.
- Required correlation identifiers are listed.
- Owners and environments are identified.
