---
title: "Lab 5: Safety, Red-Team Follow-Through, and Governance"
layout: default
parent: Labs
nav_order: 5
---

# Lab 5: Safety, Red-Team Follow-Through, and Governance

{: .outcome }
> **Artefact produced:** [safety and red-team follow-through plan]({{ '/long/labs/templates/safety-redteam-followthrough-plan/' | relative_url }})
> (including the governance / RACI map).

**Pillar:** Operate (safety and governance). **Duration:** 45 minutes. **Level:** no-code / low-code.

## Objective

Treat safety as a distinct signal from quality, run adversarial testing, and define who
owns what. By the end you can answer: *can someone make this agent misbehave, what do we
do when they can, and who is accountable?*

## Why safety is its own signal

Quality evaluation asks "is the answer good?"; red teaming asks "can someone make it
misbehave?". A quality score will not catch a jailbreak. Both signals are required, and a
safety finding is not closed when it is fixed - it is closed when an eval row would catch
the regression next time.

## Prerequisites

- Labs 1-3 complete (agent, dataset, evidence package).
- Foundry AI Red Teaming Agent available in your project.

## Concepts (10 min)

- **Four risk categories:** harmful content, jailbreak / prompt injection, hallucination /
  ungrounded claims, data exfiltration / PII leakage.
- **Red teaming:** Foundry's AI Red Teaming Agent (backed by Microsoft's PyRIT framework)
  automates adversarial probes.
- **Cadence:** pre-release gate, scheduled scans, post-incident.
- **Governance:** clear accountability via a RACI map - evaluation sign-off, release
  approval, safety review, incident response, cost ownership.

## Steps

### Step 1 - Scope the risk categories (10 min)

Open the [safety and red-team follow-through plan template]({{ '/long/labs/templates/safety-redteam-followthrough-plan/' | relative_url }}).
For each of the four risk categories, decide whether it is in scope for your agent and
why. A retrieval agent over public docs has a different exfiltration risk than one with
tool access to customer data.

### Step 2 - Run a red-team scan (10 min)

Run the Foundry AI Red Teaming Agent against your agent (pre-release cadence). Record each
finding in the plan: category, severity, status. Even a short scan surfaces the shape of
the findings.

### Step 3 - Follow findings through to eval coverage (10 min)

For each high or medium finding, add an adversarial row to your eval dataset (Lab 2) so
the regression is caught in the PR gate. Mark "eval row added?" in the plan. This is the
follow-through that makes safety durable rather than a one-time report.

### Step 4 - Draw the governance / RACI map (10 min)

Fill in the RACI table: for evaluation sign-off, release approval, safety / red-team
review, incident response, and cost ownership, name who is Responsible, Accountable,
Consulted, and Informed. Ambiguous accountability here is the most common reason agents
stall before production.

### Step 5 - Update the evidence package (5 min)

Return to the readiness evidence package (Lab 3) section 5 and record content-safety
status, the red-team scan link, and any open high findings.

## Artefact

**Safety and red-team follow-through plan** - risk scope, findings with follow-through
status, cadence, and the governance / RACI map.

## Observability metadata captured

- Safety findings (category, severity, status) linked to `agent_version`.
- Content-safety events surfaced in the Lab 4 dashboards and the evidence package.

## Time budget

| Step | Minutes |
|---|---:|
| Concepts | 10 |
| Scope risk categories | 10 |
| Red-team scan | 10 |
| Findings to eval coverage | 10 |
| Governance / RACI | 10 |
| Update evidence | 5 |

## Facilitator tips

- Keep the scan short and the follow-through long - the lesson is the loop from finding to
  eval row, not the scan output volume.
- The RACI conversation often reveals that "nobody" owns release approval today. That is a
  finding worth surfacing to leadership.
- If the Red Teaming Agent is unavailable in a tenant, use a sample findings list and
  focus the time on follow-through and governance.

## Discussion prompts

- Which risk category would do the most damage to your organization if it landed in prod?
- Who is accountable (not just responsible) for safety on your agent today?
- How many of your last safety findings became permanent test coverage?

## References

- [AI red teaming agent](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/run-ai-red-teaming-cloud)
- [AgentOps Accelerator](https://github.com/Azure/agentops) - eval dataset and `agentops doctor` evidence.
