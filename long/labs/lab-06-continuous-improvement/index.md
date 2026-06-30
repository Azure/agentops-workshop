---
title: "Lab 6: Incident Response and Continuous Improvement"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 6
---

# Lab 6: Incident Response and Continuous Improvement

## Where you are in the journey

In Lab 4, you used Foundry tracing and Azure Monitor / Application Insights to find a bad production trace for the Contoso Travel Agent. In Lab 5, you hardened the safety and governance evidence around the same agent.

Now you close the continuous improvement loop: take that real failure signal, turn it into a permanent regression test, fix the agent, and move the baseline forward so the same issue does not quietly return.

## Duration and you will build

**Duration:** 75 minutes

**You will build:** a simulated incident from the flagged trace, a trace promotion flow that creates a new regression row, a re-evaluation that catches the issue, a fixed `travel-agent` version, and an updated baseline and evidence pack.

## Prerequisites

Before you start, confirm you have:

- Completed Labs 1-5.
- Your `agentops-vbd\` folder still has `agentops.yaml` and `.agentops\`.
- Your dataset from Lab 2 exists at `.agentops\data\travel-smoke.jsonl`.
- Your baseline from Lab 2 or Lab 3 exists at `.agentops\baseline\results.json`.
- Your latest release evidence exists under `.agentops\release\latest\`.
- You noted one bad trace ID, operation ID, or replay link in Lab 4.
- PowerShell is open in the `agentops-vbd\` folder.
- These environment variables are set in the current terminal:

```powershell
$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
$env:AZURE_OPENAI_ENDPOINT = "https://<openai-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
```

Quick check:

```powershell
Get-Location
Test-Path agentops.yaml
Test-Path .agentops\data\travel-smoke.jsonl
Test-Path .agentops\baseline\results.json
agentops --version
```

Expected result: you are in `agentops-vbd\`, all three `Test-Path` commands return `True`, and the `agentops` CLI prints a version.

## Concepts in two minutes

- **Incident -> evidence -> regression test:** a production failure is not complete when it is explained. It is complete when the release gate can catch it next time.
- **Trace promotion:** AgentOps can convert reviewed Foundry or Application Insights trace exports into reviewable dataset rows with `agentops eval promote-traces --source FILE [--apply]`.
- **Human review still matters:** production output is not automatically correct. The promoted row is a candidate until you review the expected answer.
- **The dataset must grow from production:** the best regression tests often come from real user behavior, not only from examples invented before launch.
- **The loop:** Evaluate -> Ship -> Observe -> Operate -> back to Evaluate.
- **Baselines move forward:** after the fix passes, refresh `.agentops\baseline\results.json` so future releases are compared against the new, better bar.

## Step by step

### 1. Reproduce the incident from the bad trace

Open the trace you flagged in Lab 4 and capture exactly what failed.

Portal clicks:

1. Go to [https://ai.azure.com](https://ai.azure.com).
2. Open your Foundry project.
3. Open your `travel-agent` agent.
4. Go to **Traces**.
5. Search for the trace ID, operation ID, or replay link you saved in Lab 4.
6. Open the trace.
7. In the trace details, inspect the span tree, input, output, metadata, latency, model calls, tool calls if present, and any linked evaluation context.
8. If the trace is easier to investigate in Application Insights, open the connected App Insights resource, go to **Logs**, and query the same operation ID.

Use this KQL when you have an operation ID:

```powershell
# Paste this query into Application Insights Logs, not into PowerShell.
union traces, requests, dependencies
| where timestamp > ago(1h)
| where operation_Id == "<trace-or-operation-id>"
| order by timestamp asc
```

Create a short incident note in your terminal so you can use it during the lab:

```powershell
New-Item -ItemType Directory -Force .agentops\incidents | Out-Null
@'
# Mini incident review

Trace ID: <paste trace id or operation id>
Replay URL: <paste Foundry trace URL if available>

What failed:
<one sentence, for example: The agent gave a vague answer instead of a day-by-day itinerary.>

Impact:
<one sentence, for example: A traveler could not use the answer to plan the trip.>

Signal:
<one sentence, for example: Foundry trace showed low-quality output for a real user input after release.>

Exact user input:
<paste the user input from the trace>

Bad output:
<paste the bad assistant output from the trace>
'@ | Set-Content -Encoding utf8 .agentops\incidents\lab-06-incident-review.md
notepad .agentops\incidents\lab-06-incident-review.md
```

Expected result: `.agentops\incidents\lab-06-incident-review.md` contains the exact user input, the bad output, the trace ID, and a short explanation of impact and signal.

### 2. Get the trace into a promotable form

AgentOps trace promotion reads local JSON or JSONL trace export files. The docs describe this as reviewed Foundry or Application Insights traces that include fields such as input, response, trace ID, timestamp, replay URL, source system, and optional context.

Create a trace export folder:

```powershell
New-Item -ItemType Directory -Force .agentops\traces | Out-Null
```

If you can export the trace during the workshop, save the reviewed export as:

```text
.agentops\traces\candidate-traces.jsonl
```

Use a JSONL shape like this. Keep one JSON object per line.

```powershell
@'
{"operation_Id":"<trace-or-operation-id>","trace_replay_url":"<Foundry trace URL>","agent":"travel-agent","agent_version":"1","customDimensions":{"source_system":"foundry","input":"<exact user input from the trace>","response":"<bad output from the trace>"}}
'@ | Set-Content -Encoding utf8 .agentops\traces\candidate-traces.jsonl
```

If live export is not available in the room, use this ready-made source file. It represents a flagged case where the Travel Agent answered too vaguely.

```powershell
@'
{"operation_Id":"lab4-bad-trace-001","trace_replay_url":"https://ai.azure.com/traces/lab4-bad-trace-001","agent":"travel-agent","agent_version":"1","sampling_policy":"workshop-reviewed","customDimensions":{"source_system":"foundry","input":"Plan a 4-day family trip to Barcelona with two kids, a moderate budget, and a preference for history and beaches.","response":"Barcelona is nice for families. Look online for attractions and choose what you like."}}
'@ | Set-Content -Encoding utf8 .agentops\traces\candidate-traces.jsonl
```

Open the file:

```powershell
Get-Content .agentops\traces\candidate-traces.jsonl
```

Expected result: the file exists and contains one JSON object with an `input`, a `response`, and lineage fields such as `operation_Id` or `trace_replay_url`.

### 3. Preview the trace promotion

Preview first. Do not use `--apply` yet.

```powershell
agentops eval promote-traces --source .agentops\traces\candidate-traces.jsonl
```

Expected result: the command prints an `AgentOps trace-to-dataset preview` summary. It shows the source file, the output dataset candidate path, the number of rows, the number skipped, the label mode, warnings, and sample row inputs. Because this is a preview, no dataset file is written.

Important teaching point: the preview proposes dataset rows derived from the trace input and response. It does not prove the response is correct. The row still needs review before it becomes a release gate.

### 4. Apply the promotion and add the reviewed row to `travel-smoke.jsonl`

Apply the promotion:

```powershell
agentops eval promote-traces --source .agentops\traces\candidate-traces.jsonl --apply
```

Expected result: AgentOps writes reviewable regression candidates under `.agentops\data\`, including a trace regression dataset and a provenance manifest. The manifest records lineage such as source file, row count, trace IDs, replay URLs, source systems, agent versions, and whether human review is required.

Open the promoted candidate file:

```powershell
Get-Content .agentops\data\trace-regression.jsonl
Get-Content .agentops\data\trace-regression-manifest.json
```

Expected result: `trace-regression.jsonl` contains a new row with `input`, `expected`, and `metadata`. The metadata includes `needs_review` because the production response is not automatically trusted as ground truth.

Now review the candidate and append the corrected regression row to the same dataset you created in Lab 2: `.agentops\data\travel-smoke.jsonl`.

For the ready-made source file, use this reviewed row:

```powershell
@'
{"id":"trace-lab4-bad-trace-001","input":"Plan a 4-day family trip to Barcelona with two kids, a moderate budget, and a preference for history and beaches.","expected":"A concise 4-day Barcelona family itinerary with kid-friendly history stops, beach time, moderate-budget tips, transit or pacing notes, and a reminder that the agent cannot make live bookings.","metadata":{"source":"production_trace","trace_id":"lab4-bad-trace-001","needs_review":false,"reviewed_in_lab":"lab-06-continuous-improvement"}}
'@ | Add-Content -Encoding utf8 .agentops\data\travel-smoke.jsonl
```

If you used your own trace, append a reviewed row with the exact trace input and the corrected expected answer your team wants the fixed agent to produce:

```powershell
@'
{"id":"trace-<your-trace-id>","input":"<exact user input from the trace>","expected":"<correct answer or acceptance criteria the fixed agent must satisfy>","metadata":{"source":"production_trace","trace_id":"<your-trace-id>","needs_review":false,"reviewed_in_lab":"lab-06-continuous-improvement"}}
'@ | Add-Content -Encoding utf8 .agentops\data\travel-smoke.jsonl
```

Confirm the dataset grew:

```powershell
Get-Content .agentops\data\travel-smoke.jsonl | Select-Object -Last 3
```

Expected result: the last lines of `travel-smoke.jsonl` include the new regression row derived from the reviewed trace. This is the handoff back to Lab 2: the original smoke dataset is now a living production-informed dataset.

### 5. Re-evaluate and watch the new case catch the issue

First, run the eval against the current version. If the agent still behaves like the bad trace, this run should fail or show a regression. That is the point.

```powershell
agentops eval run --baseline .agentops\baseline\results.json
code .agentops\results\latest\report.md
```

Expected result: `agentops eval run` writes updated results under `.agentops\results\latest\`. If the current `travel-agent` still fails the new row, the command can exit with code `2` for threshold failure, and the report should make the new regression visible. Exit code `2` means the quality gate caught the issue, not that the CLI crashed.

If you want to make the failure obvious for teaching, temporarily point `agentops.yaml` to the still-bad agent version from Lab 4 or Lab 5. For example:

```powershell
notepad agentops.yaml
```

Set the agent back to the known bad version if you have it:

```yaml
agent: "travel-agent:1"
dataset: .agentops/data/travel-smoke.jsonl
```

Then run the eval again:

```powershell
agentops eval run --baseline .agentops\baseline\results.json
```

Expected result: the new Barcelona row should be part of the gate, and the bad version should not be release-ready.

Now fix the agent in Foundry.

Portal clicks:

1. Go to [https://ai.azure.com](https://ai.azure.com).
2. Open your Foundry project.
3. Open the `travel-agent` agent.
4. Edit the instructions so the agent always includes:
   - a short summary;
   - a day-by-day plan when asked for an itinerary;
   - practical notes about budget, transit, weather, pacing, or booking constraints;
   - a reminder that it cannot make live reservations or purchases.
5. Test the exact incident input in the playground.
6. Publish the fixed version. Use the exact version Foundry shows, for example `travel-agent:2`.
7. Update `agentops.yaml` to point at the fixed version.

```powershell
notepad agentops.yaml
```

Example:

```yaml
version: 1
agent: "travel-agent:2"
dataset: .agentops/data/travel-smoke.jsonl
```

Re-run until the gate is green:

```powershell
agentops eval run --baseline .agentops\baseline\results.json
code .agentops\results\latest\report.md
```

Expected result: the fixed agent passes the eval with the new regression row included. The report includes the latest scores and, when available, a comparison against `.agentops\baseline\results.json`.

### 6. Move the baseline forward and record the improvement

Once the fixed version passes, refresh the baseline. This is the quality ratchet: the new, better behavior becomes the bar future versions must meet.

```powershell
New-Item -ItemType Directory -Force .agentops\baseline | Out-Null
Copy-Item .agentops\results\latest\results.json .agentops\baseline\results.json -Force
```

Expected result: `.agentops\baseline\results.json` now reflects the passing run that includes the promoted regression row.

Run Doctor and rebuild the evidence pack:

```powershell
agentops doctor --evidence-pack
code .agentops\release\latest\evidence.md
```

Expected result: AgentOps updates the Doctor findings and release evidence under `.agentops\release\latest\`. The evidence now reflects the improved dataset, the latest eval run, and the refreshed baseline.

### 7. Make continuous improvement a habit

Use this cadence after launch:

1. Review Foundry traces and Application Insights signals every week, or after every incident.
2. Pick representative failures, confusing answers, safety misses, or expensive interactions.
3. Promote reviewed traces with:

```powershell
agentops eval promote-traces --source .agentops\traces\candidate-traces.jsonl
agentops eval promote-traces --source .agentops\traces\candidate-traces.jsonl --apply
```

4. Review the candidate rows. Add corrected expected answers before they become blocking gates.
5. Append approved rows to `.agentops\data\travel-smoke.jsonl` or your team-owned dataset.
6. Fix the agent in Foundry or in your hosted endpoint.
7. Re-run `agentops eval run --baseline .agentops\baseline\results.json`.
8. Refresh `.agentops\baseline\results.json` only after the improved run is green.
9. Re-run `agentops doctor --evidence-pack` so release evidence keeps up.

Ownership model:

| Activity | Primary owner | Review partner |
|---|---|---|
| Trace review | Service owner or support engineer | AI engineer |
| Expected answer labeling | Product owner or domain expert | AI engineer |
| Agent fix | AI engineer | Architect |
| Baseline refresh | Platform or DevOps owner | Service owner |
| Evidence review | Release owner | Governance stakeholder |

Expected result: the team can explain who reviews traces, who labels expected behavior, who fixes the agent, who refreshes the baseline, and how the evidence pack is kept current. This is Day-2 operations.

## Checkpoint

Run this verification block:

```powershell
Write-Host "Dataset rows:"
(Get-Content .agentops\data\travel-smoke.jsonl).Count

Write-Host "Latest regression row:"
Get-Content .agentops\data\travel-smoke.jsonl | Select-Object -Last 1

Write-Host "Latest eval files:"
Test-Path .agentops\results\latest\results.json
Test-Path .agentops\results\latest\report.md

Write-Host "Baseline refreshed:"
Test-Path .agentops\baseline\results.json

Write-Host "Evidence refreshed:"
Test-Path .agentops\release\latest\evidence.json
Test-Path .agentops\release\latest\evidence.md
```

Expected result:

- `travel-smoke.jsonl` contains a new row derived from a real or simulated production trace.
- `agentops eval run --baseline .agentops\baseline\results.json` passes after the agent fix.
- `.agentops\baseline\results.json` has been refreshed from the latest passing run.
- `agentops doctor --evidence-pack` updated the release evidence.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `promote-traces` says no usable input/response pairs were found | The source trace file does not contain fields AgentOps can map, such as `input`, `response`, `customDimensions.input`, or `customDimensions.response` | Open `.agentops\traces\candidate-traces.jsonl`, compare it with the sample shape in Step 2, and make sure each line is valid JSON with input and response text. |
| You ran `promote-traces` but no file was written | You previewed without `--apply` | Run `agentops eval promote-traces --source .agentops\traces\candidate-traces.jsonl --apply` after reviewing the preview. |
| The new row makes `agentops eval run` fail | Expected behavior - the row captured a real gap and the current agent still fails it | Fix the agent in Foundry, publish the new version, update `agentops.yaml`, and re-run until green. |
| The eval passes but still seems to reward the bad output | The promoted production response was treated as expected before human review | Edit or append a reviewed row where `expected` describes the corrected answer you want, not the bad answer you observed. |
| Baseline comparison still points to the old bar | `.agentops\baseline\results.json` was not refreshed after the fixed green run | Run `Copy-Item .agentops\results\latest\results.json .agentops\baseline\results.json -Force` only after the improved run passes. |
| Doctor evidence does not show the latest result | Evidence was not regenerated after the eval and baseline refresh | Run `agentops doctor --evidence-pack` again and reopen `.agentops\release\latest\evidence.md`. |

## What you just learned

- Production failures can become permanent regression tests.
- The eval dataset is a living asset, not a one-time Lab 2 file.
- Baselines ratchet quality upward after a fix is proven.
- The AgentOps loop never ends: Operate feeds Evaluate so the next release is safer than the last.

## Carry into the capstone

You have run the full loop once on `travel-agent`. The Capstone wires it into CI/CD and produces the final production-readiness evidence pack for a ship / no-ship decision.
