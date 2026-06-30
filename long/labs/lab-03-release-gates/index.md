---
title: "Lab 3: Release Gates and Evidence"
layout: default
parent: Lab Planning Pages
grand_parent: AgentOps VBD Workshop
nav_order: 3
---

# Lab 3: Release Gates and Evidence

This lab turns evaluation into an enforceable shipping process.

## Duration

60 minutes

## Outcome

Attendees plan how evaluation results become enforceable release gates and reviewable evidence.

## Concepts

- PR gates
- Deployment gates
- Baseline comparison
- Threshold failure
- Readiness report
- Evidence package
- Review and approval workflow

## Artifact

A release-gate plan:

- Gate location
- Required evals
- Thresholds
- Failure behavior
- Evidence artifact
- Reviewer
- Promotion criteria

## Exercise flow

1. **Map the delivery path.** Identify where changes enter: prompt edits, model configuration, tool changes, data-source changes, app code, policy changes, and infrastructure.
2. **Choose gate locations.** Decide what runs on PR, pre-merge, pre-deploy, post-deploy smoke, and scheduled readiness review.
3. **Attach evidence.** Define the report or artifact reviewers need: eval run, threshold summary, failed cases, risk notes, telemetry expectations, and approval record.
4. **Define failure behavior.** Decide what blocks automatically, what requires human review, and what can be accepted with documented risk.
5. **Plan promotion.** Define how a version moves across dev, qa, pilot, and production.

## Facilitator prompts

- Which agent changes bypass normal app-code review today?
- What proof should a reviewer see before approving a release?
- Can a release pass CI while still failing safety or observability readiness?
- How does the team prove a deployed version is observable after promotion?

## Observability angle

Release evidence should include links to telemetry expectations and post-deployment observability checks. A release is not complete until the team can verify that the new version is visible in traces and dashboards.

## Completion criteria

- Gate locations are named.
- Required evaluation results are connected to those gates.
- Release evidence is reviewable by a human.
- Post-deployment observability checks are part of the release definition.
