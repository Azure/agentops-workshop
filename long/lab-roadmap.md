---
title: Lab Roadmap
layout: default
parent: AgentOps VBD Workshop
nav_order: 2
---

# Lab Roadmap

This roadmap defines the full-day VBD lab sequence. The labs are hands-on: attendees install the Azure AgentOps accelerator (CLI `agentops`), create a real Microsoft Foundry agent, and operate it end to end. Each lab builds directly on the artifact produced by the previous lab.

## Labs

| Lab | Duration | Level | Outcome |
|---|---:|---|---|
| [Lab 1: Foundations and Control Plane](labs/lab-01-foundations/) | 60 min | guided setup | Install the accelerator, sign in to Azure, create `travel-agent:1` in Foundry, and run `agentops init`. |
| [Lab 2: Evaluation Design](labs/lab-02-evaluation/) | 75 min | hands-on | Build a JSONL dataset, set thresholds, run `agentops eval run`, and capture a baseline. |
| [Lab 3: Release Gates and Evidence](labs/lab-03-release-gates/) | 75 min | hands-on | Regress to `travel-agent:2`, fail the baseline-compared gate, and produce a Doctor evidence pack. |
| [Lab 4: Observability and Trace-Driven Operations](labs/lab-04-observability/) | 90 min | hands-on | Turn on Foundry + Application Insights tracing, import telemetry, open Cockpit, and drill into a trace. |
| [Lab 5: Safety, Red-Team Follow-Through, and Governance](labs/lab-05-safety-governance/) | 75 min | hands-on | Add a content-safety evaluator, wire governance-as-code, and run a Foundry red-team scan. |
| [Lab 6: Incident Response and Continuous Improvement](labs/lab-06-continuous-improvement/) | 75 min | hands-on | Promote a real trace into the dataset, re-evaluate, and move the baseline forward. |
| [Capstone: Production-Readiness Review](labs/capstone/) | 90 min | hands-on | Generate a GitHub Actions PR gate, prove it green and red, and sign a ship decision. |

## The continuity spine

The labs share one running example - the Contoso Travel Agent (`travel-agent`) - and one workspace folder (`agentops-vbd`). What each lab hands to the next:

| Lab | Consumes | Produces |
|---|---|---|
| Lab 1 | Nothing | `travel-agent:1` in Foundry + initialized `agentops.yaml` and `.agentops/`. |
| Lab 2 | Lab 1 workspace | `.agentops/data/travel-smoke.jsonl` + green baseline at `.agentops/baseline/`. |
| Lab 3 | Lab 2 baseline | Regressed `travel-agent:2`, failing gate, evidence pack at `.agentops/release/latest/`. |
| Lab 4 | Lab 3 shipping agent | Live traces in Foundry + App Insights, imported telemetry, one flagged trace id. |
| Lab 5 | Lab 4 flagged agent | Content-safety evaluator + governance files, red-team results in evidence. |
| Lab 6 | Lab 4 flagged trace | New regression row in `travel-smoke.jsonl` + refreshed baseline. |
| Capstone | All prior artifacts | GitHub Actions gate (green and red) + final evidence pack + ship-decision record. |

## Lab-to-pillar mapping

| Pillar | Covered in | Evidence produced |
|---|---|---|
| Evaluate | Lab 2, Lab 5, Lab 6 | Dataset, metrics, thresholds, content-safety scores, incident-derived eval rows. |
| Ship | Lab 1, Lab 3, Capstone | Initialized workspace, baseline-compared gates, exit codes, CI/CD, release evidence pack. |
| Observe | Lab 4, Lab 6 | Foundry + App Insights traces, imported telemetry, Cockpit, trace-to-eval feedback. |
| Operate | Lab 5, Lab 6, Capstone | Red-team follow-through, governance-as-code, continuous-improvement loop, ship decision. |

## Observability thread

Observability is not isolated to Lab 4. Each lab keeps the agent traceable:

- Lab 1 fixes the target and version identity (`travel-agent:1`).
- Lab 2 defines which eval cases and metrics later need production correlation.
- Lab 3 attaches release evidence to the gate decision.
- Lab 4 turns on tracing and telemetry import - the deepest lab.
- Lab 5 records safety and governance signals into the evidence pack.
- Lab 6 turns a real trace into a permanent regression test.
- The capstone combines all evidence into an automated, reviewable release decision.
