---
title: Instructor Guide
layout: default
parent: AgentOps VBD Workshop
nav_order: 7
---

# Instructor Guide

This is the Field Engagement Guide for delivering the AgentOps Value Delivery Workshop.
It covers objectives, scope, setup, timing, and lab-by-lab pitfalls. Read it end to end
before delivery, and walk every lab on the shared sample agent at least once.

## Objectives

- Each attendee leaves with a release-readiness package filled in for one of their own
  production-candidate agents.
- The four-pillar model (Evaluate -> Ship -> Observe -> Operate) is demonstrated end to
  end, not just described.
- The observability thread is real: one production trace can be walked back to its
  version, evaluation, release, and owner.

## Scope

**In scope:** the operating model, hands-on labs against the attendee's own Foundry
project and sample agent, and the ten release-readiness artefacts.

**Out of scope:** provisioning per-attendee Azure resources, building a bespoke pipeline
beyond what `agentops workflow generate` produces, and any work on agents other than the
chosen candidate. This is a one-day workshop, not a multi-week engagement.

## Required customer participants

- A builder who knows the candidate agent.
- A platform / DevOps engineer who can run CI workflows.
- A governance or Responsible AI stakeholder for the safety and RACI work.
- Someone who can speak to release-approval ownership (often the gap the workshop exposes).

## Foundry and environment prerequisites

Confirm the [prerequisites checklist]({{ '/long/prerequisites' | relative_url }}) is met a
week ahead. The two that most often block the room on the day:

- The Foundry **project endpoint** and **linked Application Insights** resource.
- Each machine's **eval environment variables** and a working `az login`.

## Sample agent setup

Bring a shared sample agent so attendees without their own can still do every lab:

- A simple Prompt agent in a demo Foundry project with one or two tools and a small
  knowledge source.
- A seeded eval dataset (20-40 cases) under `.agentops/data/`.
- A captured baseline under `.agentops/baseline/results.json`.
- One or two exported **trace files** for Labs 4 and 6 (so the trace-promotion loop works
  even with no live traffic).

Have these in a repo attendees can fork or clone at the start of Lab 1.

## Room and AV

- One screen for the deck; a second for live `agentops` / Foundry / Azure Monitor is ideal.
- Reliable internet to Azure for every participant.
- Power and seating for a full day; plan the breaks in the agenda.
- A shared channel (Teams chat) for pasting commands and endpoints.

## Timing and contingency

The [agenda]({{ '/long/agenda' | relative_url }}) is sized so the content runs ~8 hours
with ~75 minutes of breaks. If you fall behind:

- **Protect Lab 4** (observability) - it is the deepest and the differentiator. Cut time
  from Labs 5 and 6 first.
- Labs 3, 5, and 6 can be run as "fill in the artefact + walk one example" if Azure access
  is flaky, without losing the learning.
- The capstone must happen even if shortened - it is where the day becomes one story.

Rough cut order if you are short on time: trim Lab 6 to one walked incident, then Lab 5
red-team scan to a sample findings list, then Lab 2 dataset to the seeded sample.

## Lab-by-lab pitfalls

| Lab | Most common pitfall | Mitigation |
|---|---|---|
| 1 Foundations | Analysis paralysis on agent choice | Time-box selection; the choice is reversible |
| 1 Foundations | `agentops init` fails on missing endpoint | Put the endpoint format on a slide |
| 2 Evaluation | Hundreds of synthetic cases | Insist on 20-40 real cases |
| 2 Evaluation | Quota / slow eval runs | Use a reduced dataset; the learning is the threshold design |
| 3 Release gates | Only seeing a passing gate | Force a regressing PR so everyone sees a red check |
| 3 Release gates | Expecting prod to re-evaluate | Stress that evidence is locked at qa |
| 4 Observability | Missing release metadata on traces | Let attendees discover the gap in Step 2 |
| 4 Observability | No production traffic | Provide a sample trace file |
| 5 Safety | Treating fixed as closed | A finding is closed only when an eval row covers it |
| 5 Safety | "Nobody" owns release approval | Surface it as a finding, not a failure |
| 6 Improvement | Several half-walked incidents | One incident, walked completely |
| Capstone | Hand-waved "go" | A no-go with a 30-day plan is a success |

## Facilitation principles

- Keep the operating model the narrative; the accelerator is the "how", not the topic.
- Use the four-pillar language consistently. Do not reintroduce the old six-step loop or
  the word "Own" - the workshop pillar is **Operate**.
- Tie every lab artefact back to the release-readiness contract from Lab 1.
- End on the maturity move: most teams advance one level on one agent. That is the win.

## After the workshop

- Each team has a 30-day plan from the capstone - schedule a check-in.
- Point teams at the [AgentOps Accelerator docs](https://github.com/Azure/agentops) for
  pipeline, dashboard, and Doctor depth beyond the workshop.
- Capture recurring gaps (often release-approval ownership and missing release metadata) as
  feedback for the program.
