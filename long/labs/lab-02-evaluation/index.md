---
title: "Lab 2: Evaluation Design"
layout: default
parent: Lab Planning Pages
grand_parent: AgentOps VBD Workshop
nav_order: 2
---

# Lab 2: Evaluation Design

This lab defines how the team will know whether the agent behaves well enough to ship.

## Duration

75 minutes

## Outcome

Attendees design an evaluation strategy for one production-candidate agent.

## Concepts

- Golden datasets
- Regression candidates
- Baselines
- Thresholds
- Quality, groundedness, safety, latency, and cost metrics
- Evaluation evidence as a release signal

## Artifact

An evaluation plan:

- Dataset scope
- Example user journeys
- Expected behavior
- Metrics
- Thresholds
- Baseline strategy
- Review cadence

## Exercise flow

1. **List critical journeys.** Identify the highest-value and highest-risk user journeys for the selected agent.
2. **Create dataset slices.** Group examples by happy path, edge case, safety risk, grounding risk, tool failure, and known incident pattern.
3. **Define expected behavior.** Capture what a good answer, safe refusal, grounded citation, or tool action should look like.
4. **Select metrics.** Choose quality, groundedness, safety, latency, cost, and task-completion metrics that are meaningful for the release decision.
5. **Set gates.** Define minimum thresholds and baseline deltas that would block a release.
6. **Close the loop.** Decide how production traces, user feedback, red-team findings, and incidents become future evaluation rows.

## Facilitator prompts

- Which cases must never regress?
- Which failures should block a PR and which should block environment promotion?
- What is the baseline: prior agent version, human answer, known-good response, or policy?
- Which production traces are important enough to preserve as regression tests?

## Observability angle

Production traces become future evaluation cases. The evaluation dataset should include a field or convention for linking a row back to a trace, incident, customer journey, or red-team finding.

## Completion criteria

- The team has at least five dataset slices.
- Each critical metric has a threshold or baseline comparison.
- Release-blocking failures are explicit.
- The trace-to-eval promotion rule is documented.
