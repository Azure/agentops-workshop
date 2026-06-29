---
title: Prerequisites
layout: default
parent: AgentOps VBD Workshop
nav_order: 2
---

# Prerequisites checklist

Have these in place before Day 1 so the room spends its time on AgentOps, not setup.
Share this page with the customer at least one week ahead.

## For the organization (before the workshop)

- [ ] A **Microsoft Foundry project** the participants can access.
- [ ] At least one **sample or real agent** in that project (Prompt agent, Hosted agent,
      or HTTP endpoint). A shared sample agent is provided for attendees who do not yet
      have their own - see the [instructor guide]({{ '/long/instructor-guide' | relative_url }}).
- [ ] A **GitHub repository** (or Azure DevOps project) where participants can open pull
      requests and run CI workflows.
- [ ] **Azure Monitor / Application Insights** linked to the Foundry project, with read
      access for participants.
- [ ] **Named participants** (6-20) covering builder, platform/DevOps, and governance
      roles. Include at least one person who can speak to release approval ownership.
- [ ] An **identified production-candidate agent** per team, or willingness to choose one
      in Lab 1.

## For each participant (on their machine)

- [ ] Python 3 and the ability to `pip install`.
- [ ] **AgentOps Accelerator** installed:
      `python -m pip install agentops-accelerator`
- [ ] Azure CLI installed and `az login` working against the right tenant.
- [ ] Environment variables ready for evaluation:
  - `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_DEPLOYMENT`
- [ ] Git configured and access to the workshop repository.

## Access and permissions

- [ ] Permission to **view and run evaluations** in the Foundry project.
- [ ] Permission to **view traces and telemetry** in Application Insights / Log Analytics.
- [ ] Permission to **open pull requests and run Actions** in the repository.
- [ ] (For the safety lab) access to the **Foundry AI Red Teaming Agent** in the project.

## Nice to have

- [ ] A small set of **real example interactions** with the candidate agent, to seed the
      evaluation dataset in Lab 2.
- [ ] One or two **production traces** (or exported trace files) to use in Labs 4 and 6.

## Out of scope

This workshop does not provision per-attendee Azure resources. Participants work in their
own Foundry project against their own (or the shared sample) agent. There is no
requirement for a pre-built CI/CD pipeline - Lab 3 generates one.
