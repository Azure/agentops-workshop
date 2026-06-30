---
title: "Lab 4: Observability and Trace-Driven Operations"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 4
---

# Lab 4: Observability and Trace-Driven Operations

## Where you are in the journey

In Labs 1-3, you created the Contoso Travel Agent, evaluated `travel-agent:1`, shipped a changed version with a gate, and produced release evidence in `.agentops\release\latest\`. That is enough to make a release decision, but it is not enough to operate the agent after real users arrive.

Now the Travel Agent is treated as "in production." Your job is to see what it is doing: traces, spans, telemetry, latency, errors, token usage, and the first feedback loop from a real trace back into future evaluation coverage.

## Duration

90 minutes

## You will build

You will enable or confirm Foundry and Application Insights tracing for the Travel Agent, generate a real trace, inspect the same interaction in Foundry and Application Insights, import telemetry candidates into the AgentOps workspace, open Cockpit as the local command center, and identify one bad trace to carry into Lab 6.

## Prerequisites

Before you start, confirm each item. Do not skip this list. Most observability failures are setup failures.

- Completed Lab 3, and your `agentops-vbd\` folder still has `agentops.yaml` and `.agentops\`.
- The Travel Agent exists in Microsoft Foundry and is referenced by `agentops.yaml`, typically as `agent: "travel-agent:1"` or the version you shipped in Lab 3.
- The Lab 3 evidence pack exists:
  - `.agentops\release\latest\evidence.json`
  - `.agentops\release\latest\evidence.md`
- You are signed in to Azure CLI with the tenant that owns the Foundry project.
- These environment variables are set in the terminal where you run AgentOps commands:
  - `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"`
  - `AZURE_OPENAI_ENDPOINT = "https://<openai-resource>.openai.azure.com"`
  - `AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"`
- For Cockpit and agent-facing features, the optional agent extra is installed:

```powershell
cd agentops-vbd
python -m pip install "agentops-accelerator[agent]"
agentops --version
```

Expected result: The install succeeds and `agentops --version` prints the installed AgentOps CLI version.

- An Application Insights resource is connected to the Foundry project. You will confirm this in Step 1.
- You have permission to read the Application Insights resource and its backing Log Analytics workspace. Reader is enough for this lab.
- You can open the Azure portal and Microsoft Foundry portal in a browser.

Useful public references for this lab:

- Azure/agentops README: <https://raw.githubusercontent.com/Azure/agentops/main/README.md>
- Azure/agentops concepts: <https://raw.githubusercontent.com/Azure/agentops/main/docs/concepts.md>
- Azure/agentops how it works: <https://raw.githubusercontent.com/Azure/agentops/main/docs/how-it-works.md>
- Azure/agentops end-to-end tutorial: <https://raw.githubusercontent.com/Azure/agentops/main/docs/tutorial-end-to-end.md>
- Azure/agentops evaluation and telemetry import: <https://raw.githubusercontent.com/Azure/agentops/main/docs/evaluation.md>
- Foundry tracing concepts and setup: <https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/develop/trace-agents-sdk>
- Application Insights transaction search and diagnostics: <https://learn.microsoft.com/en-us/azure/azure-monitor/app/failures-performance-transactions>
- Azure Monitor alerts overview: <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview>

## Concepts in two minutes

- **Control plane vs runtime observability layer.** Microsoft Foundry is the control plane for agents, evaluations, tracing entry points, operations views, safety, and investigation. Azure Monitor and Application Insights are the runtime observability layer where telemetry, transactions, dependencies, traces, logs, and alerts are stored and queried.
- **Trace.** A trace is one end-to-end request or workflow. For an agent, it answers: what did the user ask, what did the agent do, which model or tool calls happened, how long did each step take, what failed, and what answer came back?
- **Span.** A span is one operation inside a trace. In an agent trace, common spans include input handling, model call, tool call, retrieval call, safety check, and response generation.
- **Attributes.** Attributes are key-value facts on spans, such as latency, token counts, model deployment, tool name, status code, trace ID, or agent version.
- **Telemetry as evidence.** Evaluation results prove what happened before release. Telemetry proves what happened after release. AgentOps connects both into release evidence.
- **Trace-to-evaluation feedback loop.** A weak production answer should not stay as tribal knowledge. You capture the trace ID, review it, promote it into a regression candidate later, and make the next release gate catch it.
- **Cockpit.** Cockpit is a local command center for the current AgentOps workspace. It shows local eval history, Doctor findings, evidence, observability readiness, telemetry status, and links back to Foundry and Azure Monitor.

## Step by step

### 1. Enable or confirm tracing in Foundry

Start in the portal because runtime observability must be connected before AgentOps can reason about it.

Portal clicks:

1. Open <https://ai.azure.com>.
2. Select the Foundry project you used in Labs 1-3.
3. In the project left navigation, open **Tracing** or the project's observability area.
4. Confirm that an **Application Insights** resource is connected.
5. If no resource is connected, choose **Create new** or **Connect existing**, select the subscription and resource group, and attach an Application Insights resource.
6. Open the Travel Agent from the project.
7. Look for the agent run or trace view where agent executions appear.

Foundry tracing is based on OpenTelemetry concepts. Microsoft Learn describes traces as the journey of a request and spans as the operations inside that trace. Foundry exports those traces to Azure Monitor when Application Insights is connected.

Run this local check after you confirm the portal wiring:

```powershell
cd agentops-vbd
az login
$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
$env:AZURE_OPENAI_ENDPOINT = "https://<openai-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
agentops eval analyze
```

Expected result: Foundry shows an attached Application Insights resource, and `agentops eval analyze` can read the local eval configuration without reporting missing Azure environment variables.

### 2. Generate live traffic for the Travel Agent

You need fresh traffic so there is something to inspect. Use the Foundry playground or Agents test pane so the run is produced by the real agent surface.

Portal clicks:

1. In Foundry, open the Travel Agent.
2. Open **Playground**, **Test**, or the agent test pane.
3. Send these prompts one at a time:
   - `Plan a 3-day first-time trip to Lisbon for a couple who likes food and history.`
   - `Suggest a low-budget weekend in Seattle for a solo traveler who likes coffee and museums.`
   - `I want to visit Tokyo for 5 days with two kids. What should we do?`
4. Wait one or two minutes.
5. Return to the project **Tracing** or agent run view.
6. In the Azure portal, open the connected Application Insights resource.
7. Open **Investigate** > **Transaction search** or **Search**.
8. Set the time range to **Last 30 minutes**.

Expected result: At least one Travel Agent run appears in the Foundry tracing view. Within a minute or two, related telemetry appears in Application Insights Search or Transaction search. If it does not appear immediately, wait up to five minutes before troubleshooting.

### 3. Inspect one trace end to end

Pick one run and read it slowly. The goal is not to admire the portal. The goal is to prove that an operator can explain a single answer.

Portal clicks in Foundry:

1. Open the project **Tracing** or agent trace view.
2. Select one recent Travel Agent run.
3. Copy the trace ID or operation ID if the portal exposes it.
4. Expand the span tree.
5. Start at the top span and read downward:
   - user input;
   - agent or orchestration span;
   - model call span;
   - tool or retrieval span, if present;
   - final output span.
6. For each important span, look for:
   - duration or latency;
   - status or error;
   - model deployment;
   - token counts, if shown;
   - tool name and arguments, if a tool was used;
   - response content or output metadata.

Portal clicks in Application Insights:

1. Open the connected Application Insights resource in the Azure portal.
2. Open **Investigate** > **Transaction search** or **Search**.
3. Set the time range to **Last 30 minutes**.
4. Search for the trace ID, operation ID, agent name, or a distinctive prompt word such as `Lisbon`.
5. Select a matching telemetry item.
6. Open **End-to-end transaction details**.
7. Compare the operation timeline with the Foundry span tree.
8. If you need raw query detail, choose **View in Logs** and inspect the related operation in Log Analytics.

Optional KQL for the Logs view:

```powershell
# Paste this query into the Application Insights Logs editor, not into PowerShell.
# Replace <trace-or-operation-id> with the trace ID or operation ID you copied.
union traces, requests, dependencies
| where timestamp > ago(1h)
| where operation_Id == "<trace-or-operation-id>"
| order by timestamp asc
```

Microsoft Learn reference: Application Insights Search helps locate individual telemetry items, and Transaction diagnostics helps investigate end-to-end transaction details across related telemetry. See <https://learn.microsoft.com/en-us/azure/azure-monitor/app/failures-performance-transactions>.

Expected result: You can explain one agent answer from input to output, including where time was spent, whether model or tool calls happened, whether any error occurred, and where the same operation appears in Application Insights.

### 4. Bring telemetry into the AgentOps workspace

AgentOps telemetry import is the bridge from production observation to future evaluation coverage. It does not declare that production answers are correct. It creates reviewable dataset candidates with lineage.

First, configure a named telemetry import. If your instructor already provided one in `agentops.yaml`, use that name and skip the edit. If not, add a block like this to `agentops.yaml` and replace the placeholders with your resource ID and field mappings.

```yaml
telemetry_imports:
  - name: prod-agent-traces
    target: application-insights
    resource_id: $APPINSIGHTS_RESOURCE_ID
    time_range:
      lookback_days: 1
    filters:
      customDimensions.agent: travel-agent
    fields:
      input: customDimensions.question
      response: customDimensions.answer
      trace_id: operation_Id
    output:
      path: .agentops/data/prod-agent-trace-candidates.jsonl
      label_mode: pending
```

Set the Application Insights resource ID in your shell. You can copy it from the Azure portal resource **Properties** page.

```powershell
cd agentops-vbd
$env:APPINSIGHTS_RESOURCE_ID = "/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/microsoft.insights/components/<app-insights-name>"
```

Now run the three telemetry commands shown in the AgentOps documentation.

```powershell
agentops telemetry validate prod-agent-traces
```

Expected result: AgentOps validates that the named import exists and that the configuration shape is usable before it queries Azure.

```powershell
agentops telemetry preview prod-agent-traces --rows 10
```

Expected result: AgentOps previews up to 10 rows from Azure Monitor or Application Insights so you can confirm the input, response, trace ID, and metadata mappings before writing files.

```powershell
agentops telemetry import prod-agent-traces --apply
```

Expected result: AgentOps writes the imported telemetry candidates to the configured output path under `.agentops\`, for this lab `.agentops\data\prod-agent-trace-candidates.jsonl`. The import also preserves lineage metadata such as trace ID, timestamp, source system, and replay or investigation links when available.

Open the imported candidate file:

```powershell
code .agentops\data\prod-agent-trace-candidates.jsonl
```

Expected result: The file opens in VS Code. Rows are candidates for human review, not approved ground truth. In `pending` label mode, the expected answer is intentionally empty or review-oriented until a human decides what the correct behavior should be.

### 5. Open Cockpit, the local command center

Cockpit gives the operator a single local command center for the current workspace. It combines repo-side evidence with links back to Foundry and Azure Monitor.

```powershell
cd agentops-vbd
agentops cockpit
```

Expected result: The command starts a local web server and prints a localhost URL, commonly `http://127.0.0.1:8090`. Open that URL in your browser. Press `Ctrl+C` in the terminal when you are done.

In Cockpit, review these sections top to bottom:

- **Foundry connection** - confirm the project, tenant, agent, and App Insights connection.
- **Foundry launchpad** - use links to jump back to the agent, project, and telemetry surfaces.
- **Observability readiness** - confirm tracing, telemetry discovery, evals, red-team readiness, and alert readiness.
- **AgentOps Doctor** - review the latest readiness findings.
- **Eval gate summary** - confirm the Lab 2 and Lab 3 evaluation runs are visible.
- **Quality gate summary** - review score trends and regressions.
- **Production signal** - check the App Insights health snapshot or the clear no-traffic state.
- **CI/CD Pipelines** - confirm the generated workflows or known gaps.
- **Next actions** - read the prioritized follow-up list.

Expected result: Cockpit opens locally and shows your workspace state. It should help you answer: what was evaluated, what evidence exists, whether telemetry is connected, and where to drill into official Foundry and Azure Monitor runtime views.

### 6. Close the loop by flagging one poor trace

Now make the Observe pillar actionable. Pick one trace where the agent did something weak, incomplete, slow, confusing, or risky.

Examples of a trace worth flagging:

- The user asked for a day-by-day itinerary, but the agent returned vague advice.
- The answer omitted the booking caveat.
- The trace shows high latency on the model call.
- A tool call failed or returned empty data.
- The answer was correct but too expensive because it used too many tokens.
- The response was safe but not useful enough for the travel-support scenario.

Create a small local note inside the AgentOps workspace so the next labs know which trace you chose.

```powershell
cd agentops-vbd
New-Item -ItemType Directory -Force .agentops\notes | Out-Null
$flaggedTrace = @(
  "trace_id: <paste-trace-or-operation-id>",
  "why_flagged: <one sentence explaining what went poorly>",
  "source: Foundry tracing and Application Insights",
  "next_action: Review in Lab 6 and decide whether to promote into the eval dataset."
)
$flaggedTrace | Set-Content -Encoding utf8 .agentops\notes\lab-04-flagged-trace.txt
code .agentops\notes\lab-04-flagged-trace.txt
```

Expected result: `.agentops\notes\lab-04-flagged-trace.txt` contains one trace ID and one plain-English reason. In Lab 6, you will use this trace as the candidate for trace-to-evaluation promotion.

### 7. Define one operational guardrail in Azure Monitor

Observability is incomplete if nobody is notified when the agent degrades. Define one alert you would create for the Travel Agent. You do not need to save the alert during this lab unless your instructor tells you to, but you must know exactly what you would alert on and why.

Recommended first guardrail:

- Alert when failed agent operations exceed an agreed threshold, because users experience failed operations as broken support.

Alternative guardrail:

- Alert when P95 latency exceeds the target for several evaluation periods, because slow agents reduce trust and can hide model, retrieval, or tool dependency problems.

Portal clicks:

1. Open the Azure portal.
2. Open the connected Application Insights resource.
3. Select **Monitoring** > **Alerts**.
4. Select **Create** > **Alert rule**.
5. Confirm the Application Insights resource is the scope.
6. Choose a signal that matches your guardrail, such as failed requests, server response time, or a log search query over `requests`, `dependencies`, or `traces`.
7. Set the condition threshold.
8. Choose or create an action group for notification.
9. Name the alert with the agent and signal, for example `travel-agent-prod-p95-latency`.
10. Stop before creating if this is a shared workshop subscription and your instructor did not ask you to save it.

Microsoft Learn reference: Azure Monitor alert rules combine a resource, a signal, conditions, and an action group. Alerts can use metric data or log data. See <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview>.

Expected result: You can state one concrete alert in this format: "For `travel-agent`, alert when `<signal>` is `<condition>` for `<time window>`, notify `<owner/action group>`, because `<user or business impact>`."

## Checkpoint

You are done when all of these are true:

- At least one Travel Agent trace is visible in the Foundry tracing view.
- The same operation, trace, transaction, or related telemetry is visible in Application Insights Search, Transaction search, End-to-end transaction details, or Logs.
- `agentops telemetry validate prod-agent-traces` ran successfully.
- `agentops telemetry preview prod-agent-traces --rows 10` showed mapped rows or an understandable no-data result tied to your time range or filters.
- `agentops telemetry import prod-agent-traces --apply` wrote the configured candidate file under `.agentops\`.
- `agentops cockpit` opened the local command center.
- `.agentops\notes\lab-04-flagged-trace.txt` records one trace ID or operation ID to revisit in Lab 6.

Quick local verification:

```powershell
cd agentops-vbd
Test-Path .agentops\release\latest\evidence.md
Test-Path .agentops\data\prod-agent-trace-candidates.jsonl
Test-Path .agentops\notes\lab-04-flagged-trace.txt
```

Expected result: Each command returns `True`. If the telemetry file is not present because the preview had no rows, keep the validated import configuration and record the no-data reason in your flagged-trace note.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| No traces appear in Foundry. | Application Insights is not connected, tracing is not enabled for the project or runtime, the wrong project is open, or the run has not been ingested yet. | Reopen the project in <https://ai.azure.com>, confirm **Tracing** has an attached Application Insights resource, generate a fresh playground run, and wait 2-5 minutes. |
| Traces appear in Foundry but not in Application Insights. | You are looking at the wrong Application Insights resource, the time range is too narrow, telemetry sampling retained only some items, or ingestion is delayed. | Open the App Insights resource linked from Foundry, set time range to **Last 30 minutes** or **Last 24 hours**, search by trace ID or prompt keyword, and check Search plus Logs. |
| `agentops telemetry validate` says the import name is unknown. | `agentops.yaml` does not contain a `telemetry_imports` entry with that `name`. | Add the `telemetry_imports` block from Step 4 or use the exact name your instructor provided. |
| `agentops telemetry preview` returns no rows. | The time range, filters, field mappings, or Application Insights resource ID do not match the actual telemetry. | Temporarily widen `lookback_days`, remove narrow filters, verify `$env:APPINSIGHTS_RESOURCE_ID`, and confirm the same operation exists in Application Insights first. |
| `agentops telemetry import` fails with permissions errors. | Your Azure identity can see Foundry but cannot read Application Insights or the backing Log Analytics workspace. | Ask for Reader access on the Application Insights resource and its workspace, then run `az login` again in the same terminal. |
| `agentops cockpit` is not recognized or the command is missing. | The optional agent extra is not installed in this Python environment. | Run `python -m pip install "agentops-accelerator[agent]"`, then rerun `agentops --version` and `agentops cockpit`. |
| Cockpit opens but shows missing telemetry. | Doctor or Cockpit cannot discover the App Insights connection, or the workspace env is incomplete. | Confirm the Foundry connection, set `APPLICATIONINSIGHTS_CONNECTION_STRING` in `.agentops\.env` only if your instructor approves, rerun Doctor if needed, and reopen Cockpit. |
| Transaction search seems to miss the run you just created. | Clock, timezone, or ingestion delay confusion. | Use **Last 24 hours**, sort by newest first, and search by prompt keyword as well as trace ID. Remember that portal times may display in local time while logs are stored in UTC. |
| You see sensitive prompt or customer data in traces. | Content recording or custom attributes are capturing too much payload. | Do not copy sensitive payloads into the repo. Redact before importing. Keep only safe metadata and reviewed examples. |

## What you just learned

- Foundry is the agent control plane, while Azure Monitor and Application Insights are the runtime observability layer.
- A trace explains one agent interaction through spans: input, model call, tool or retrieval call, output, latency, tokens, and errors.
- Telemetry is release evidence after deployment, not just operational noise.
- AgentOps can validate, preview, and import telemetry candidates into `.agentops\` so real traces can become future regression coverage.
- Cockpit is a local command center that connects eval history, Doctor findings, evidence, telemetry readiness, and links to official runtime views.
- The Observe pillar is the heart of AgentOps because it turns production behavior into the next improvement loop.

## Carry into the next lab

You can now see the agent in production and you flagged a bad trace. Lab 5 hardens it - safety, red-team follow-through, and governance evidence - before Lab 6 feeds that bad trace back into evaluation.

