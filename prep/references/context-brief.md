---
title: Context Brief
layout: default
parent: Source Materials
nav_order: 1
---

# Context Brief

This page captures the working context for the AgentOps Workshop so contributors can continue from this repository without needing private chat history or private source links.

## What this repository is

This repository is a GitHub Pages workshop site for teaching AgentOps as the operating model for production-ready AI agents.

It has two tracks:

- **Short workshop:** concise customer-facing session plan with deck outline, run of show, observability plan, and demo video plan.
- **Long workshop:** full-day workshop planning structure with multiple future labs. The labs are intentionally placeholders until the lab implementation plan is approved.

## Core story

AI agents are moving from prototype to production. Production teams need more than a working demo: they need release evidence, evaluation, CI/CD gates, observability, diagnostics, safety, governance, cost awareness, and continuous improvement.

AgentOps is the operating model that connects those practices into a repeatable loop:

**Evaluate -> Gate -> Observe -> Diagnose -> Ship -> Improve**

## Current state

The repository currently includes:

- GitHub Pages site structure with Jekyll and Just the Docs.
- A short workshop session plan.
- A long workshop planning skeleton.
- A dedicated observability plan for the short session.
- A dedicated observability lab plan for the full-day workshop.
- Sanitized reference notes instead of raw private source links.

## What to work on next

The next useful work is:

1. Turn the short workshop slide plan into a polished deck.
2. Expand the short workshop demo video plan into a recording script and shot list.
3. Define the scenario for the long workshop.
4. Implement Lab 1 and Lab 2 first, then use those to anchor the rest of the labs.
5. Build the observability lab with traces, telemetry correlation, dashboards, alerts, and trace-to-evaluation feedback.
6. Add an FAQ page based on reviewer and attendee questions.

## What not to add

Do not add:

- Personal names.
- Private links.
- Local machine paths.
- Tenant identifiers.
- Customer data.
- Raw telemetry exports.
- Product claims that are not verified.
- Lab solution code before the lab plan is approved.

## Important emphasis

Observability should remain one of the strongest parts of the workshop. It is not just infrastructure monitoring. The material should teach how traces, telemetry, release metadata, incidents, user feedback, safety signals, latency, and cost connect back to evaluation and release readiness.
