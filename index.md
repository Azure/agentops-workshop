---
title: Home
layout: home
nav_order: 1
---

# AgentOps Workshop — Instructor Kit

This site is for **instructors** preparing to deliver the AgentOps workshop. It packages the slides, the narrated walkthrough, the speaker script, and the run-of-show in one place.

Two tracks are available:

- **Short workshop** (~1 hour) — ready to deliver.
- **Long workshop** (~8 hours) — under construction.

---

## Short workshop — ready to deliver

[Download PowerPoint deck (slides.pptx)]({{ '/short/slides.pptx' | relative_url }}){: .btn .btn-primary .fs-5 }
[Download narrated video (101 MB, 46 min)](https://github.com/Azure/agentops-workshop/releases/download/v0.1.0-short/agentops-short-video.mp4){: .btn .btn-primary .fs-5 }
[Open speaker script]({{ '/short/speaker-script' | relative_url }}){: .btn .fs-5 }

| Resource | What it is |
|---|---|
| [Agenda]({{ '/short/agenda' | relative_url }}) | Customer-facing abstract and timeboxed agenda. |
| [Run of show]({{ '/short/run-of-show' | relative_url }}) | Presenter timing, transitions, and delivery cues. |
| [Speaker script]({{ '/short/speaker-script' | relative_url }}) | Verbatim word-for-word narration (~50 min). |
| [Instructor delivery guide]({{ '/instructor/delivery-guide' | relative_url }}) | Cross-track notes on what to emphasize. |

---

## Long workshop — under construction

The full-day (~8 hours) workshop is being designed. The planning pages are visible so you can see where it is heading, but the labs are placeholders.

[See the long workshop plan]({{ '/long/' | relative_url }}){: .btn }

---

## What the workshop is about

AgentOps applies production engineering discipline to AI agents. The workshop walks instructors through an operating loop used to take one agent from prototype to production:

**Evaluate → Gate → Observe → Diagnose → Ship → Improve**

The short workshop introduces the loop with a demo storyline: an existing Foundry agent is evaluated, a regression is blocked before release, the issue is fixed, readiness evidence is reviewed, and telemetry links the release decision back to runtime behavior.

---

## Authoring this workshop

If you are not delivering the workshop but contributing to it, start with the [repository README on GitHub](https://github.com/Azure/agentops-workshop#readme). The README and the `prep/` folder hold the authoring tools, references, and intermediate artefacts used to build everything published here.

