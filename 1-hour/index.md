---
title: 1-Hour Session
layout: default
nav_order: 2
has_children: true
---

# 1-Hour Session

This track is the short customer-facing session for AgentOps. It is designed for a 1-hour delivery and is labeled the **1-hour session** to avoid confusion with the full 8-hour workshop.

## Session promise

In one hour, attendees should understand how AgentOps helps teams answer one production question:

> Can we safely ship this version of the agent, and where is the evidence?

## Planning pages

| Page | Purpose |
|---|---|
| [Agenda](agenda.md) | Customer-facing abstract and timeboxed agenda. |
| [Run of show](run-of-show.md) | Presenter timing, transitions, and delivery cues. |
| [Speaker script](speaker-script.md) | Verbatim word-for-word narration for the recorded video (~50 min). |

## Deliverables

- `slides.md` - Marp source of the 23-slide deck.
- `slides.pptx` - Exported PowerPoint deck.
- `agentops-1hour-video.mp4` - 46-minute narrated walkthrough recorded from the deck.
- `images\` - Diagrams referenced from the slides.

Internal authoring notes (slide plan, observability plan, demo video plan, build tools, intermediate artefacts) live under `prep\1-hour\` and `prep\tools\` and are excluded from the published site.

## Required emphasis

The short session must still explore observability clearly. It should not reduce observability to a single monitoring bullet. The audience should leave understanding why agent observability needs correlated traces, evals, releases, user feedback, safety events, latency, and cost signals.
