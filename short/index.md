---
title: AgentOps Briefing
layout: default
nav_order: 2
has_children: true
---

# AgentOps Briefing

A ~1 hour customer-facing AgentOps session. Everything below is ready to deliver.

## Download

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
<a class="download-card download-card--secondary" href="{{ '/short/video-narration' | relative_url }}">
  <span class="download-card__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8z"/><path d="M14 3v5h5"/><path d="M8 13h8M8 17h6"/></svg>
  </span>
  <span class="download-card__text">
    <span class="download-card__title">Video narration</span>
    <span class="download-card__meta">Verbatim short video narration</span>
  </span>
  <span class="download-card__chevron" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>
  </span>
</a>
</div>

<p class="downloads-note" markdown="0">Repository access required: this repository is private, so the download links resolve only for signed-in members of the <strong>Azure</strong> GitHub organization.</p>

## Session promise

In one hour, attendees should understand how AgentOps helps teams answer one production question:

> Can we safely ship this version of the agent, and where is the evidence?

## Delivery pages

| Page | Purpose |
|---|---|
| [Agenda]({{ '/short/agenda' | relative_url }}) | Customer-facing abstract and timeboxed agenda. |
| [Run of show]({{ '/short/run-of-show' | relative_url }}) | Presenter timing, transitions, and delivery cues. |
| [Video narration]({{ '/short/video-narration' | relative_url }}) | Verbatim narration for the short recorded video. |
| [Speaker script]({{ '/short/speaker-script' | relative_url }}) | Verbatim narration for the recorded workshop walkthrough (~50 min). |

## Required emphasis

The short session must explore observability clearly. It should not reduce observability to a single monitoring bullet. The audience should leave understanding why agent observability needs correlated traces, evals, releases, user feedback, safety events, latency, and cost signals.

## Reusing the material

The deck and video are intended to be delivered as-is, lightly customised, or remixed into your own session. If you change content, please keep the four-pillar operating model (Evaluate -> Ship -> Observe -> Operate) intact, since the rest of the narrative depends on it.
