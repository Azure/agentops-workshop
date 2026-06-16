---
title: Home
layout: home
nav_order: 1
---

# AgentOps Workshop

This site is for **instructors** preparing to deliver the AgentOps workshop. It packages the slides, the narrated walkthrough, the speaker script, and the run-of-show in one place.

Two tracks are available:

- **AgentOps Briefing** (~1 hour) - ready to deliver.
- **AgentOps Value Delivery Workshop** (~8 hours, Value-Based Delivery) - under construction.

---

## AgentOps Briefing - ready to deliver

<div class="video-preview" markdown="0">
  <video controls preload="metadata" playsinline>
    <source src="{{ '/short/agentops-short-video.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support embedded video. <a href="{{ '/short/agentops-short-video.mp4' | relative_url }}">Download the video</a> to view it.
  </video>
</div>

<div class="download-cards" markdown="0">
<a class="download-card" href="{{ '/short/slides.pptx' | relative_url }}">
  <span class="download-card__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3.75 3v11.25A2.25 2.25 0 006 16.5h12a2.25 2.25 0 002.25-2.25V3"/><path d="M3 3h18M8 21l4-4 4 4"/><path d="M7.5 12l2.5-3 2 2 3.5-4.5"/></svg>
  </span>
  <span class="download-card__text">
    <span class="download-card__title">PowerPoint deck</span>
    <span class="download-card__meta">slides.pptx · 30 MB</span>
  </span>
  <span class="download-card__chevron" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v15M5 12l7 7 7-7"/></svg>
  </span>
</a>
<a class="download-card" href="{{ '/short/agentops-short-video.mp4' | relative_url }}">
  <span class="download-card__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l6-3.5z" fill="currentColor" stroke="none"/></svg>
  </span>
  <span class="download-card__text">
    <span class="download-card__title">Narrated video</span>
    <span class="download-card__meta">MP4 · 69 MB · 46 min</span>
  </span>
  <span class="download-card__chevron" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v15M5 12l7 7 7-7"/></svg>
  </span>
</a>
<a class="download-card download-card--secondary" href="{{ '/short/speaker-script' | relative_url }}">
  <span class="download-card__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8z"/><path d="M14 3v5h5"/><path d="M8 13h8M8 17h6"/></svg>
  </span>
  <span class="download-card__text">
    <span class="download-card__title">Speaker script</span>
    <span class="download-card__meta">Verbatim narration</span>
  </span>
  <span class="download-card__chevron" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>
  </span>
</a>
</div>

<p class="downloads-note" markdown="0">Repository access required: this repository is private, so the preview and download links resolve only for signed-in members of the <strong>Azure</strong> GitHub organization.</p>

| Resource | What it is |
|---|---|
| [Agenda]({{ '/short/agenda' | relative_url }}) | Customer-facing abstract and timeboxed agenda. |
| [Run of show]({{ '/short/run-of-show' | relative_url }}) | Presenter timing, transitions, and delivery cues. |
| [Speaker script]({{ '/short/speaker-script' | relative_url }}) | Verbatim word-for-word narration (~50 min). |
| [Instructor delivery guide]({{ '/instructor/delivery-guide' | relative_url }}) | Cross-track notes on what to emphasize. |

---

## AgentOps Value Delivery Workshop

The full-day (~8 hours) workshop is the Value-Based Delivery (VBD) track. It is still being designed, and the planning pages are visible so you can see where it is heading, but the labs are placeholders.

[See the VBD workshop plan]({{ '/long/' | relative_url }}){: .btn }

---

## What the workshop is about

AgentOps applies production engineering discipline to AI agents. The workshop walks instructors through the four-pillar operating model used to take one agent from prototype to production:

**Evaluate → Ship → Observe → Own**

AgentOps Briefing introduces the model with a demo storyline: an existing Foundry agent is evaluated, release gates block regressions before production, runtime traces make behavior observable, and Day-2 ownership turns incidents and production learnings into the next evaluation cycle.

---

## Authoring this workshop

If you are not delivering the workshop but contributing to it, start with the [repository README on GitHub](https://github.com/Azure/agentops-workshop#readme). The README and the `prep/` folder hold the authoring tools, references, and intermediate artefacts used to build everything published here.
