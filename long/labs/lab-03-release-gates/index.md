---
title: "Lab 3: Release Gates and Evidence"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 3
---

# Lab 3: Release Gates and Evidence

## Where you are in the journey

In Lab 2, you evaluated `travel-agent:1` and saved a green baseline at `.agentops/baseline/results.json`. In this lab, you act like a real team shipping a prompt change: you deliberately make the agent worse, compare the new version against the baseline, and prove the gate catches the regression before merge.

This lab is the **Ship** pillar in action: a team should not rely on a good feeling or a demo. A team should require a repeatable gate and durable release evidence.

## Duration and what you will build

**Duration:** 75 minutes.

**You will build:** a second Foundry Prompt Agent version, `travel-agent:2`, with a deliberately worse prompt; a baseline-compared evaluation run that fails the release gate with exit code `2`; and a review-ready release evidence pack from Doctor at `.agentops/release/latest/`.

## Prerequisites

Before you start, make sure all of these are true:

- You completed Labs 1 and 2.
- Your working folder is still `agentops-vbd/`.
- `agentops.yaml` exists at the folder root.
- `.agentops/` exists.
- The Lab 2 baseline exists at `.agentops/baseline/results.json`.
- Your dataset still exists at `.agentops/data/travel-smoke.jsonl`.
- Your latest passing Lab 2 run produced `.agentops/results/latest/results.json` and `.agentops/results/latest/report.md`.
- You are signed in with Azure CLI.
- These environment variables are still set in your PowerShell session:

```powershell
$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
$env:AZURE_OPENAI_ENDPOINT = "https://<openai-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
```

Quick check:

```powershell
cd agentops-vbd
Test-Path .agentops\baseline\results.json
Select-String -Path agentops.yaml -Pattern '^agent:'
```

**Expected result:** `Test-Path` prints `True`, and `agentops.yaml` still points at the passing Lab 2 version, usually `agent: "travel-agent:1"`.

## Concepts in two minutes

- **Absolute thresholds** ask, "Did this run meet the minimum bar?" Example: coherence must be above a threshold.
- **Regression gates** ask, "Did this version get worse than the approved baseline?" That is what `agentops eval run --baseline` adds.
- **Baseline comparison** uses `.agentops/baseline/results.json` from Lab 2 as the known-good reference and compares the candidate run against it.
- **Exit codes are the merge signal:** `0` means pass, `2` means a threshold or gate failed, and `1` means the command itself errored.
- **Doctor** runs readiness checks across local workspace evidence, evaluation history, Foundry control-plane signals when configured, Azure Monitor when configured, and Azure resource posture when available.
- **Evidence pack** means the durable proof a reviewer can attach to a release or PR: `.agentops/release/latest/evidence.json` for machines and `.agentops/release/latest/evidence.md` for humans.

## Step by step

### 1. Regress the Travel Agent prompt in Foundry

Open the Foundry portal and publish a deliberately worse version of the same agent.

Portal clicks:

1. Open <https://ai.azure.com>.
2. Select the same Foundry project you used in Labs 1 and 2.
3. Go to **Agents**.
4. Open **travel-agent**.
5. Open the prompt or instructions editor.
6. Replace the helpful Lab 1 prompt with this deliberately bad prompt:

```text
You are Travel Agent. Be very brief. Give a short answer. Do not ask follow-up questions.
```

7. Save the change.
8. Click **Publish**.
9. Note the new published version. For this lab, treat it as `travel-agent:2`.

**Expected result:** Foundry shows a new published agent version, `travel-agent:2`. The prompt is clearly weaker because it removes the guidance to be accurate, include practical travel details, and ask for missing destination, duration, or preference details.

Now update `agentops.yaml` so AgentOps evaluates the regressed candidate.

```powershell
(Get-Content agentops.yaml) `
  -replace '^agent:.*$', 'agent: "travel-agent:2"' |
  Set-Content -Encoding utf8 agentops.yaml

Select-String -Path agentops.yaml -Pattern '^agent:'
```

**Expected result:** PowerShell prints:

```text
agent: "travel-agent:2"
```

### 2. Re-run evaluation against the Lab 2 baseline

Run the same evaluation, but compare this candidate version against the saved baseline from Lab 2.

```powershell
agentops eval run --baseline .agentops/baseline/results.json
$LASTEXITCODE
```

**Expected result:** AgentOps scores the current candidate from `agentops.yaml`, which is now `travel-agent:2`, then compares it against the `travel-agent:1` baseline in `.agentops/baseline/results.json`.

Because the prompt is intentionally worse, the gate should fail and `$LASTEXITCODE` should print:

```text
2
```

The terminal summary should indicate that the run did not pass. Do not worry if your exact metric names differ from your Lab 2 configuration. The important signal is that the candidate run was compared to the baseline and the process exited with code `2`.

Open the human report:

```powershell
Get-Content .agentops\results\latest\report.md
```

**Expected result:** The report contains the latest evaluation summary and a baseline comparison section. Look for the metric or metrics that regressed. For a beginner, read it in this order:

1. Find the overall pass or fail status.
2. Find the comparison against baseline.
3. Find the metric with the negative delta or failed threshold.
4. Connect that metric back to the worse prompt you published.

### 3. Map the failed command to a PR gate

You do not build the full CI pipeline in this lab. You only learn the contract the pipeline will use.

The same command can run in CI:

```powershell
agentops eval run --baseline .agentops/baseline/results.json
```

**Expected result:** The command is now easy to reason about as a PR gate:

- Exit code `0` means the candidate can continue through the pipeline.
- Exit code `2` means the quality or regression gate failed, so the PR should not merge.
- Exit code `1` means the evaluation command errored, so the pipeline should also stop.

The capstone will generate the full workflow. For now, remember the document name: **CI/CD with GitHub Actions**.

### 4. Generate the human report again

Regenerate the Markdown report from the latest results.

```powershell
agentops report generate
Get-Content .agentops\results\latest\report.md
```

**Expected result:** `.agentops/results/latest/report.md` exists and is readable. This is the PR-friendly report a reviewer can skim without opening `results.json`.

Use this quick reading pattern:

- Start with the verdict.
- Check the metric table.
- Check the baseline comparison.
- Decide whether the candidate is safe to ship.

For `travel-agent:2`, the answer should be **do not ship**.

### 5. Run Doctor and create release evidence

First run Doctor as a readiness check.

```powershell
agentops doctor
$LASTEXITCODE
```

**Expected result:** Doctor writes a readiness report under `.agentops/agent/`, usually `.agentops/agent/report.md`. Doctor exit codes follow the same pattern: `0` means no finding crossed the configured fail floor, `2` means at least one finding crossed that floor, and `1` means Doctor itself errored.

Doctor checks can include these families, depending on what is configured and reachable in your workspace:

- Quality regression findings such as `regression.<metric>` from evaluation history.
- Performance checks such as latency.
- Reliability checks such as production error rate or missing runtime telemetry.
- Security posture checks such as managed identity, public network access, local auth, and diagnostic settings.
- Responsible AI checks such as content-filter signals, continuous evaluation configuration, and LLM-judged prompt or dataset findings.
- Operational excellence checks such as thresholds, PR gate workflow presence, deploy workflow presence, stale evaluations, baseline presence, and release evidence readiness.

Now create the release evidence pack.

```powershell
agentops doctor --evidence-pack
Get-ChildItem .agentops\release\latest
Get-Content .agentops\release\latest\evidence.md
```

**Expected result:** The release folder contains both files:

```text
evidence.json
evidence.md
```

`evidence.md` is what a release reviewer reads. It summarizes the evaluation result, baseline readiness, Doctor findings, workflow readiness, Foundry and monitoring readiness when available, and the final release posture. If the latest evaluation is still the regressed `travel-agent:2` run, the evidence should make the do-not-ship decision visible.

### 6. Fix the prompt and end on a passing version

The gate did its job. Now fix the candidate before the lab ends.

You have two acceptable options. Use **Option A** if you want another Foundry version. Use **Option B** if your instructor wants everyone to return to the Lab 2 baseline version.

#### Option A - Publish a fixed `travel-agent:3`

Portal clicks:

1. Open <https://ai.azure.com>.
2. Select your Foundry project.
3. Go to **Agents**.
4. Open **travel-agent**.
5. Edit the prompt or instructions.
6. Restore the careful Travel Agent behavior. Use the Lab 1 prompt, or use this beginner-safe version:

```text
You are Travel Agent, a concise travel planning assistant.

Help users plan short leisure trips. Always include:
- a short summary;
- a day-by-day plan when the user asks for an itinerary;
- practical notes about budget, transit, weather, or booking constraints;
- a reminder that you cannot make live reservations or purchases.

Ask one clarifying question only when the destination, duration, or traveler preference is missing. Do not invent booking confirmations, prices, or availability.
```

7. Save the change.
8. Click **Publish**.
9. Note the new version, usually `travel-agent:3`.

Update `agentops.yaml`:

```powershell
(Get-Content agentops.yaml) `
  -replace '^agent:.*$', 'agent: "travel-agent:3"' |
  Set-Content -Encoding utf8 agentops.yaml
```

Re-run the gate:

```powershell
agentops eval run --baseline .agentops/baseline/results.json
$LASTEXITCODE
```

**Expected result:** `$LASTEXITCODE` prints `0`. The fixed version is no longer worse than the baseline according to your configured gate.

#### Option B - Revert `agentops.yaml` to `travel-agent:1`

If you do not want to publish another Foundry version, point the lab back to the passing baseline version.

```powershell
(Get-Content agentops.yaml) `
  -replace '^agent:.*$', 'agent: "travel-agent:1"' |
  Set-Content -Encoding utf8 agentops.yaml

agentops eval run --baseline .agentops/baseline/results.json
$LASTEXITCODE
```

**Expected result:** `$LASTEXITCODE` prints `0` because you are back on the known-good version.

Record the passing version you ended on:

```powershell
Select-String -Path agentops.yaml -Pattern '^agent:'
```

**Expected result:** `agentops.yaml` ends on a passing agent version, either `travel-agent:3` from Option A or `travel-agent:1` from Option B. Write that version down because Lab 4 uses the currently passing agent.

## Checkpoint

Run this verification block before you leave the lab:

```powershell
Test-Path .agentops\baseline\results.json
Test-Path .agentops\release\latest\evidence.md
Select-String -Path agentops.yaml -Pattern '^agent:'
agentops eval run --baseline .agentops/baseline/results.json
$LASTEXITCODE
```

**Expected result:**

- The baseline file check prints `True`.
- The evidence file check prints `True`.
- `agentops.yaml` points at a passing agent version.
- The final evaluation exits with code `0`.

You should also have seen one earlier failed run where `$LASTEXITCODE` was `2` for the deliberately regressed `travel-agent:2` candidate.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| The regressed run passed and there is no baseline comparison. | You forgot `--baseline .agentops/baseline/results.json`. | Re-run `agentops eval run --baseline .agentops/baseline/results.json`. Then open `.agentops/results/latest/report.md` again. |
| Foundry still shows the same version after you edited the prompt. | You saved a draft but did not publish it. | Return to Foundry, open `travel-agent`, click **Publish**, and note the new published version. |
| `agentops eval run --baseline` exits `1`. | This is a command or environment error, not a quality gate failure. Common causes are missing Azure sign-in, missing env vars, wrong Foundry endpoint, or a bad `agent:` value. | Run `az login`, verify the three environment variables, and check `agentops.yaml`. Then re-run the command. |
| `$LASTEXITCODE` is `2` and you think PowerShell failed. | Exit code `2` is the expected gate-failed signal. | Treat it as a successful detection of a bad candidate. Open `report.md` to see what regressed. |
| `.agentops/release/latest/evidence.md` is missing. | You ran `agentops doctor` without `--evidence-pack`, or Doctor errored before writing evidence. | Run `agentops doctor --evidence-pack`. If it exits `1`, fix the reported configuration or auth error and run it again. |
| Doctor reports missing PR or deploy workflow. | That is expected at this point in the workshop. | Keep going. The capstone covers generated CI/CD workflow setup. |

## What you just learned

- A release gate can compare a candidate agent against a known-good baseline, not just against absolute thresholds.
- Exit codes are the contract between local testing, CI, and merge policy: `0` pass, `2` gate fail, `1` error.
- Doctor turns evaluation history and readiness checks into reviewable release evidence.
- The Ship pillar is about proving the candidate is safe to merge before it reaches production.

## Carry into the next lab

Your agent now ships with evidence. But shipping is not the end - Lab 4 turns on Observability so you can see what the agent does in production and feed real traces back into evaluation.
