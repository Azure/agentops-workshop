---
title: "Lab 2: Evaluation Design"
layout: default
parent: Lab Planning Pages
grand_parent: AgentOps VBD Workshop
nav_order: 2
---

# Lab 2: Evaluation Design

{: .planning }
This is a planning placeholder. Lab implementation content has not been written yet.

## Planned duration

75 minutes

## Planned outcome

Attendees design an evaluation strategy for one production-candidate agent.

## Planned concepts

- Golden datasets
- Regression candidates
- Baselines
- Thresholds
- Quality, groundedness, safety, latency, and cost metrics
- Evaluation evidence as a release signal

## Planned artifact

An evaluation plan:

- Dataset scope
- Example user journeys
- Expected behavior
- Metrics
- Thresholds
- Baseline strategy
- Review cadence

## Observability angle

This lab should explain how production traces become future evaluation cases. The evaluation dataset should include a field or convention for linking a row back to a trace, incident, customer journey, or red-team finding.

## Implementation backlog

- Define a sample dataset format.
- Decide which metrics are mandatory vs. optional.
- Add example quality and safety criteria.
- Define how eval output maps to release evidence.
