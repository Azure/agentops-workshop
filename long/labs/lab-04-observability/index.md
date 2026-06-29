---
title: "Lab 4: Observability and Trace-Driven Operations"
layout: default
parent: Labs
nav_order: 4
---

# Lab 4: Observability and Trace-Driven Operations

{: .outcome }
> **Artefacts produced:** [observability correlation model]({{ '/long/labs/templates/observability-correlation-model/' | relative_url }})
> and [dashboard and alert plan]({{ '/long/labs/templates/dashboard-and-alert-plan/' | relative_url }}).

**Pillar:** Observe. **Duration:** 90 minutes (the deepest lab). **Level:** low-code.

## Objective

Make your agent's production behavior observable and correlated. Define a trace schema,
ensure every trace carries the correlation keys from Lab 1, design the Azure Monitor /
Application Insights views, set alerts that turn signals into action, and close the loop
by promoting a reviewed trace into an eval row. By the end you can answer: *if this agent
produces a bad answer in production, can we find the trace, understand it, identify the
version, route it, and prevent it next time?*

## Why observability is central

For agents, the unit of understanding is the trace - the chain of decisions, not just the
endpoint status. Infrastructure monitoring asks "is the service healthy?"; agent
observability asks "what did it do and why?". Without correlation, observability is just
disconnected dashboards. With it, the same trace answers questions across release,
runtime, evaluation, and Day-2. See the
[observability strategy]({{ '/long/observability-strategy' | relative_url }}) for the full
thread.

## Prerequisites

- Labs 1-3 complete (correlation keys defined; release evidence started).
- The Application Insights resource linked to your Foundry project (from Lab 1).
- Azure Monitor / Log Analytics access.

## Concepts (15 min)

- **Trace schema:** user request, agent plan, model calls, retrieval, tool calls, safety
  events, response, feedback - each a span.
- **Correlation keys:** trace_id, session_id, agent_version, deployment_id, eval_run_id,
  release_id, owner. Every production trace must carry all seven.
- **Foundry vs application responsibility:** Foundry captures plan, model, tool, and
  safety spans via OpenTelemetry; the application adds business context (session, user
  intent, feedback) and the release metadata.
- **Signals to actions:** every signal maps to a concrete operational response, not just a
  chart.
- **The closed loop:** trace -> diagnose -> add eval row -> gate future release -> observe
  again. Production behavior becomes future evaluation coverage.

## Steps

### Step 1 - Define the trace schema (15 min)

Open the [observability correlation model template]({{ '/long/labs/templates/observability-correlation-model/' | relative_url }}).
For one representative interaction with your agent, list the spans you expect: request,
plan, model call(s), retrieval, tool call(s), safety event, response, feedback. For each
span, note the key attributes (model, tokens, latency, tool name/args/result/error).

### Step 2 - Wire the correlation keys (15 min)

For each of the seven correlation keys, decide where it comes from:

- `trace_id`, `session_id` - OpenTelemetry / application.
- `agent_version`, `deployment_id`, `eval_run_id`, `release_id` - release metadata from
  Labs 1-3, attached as span attributes or baggage.
- `owner` - from the agent target inventory.

Fill in the coverage check: what does Foundry capture automatically, and what must the
application add? The honest gap here is usually the release metadata - Foundry knows the
model, but not which `release_id` shipped it unless you attach it.

### Step 3 - Import telemetry into the workspace (10 min)

Bring Azure Monitor / Application Insights signals into the accelerator workspace so eval
and runtime live side by side:

```text
agentops telemetry validate <name>
agentops telemetry preview <name> --rows 20
agentops telemetry import <name> --apply
```

Confirm the imported rows carry your correlation keys. If `agent_version` or `release_id`
is missing, that is the instrumentation gap to record in the correlation model.

### Step 4 - Design the dashboards (15 min)

Open the [dashboard and alert plan template]({{ '/long/labs/templates/dashboard-and-alert-plan/' | relative_url }}).
Sketch four views:

1. **Executive readiness** - release status, gate result, open risks, recent incidents,
   safety status.
2. **Operations** - request volume, error rate, tool failures, latency p50/p95/p99,
   safety events, cost/tokens.
3. **Agent behavior** - trace samples, conversation outcomes, retrieval/tool paths, user
   feedback, quality trend.
4. **Continuous improvement** - regression candidates from traces, eval coverage gaps,
   red-team findings, open actions.

`agentops cockpit` gives you a local production-signal snapshot and links into the
matching Foundry and Azure Monitor views to anchor the design.

### Step 5 - Define alerts as actions (10 min)

For each alert in the template, write the signal, threshold, severity, and the runbook
action it triggers. Examples:

- Latency spike -> Azure Monitor alert -> on-call.
- Tool error rate -> disable tool, fall back to manual.
- Safety violation -> block plus content safety incident.
- Eval score drop -> pause canary, open ticket.
- Cost anomaly -> throttle via gateway, notify FinOps.

An alert without a runbook action is noise. Each one maps to a Lab 6 runbook entry.

### Step 6 - Close the loop (10 min)

Pick one real (or sample) production trace that shows a failure. Walk it: which span
broke, which version produced it, who owns it. Then promote it into the eval dataset:

```text
agentops eval promote-traces --source <trace-file> --apply
```

The new row enters the PR gate (Lab 3) so the same failure is caught before the next
release. Record the promoted trace in the correlation model.

## Artefacts

1. **Observability correlation model** - trace schema + seven correlation keys + coverage
   check.
2. **Dashboard and alert plan** - four views and the alert-to-action mapping.

## Observability metadata captured

This lab is where the metadata thread becomes real: every correlation key defined in Lab
1 is now present on a production trace and visible in a dashboard. Update the readiness
evidence package (Lab 3) section 4 with the App Insights link and "dashboards wired: yes".

## Time budget

| Step | Minutes |
|---|---:|
| Concepts | 15 |
| Trace schema | 15 |
| Wire correlation keys | 15 |
| Import telemetry | 10 |
| Design dashboards | 15 |
| Alerts as actions | 10 |
| Close the loop | 10 |

## Facilitator tips

- This is the lab to protect time for. If the morning ran long, cut elsewhere, not here.
- The recurring "aha" is the missing release metadata - Foundry traces alone cannot tell
  you which `release_id` shipped a behavior. Let attendees discover that gap in Step 2.
- Keep Step 6 concrete: one trace, one promoted row. That single loop is the point of the
  whole workshop.
- Have a sample trace file ready for attendees whose agents have no production traffic.

## Discussion prompts

- Today, given a bad answer, how long would it take you to find the exact trace?
- Which correlation key are you most likely missing in production right now?
- Which dashboard view would your leadership actually open?
- What was the last production failure you turned into a test? If never, why not?

## References

- [Trace agent overview](https://learn.microsoft.com/azure/ai-foundry/observability/concepts/trace-agent-concept)
- [Monitor agents dashboard](https://learn.microsoft.com/azure/ai-foundry/observability/how-to/how-to-monitor-agents-dashboard)
- [Application Insights monitoring](https://learn.microsoft.com/azure/ai-foundry/how-to/monitor-applications)
- [AgentOps Accelerator](https://github.com/Azure/agentops) - `agentops telemetry ...`, `agentops cockpit`, `agentops eval promote-traces`.
