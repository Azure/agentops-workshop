---
title: "Lab 2: Evaluation Design"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 2
---

# Lab 2: Evaluation Design

## Where you are in the journey

In Lab 1, you created the Contoso Travel Agent in Microsoft Foundry as `travel-agent:1`. You also initialized the AgentOps accelerator workspace, so your `agentops-vbd\` folder now has `agentops.yaml` and `.agentops\`.

In this lab, you turn that working agent into something measurable. You will design the first evaluation gate that decides whether `travel-agent:1` is good enough to ship.

## Duration and what you will build

Duration: 75 minutes.

You will build a JSONL evaluation dataset, choose metrics and thresholds, run your first evaluation against `travel-agent:1`, read the report, and capture a baseline for the next lab.

## Prerequisites

Before you start, make sure you have:

- Completed Lab 1.
- Opened PowerShell in your `agentops-vbd\` folder.
- An `agentops.yaml` file at the folder root.
- A `.agentops\` folder created by `agentops init`.
- `agent: "travel-agent:1"` still set in `agentops.yaml`.
- The same three Foundry environment variables still set in this shell.

If you opened a new terminal, set the environment variables again:

```powershell
$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
$env:AZURE_OPENAI_ENDPOINT = "https://<openai-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
```

Expected result: PowerShell accepts the commands without output. The variables are available to `agentops eval analyze` and `agentops eval run`.

## Concepts in two minutes

- **Dataset row** - one JSON object per line in a `.jsonl` file. The beginner shape is `{"id","input","expected"}`. Some scenarios also use `context`, `tool_calls`, or `tool_definitions`.
- **Evaluator** - a scoring function. AI-assisted Foundry judges can score coherence, fluency, similarity, groundedness, relevance, retrieval, and safety. Local metrics include values such as `avg_latency_seconds` and `F1ScoreEvaluator`.
- **Threshold** - a rule in `agentops.yaml` that turns a metric into a gate, for example `coherence: ">=3"` or `avg_latency_seconds: "<=2"`.
- **Exit code** - `0` means pass, `2` means a threshold failed, and `1` means the run hit an error.
- **Evaluation scenario** - AgentOps auto-selects common evaluator patterns from the target and dataset shape. For a Foundry prompt agent with `input` and `expected`, start with answer quality. If rows include `context`, RAG evaluators can be selected. If rows include tool fields, agent workflow evaluators become possible.

## Step by step

### 1. Create the smoke evaluation dataset

Create the dataset folder and write a small travel Q&A dataset. Each row is one test case. Keep it simple and realistic.

```powershell
New-Item -ItemType Directory -Force .agentops\data | Out-Null
@'
{"id":"baggage-allowance-001","input":"What is the standard checked baggage allowance for an economy ticket from Seattle to London?","expected":"Explain that baggage allowance depends on the airline and fare class, and advise the traveler to check the booking details or airline policy before departure."}
{"id":"visa-001","input":"Do I need a visa for a short business trip from the United States to Canada?","expected":"Explain that visa requirements depend on citizenship, passport, trip purpose, and current government rules, and recommend checking official Canadian entry guidance before booking."}
{"id":"itinerary-001","input":"Create a simple three-day itinerary for a first-time visitor to Lisbon who likes food, history, and walking.","expected":"Provide a practical three-day Lisbon itinerary with food, history, and walking activities, without claiming to make bookings."}
{"id":"delay-001","input":"My flight was delayed overnight. What should I ask the airline for at the airport?","expected":"Suggest asking about rebooking, hotel or meal support, baggage handling, written delay confirmation, and the airline's compensation policy."}
{"id":"family-seating-001","input":"How can I increase the chance that my family sits together on a flight?","expected":"Recommend selecting seats early, checking the airline family seating policy, contacting the airline, arriving early, and confirming seats before boarding."}
{"id":"travel-insurance-001","input":"Should I buy travel insurance for an international trip with prepaid hotels and tours?","expected":"Explain common coverage areas such as cancellation, medical emergencies, delays, and lost baggage, and recommend comparing policy terms and exclusions."}
'@ | Set-Content -Encoding utf8 .agentops\data\travel-smoke.jsonl
```

Expected result: The file `.agentops\data\travel-smoke.jsonl` exists and contains 6 lines.

Verify the row count:

```powershell
Get-Content .agentops\data\travel-smoke.jsonl | Measure-Object -Line
```

Expected result: The `Lines` value is `6`.

### 2. Point `agentops.yaml` at the dataset and add thresholds

Open the config file:

```powershell
notepad .\agentops.yaml
```

Make sure the file includes these lines. Keep any existing Foundry settings that Lab 1 added.

```yaml
version: 1
agent: "travel-agent:1"
dataset: .agentops/data/travel-smoke.jsonl

thresholds:
  coherence: ">=3"
  avg_latency_seconds: "<=2"
```

Expected result: `agentops.yaml` connects `travel-agent:1` to `.agentops/data/travel-smoke.jsonl` and includes a small threshold gate.

Why these two thresholds:

- `coherence: ">=3"` asks the judge to check whether answers are logically consistent.
- `avg_latency_seconds: "<=2"` adds a local performance signal so quality is not the only release concern.

### 3. Analyze evaluation readiness

Run the readiness check:

```powershell
agentops eval analyze
```

Expected result: AgentOps checks evaluation readiness for the current workspace. A ready workspace should show that the config, dataset, target, credentials, and evaluator setup can be used for an evaluation.

If the workspace is not ready, fix the item named in the output, then run the command again. Common fixes are:

- Re-set the Foundry environment variables in this PowerShell session.
- Fix the `dataset:` path in `agentops.yaml`.
- Fix malformed JSONL by making sure each line is one complete JSON object.
- Confirm that the judge model deployment named by `AZURE_OPENAI_DEPLOYMENT` exists in your Foundry project.

### 4. Run the first evaluation

Run the evaluation:

```powershell
agentops eval run
$LASTEXITCODE
```

Expected result: AgentOps sends each dataset row to the Foundry target, scores the responses, applies thresholds, and writes outputs under `.agentops\results\latest\`. The final line prints the exit code.

Use the exit code this way:

- `0` - the evaluation passed.
- `2` - the run completed, but at least one threshold failed.
- `1` - the run hit an error, such as auth, endpoint, model, or malformed input.

Open the human-readable report:

```powershell
notepad .agentops\results\latest\report.md
```

Expected result: `report.md` opens. Read the summary first, then review the per-metric scores and any pass/fail status. The machine-readable result is next to it at `.agentops\results\latest\results.json`.

If the exit code is `2`, do not treat that as a broken tool. It means the quality gate worked and found a threshold failure. Read the report, decide whether the threshold is too strict or the agent answer needs improvement, then re-run the evaluation after the fix.

### 5. Capture the baseline

After you get a successful first run, copy the latest `results.json` into the baseline folder. This uses the same baseline capture shape shown in the accelerator README.

```powershell
New-Item -ItemType Directory -Force .agentops\baseline | Out-Null
Copy-Item .agentops\results\latest\results.json .agentops\baseline\results.json
```

Expected result: `.agentops\baseline\results.json` exists.

Why this matters: a baseline is the known-good measurement for `travel-agent:1`. In Lab 3, you will compare a changed agent against this baseline so a regression can be caught before merge.

### 6. Understand automatic evaluator selection and overrides

For this beginner lab, keep evaluator selection automatic. AgentOps uses the target shape and dataset shape to choose common evaluators.

Your current setup has:

- `agent: "travel-agent:1"` - a Foundry prompt agent target.
- Dataset rows with `input` and `expected` - conversational Q&A quality checks.
- No `context` field yet - no fixed RAG context is being supplied by the dataset.
- No `tool_calls` or `tool_definitions` yet - tool-use judging is not part of this smoke test.

Only override evaluators when you need a specific scoring set. For example, the built-in evaluator reference shows an override shape like this:

```yaml
evaluators:
  - GroundednessEvaluator
  - RetrievalEvaluator
  - RelevanceEvaluator
```

Expected result: You understand that the beginner path lets AgentOps choose evaluators, while advanced paths can add `evaluators:` in `agentops.yaml`.

## Checkpoint

Run these checks before you leave the lab:

```powershell
Test-Path .agentops\results\latest\report.md
Test-Path .agentops\results\latest\results.json
Test-Path .agentops\baseline\results.json
```

Expected result: Each command returns `True`.

You should also be able to open the report:

```powershell
notepad .agentops\results\latest\report.md
```

Expected result: The report shows metric scores and the gate result for the latest evaluation run.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Auth, endpoint, or project errors | The Foundry environment variables are not set in this PowerShell session, or the endpoint value is wrong. | Re-run the three `$env:` commands from the prerequisites and confirm the project endpoint matches your Foundry project. |
| JSONL read error or zero rows | The dataset file is empty, has blank pasted content, or has malformed JSON. | Recreate `.agentops\data\travel-smoke.jsonl`. Each row must be one complete JSON object on one line. |
| `agentops eval run` returns exit code `2` | The run completed, but at least one threshold failed. | Open `.agentops\results\latest\report.md`, read the failing metric, then adjust the agent or threshold intentionally. |
| Judge or model deployment error | The judge model deployment named by `AZURE_OPENAI_DEPLOYMENT` is missing or not available to the Foundry project. | Confirm that a chat-capable deployment such as `gpt-4o-mini` exists in the Foundry project and that the environment variable uses the deployment name. |

## What you just learned

- A dataset is a release contract because it names the behaviors the agent must keep.
- Thresholds turn quality and performance into an explicit gate.
- Exit codes make the gate usable locally and later in CI.
- A baseline enables regression detection when the agent changes.
- This lab is the **Evaluate** pillar in the AgentOps model: Evaluate -> Ship -> Observe -> Operate.

## Carry into the next lab

You now have a green baseline at `.agentops\baseline\results.json`. Lab 3 deliberately regresses the agent (`travel-agent:2`) and uses this baseline to catch it before merge.
