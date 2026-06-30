---
title: Labs
layout: default
parent: AgentOps VBD Workshop
nav_order: 4
has_children: true
---

# Labs

This is a hands-on lab track. You build one real agent and operate it end to end.

Across the seven labs you stand up the Contoso Travel Agent as a Microsoft Foundry Prompt Agent, then carry that same agent through evaluation, release gates, observability, safety, continuous improvement, and a CI/CD production-readiness review. Every lab gives you exact commands and exact portal clicks, and every lab consumes the artifact the previous lab produced. By the end you have run the full AgentOps loop - Evaluate, Ship, Observe, Operate - on a live Foundry agent.

The labs use the public Azure AgentOps accelerator (PyPI package `agentops-accelerator`, CLI `agentops`) as the practical way to make the operating model tangible. The accelerator is a reference accelerator only; the subject of the workshop is the AgentOps operating model on Microsoft Foundry.

## The running example

One agent runs through the whole day: the **Contoso Travel Agent**, a Foundry Prompt Agent named `travel-agent`. You create it in Lab 1, evaluate it in Lab 2, regress and gate it in Lab 3, observe it in Lab 4, secure and govern it in Lab 5, improve it from real traces in Lab 6, and ship it through CI/CD in the capstone.

## Labs

| Lab | You build | Artifact produced |
|---|---|---|
| [Lab 1: Foundations and Control Plane](lab-01-foundations/) | Install the accelerator, sign in to Azure, create `travel-agent:1` in Foundry, run `agentops init`. | Initialized `agentops.yaml` + `.agentops/` workspace. |
| [Lab 2: Evaluation Design](lab-02-evaluation/) | A JSONL eval dataset, thresholds, your first `agentops eval run`, captured baseline. | `travel-smoke.jsonl` + green baseline. |
| [Lab 3: Release Gates and Evidence](lab-03-release-gates/) | A regressed `travel-agent:2`, a baseline-compared run that fails the gate, a Doctor evidence pack. | Release evidence pack at `.agentops/release/latest/`. |
| [Lab 4: Observability and Trace-Driven Operations](lab-04-observability/) | Foundry + Application Insights tracing, telemetry import, Cockpit, a trace drilldown. | Imported telemetry + a flagged production trace. |
| [Lab 5: Safety, Red-Team Follow-Through, and Governance](lab-05-safety-governance/) | A content-safety evaluator, governance-as-code in `agentops.yaml`, a Foundry red-team scan. | Safety + governance evidence in the pack. |
| [Lab 6: Incident Response and Continuous Improvement](lab-06-continuous-improvement/) | Promote the flagged trace into the dataset, re-evaluate, move the baseline forward. | Regression row + refreshed baseline. |
| [Capstone: Production-Readiness Review](capstone/) | A GitHub Actions PR gate (green and red), the final evidence pack, a ship decision. | CI/CD gate + signed ship-decision record. |

## Before you start

Each attendee needs:

- An Azure subscription and access to a Microsoft Foundry project (portal `https://ai.azure.com`) with a model deployment named `gpt-4o-mini`.
- Owner or Contributor on the Foundry project.
- Python 3.10 or later, the Azure CLI (`az`), and git on the machine.
- An Application Insights resource connected to the Foundry project (used from Lab 4 onward).
- A GitHub account and an empty repository for the capstone CI/CD lab.

Lab 1 walks through installing `agentops-accelerator`, signing in with `az login`, and setting the Foundry environment variables. Start each lab from the `agentops-vbd` working folder you create in Lab 1, and keep the same shell open so your environment variables persist.
