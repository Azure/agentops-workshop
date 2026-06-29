---
title: Labs
layout: default
parent: AgentOps VBD Workshop
nav_order: 6
has_children: true
---

# Labs

The full-day workshop is six hands-on labs plus a capstone. Each lab is self-contained:
objective, prerequisites, step-by-step instructions, the artefact it produces, the
observability metadata it captures, a time budget, facilitator tips, and discussion
prompts. Labs run against the attendee's own Microsoft Foundry project and sample agent,
and use the [AgentOps Accelerator](https://github.com/Azure/agentops) as the concrete
implementation path.

Start each lab from its page. Fill in the matching
[artefact template](templates/) as you go - by the capstone every template should be
complete for one production-candidate agent.

## Labs

| Lab | Duration | Level | Artefact produced | Status |
|---|---:|---|---|---|
| [Lab 1: Foundations and control plane](lab-01-foundations/) | 60 min | no-code / low-code | Agent target inventory, release-readiness contract | Ready |
| [Lab 2: Evaluation design](lab-02-evaluation/) | 75 min | low-code | Evaluation dataset plan, baseline and threshold plan | Ready |
| [Lab 3: Release gates and evidence](lab-03-release-gates/) | 60 min | low-code / full-code | CI/CD gate plan, readiness evidence package | Ready |
| [Lab 4: Observability and trace-driven operations](lab-04-observability/) | 90 min | low-code | Observability correlation model, dashboard and alert plan | Ready |
| [Lab 5: Safety, red-team follow-through, and governance](lab-05-safety-governance/) | 45 min | no-code / low-code | Safety and red-team follow-through plan, governance/RACI map | Ready |
| [Lab 6: Incident response and continuous improvement](lab-06-continuous-improvement/) | 35 min | no-code / low-code | Incident response and continuous-improvement plan | Ready |
| [Capstone: Production-readiness review](capstone/) | 30 min | discussion | Composed release-readiness review | Ready |

## Templates

The downloadable [artefact templates](templates/) back the labs. There is one template
per artefact in the [lab roadmap]({{ '/long/lab-roadmap' | relative_url }}).
