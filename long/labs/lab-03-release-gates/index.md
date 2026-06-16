---
title: "Lab 3: Release Gates and Evidence"
layout: default
parent: Lab Planning Pages
grand_parent: AgentOps VBD Workshop
nav_order: 3
---

# Lab 3: Release Gates and Evidence

{: .planning }
This is a planning placeholder. Lab implementation content has not been written yet.

## Planned duration

60 minutes

## Planned outcome

Attendees plan how evaluation results become enforceable release gates and reviewable evidence.

## Planned concepts

- PR gates
- Deployment gates
- Baseline comparison
- Threshold failure
- Readiness report
- Evidence package
- Review and approval workflow

## Planned artifact

A release-gate plan:

- Gate location
- Required evals
- Thresholds
- Failure behavior
- Evidence artifact
- Reviewer
- Promotion criteria

## Observability angle

Release evidence should include links to telemetry expectations and post-deployment observability checks. A release is not complete until the team can verify that the new version is visible in traces and dashboards.

## Implementation backlog

- Choose GitHub Actions or Azure DevOps workflow examples.
- Define minimal workflow YAML later.
- Add failure and success examples.
- Decide how evidence artifacts are stored and reviewed.
