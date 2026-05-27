---
title: Instructor Delivery Guide
layout: default
nav_order: 4
---

# Instructor Delivery Guide

## Delivery intent

The workshop should feel like a production-readiness engagement, not a product tour. The instructor should repeatedly connect concepts back to the operating loop:

**Evaluate -> Gate -> Observe -> Diagnose -> Ship -> Improve**

## Recommended delivery style

- Start from the production question: "Can we safely ship this agent?"
- Use one production-candidate agent as the thread through the session.
- Treat observability as an engineering discipline, not as screenshots of dashboards.
- Use failures intentionally. A failed eval or gate is the clearest way to show value.
- Keep AgentOps Toolkit references subtle and practical.

## For the short workshop

The short workshop should prioritize:

1. Production gap and AgentOps operating model
2. Evaluation and release gates
3. Observability for agents
4. Demo video
5. 30-day starting path

The observability section should explain trace correlation and the trace-to-evaluation feedback loop.

## For the long workshop

The long workshop should prioritize:

1. One consistent scenario
2. One readiness artifact per lab
3. Strong observability thread across labs
4. Capstone release-readiness review

The dedicated observability lab should be treated as a major part of the day, not a side topic.

## Instructor checklist

Before delivery:

- Confirm the target audience and expected technical depth.
- Confirm whether the session is the short or long workshop.
- Confirm whether live demos, recorded demos, or screenshots will be used.
- Confirm the Foundry project and agent scenario.
- Confirm that no sensitive telemetry or tenant data appears in screenshots.
- Confirm the GitHub Pages site builds after content changes.

After delivery:

- Capture questions that should become FAQ entries.
- Capture observability gaps that should become lab improvements.
- Capture production scenarios that should become evaluation examples.
