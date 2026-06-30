---
title: "Lab 1: Foundations and Control Plane"
layout: default
parent: Labs
grand_parent: AgentOps VBD Workshop
nav_order: 1
---


# Lab 1: Foundations and Control Plane

## Where you are in the journey

This is the first hands-on lab in the AgentOps VBD workshop. You will create one Foundry Prompt Agent, the **Contoso Travel Agent**, and carry the same agent through all 6 labs plus the capstone.

The full workshop arc is **Evaluate -> Ship -> Observe -> Operate**:

| Later lab | What it adds to the same agent |
|---|---|
| Lab 2 - Evaluation | Design a smoke dataset and run the first quality gate. |
| Lab 3 - Release gates | Compare a changed agent version against a baseline and create release evidence. |
| Lab 4 - Observability | Connect runtime telemetry and trace behavior through Azure Monitor and Application Insights. |
| Lab 5 - Safety and governance | Add responsible AI, red-team, and governance evidence into the release view. |
| Lab 6 - Continuous improvement | Promote real traces back into regression tests. |
| Capstone | Generate CI/CD, review evidence, and make a ship or no-ship decision. |

## Duration

60 minutes

## You will build

You will install the AgentOps accelerator, sign in to Azure, create the Contoso Travel Agent as a Foundry Prompt Agent named `travel-agent:1`, and initialize an AgentOps workspace with `agentops.yaml` and `.agentops/`.

## Prerequisites

Because this is the first lab, confirm the global workshop prerequisites before you begin:

- An Azure subscription you can use for workshop resources.
- Access to a Microsoft Foundry project in <https://ai.azure.com>.
- At least one model deployment in that Foundry project named `gpt-4o-mini`.
- Owner or Contributor access on the Foundry project.
- Python 3.10 or later.
- Azure CLI `az` installed.
- Git installed.
- VS Code installed, optional but recommended.
- PowerShell. All commands below are written for PowerShell.

## Concepts in two minutes

- **AgentOps** is the operating model for production agents: evaluate quality, ship with evidence, observe runtime behavior, and operate safely after launch.
- **Microsoft Foundry** is the control plane. You create, version, run, trace, monitor, evaluate, and investigate agents there.
- **The AgentOps accelerator** is the repo-side reference accelerator that makes the operating model tangible. It creates `agentops.yaml`, runs local and CI gates, writes results, and produces release evidence.
- **A Foundry Prompt Agent identity is `name:version`**. In this lab, the identity is `travel-agent:1`.
- **The repo-side release contract lives beside your code**. The key file is `agentops.yaml`; the managed workspace is `.agentops/`.

## Step by step

### 1. Create the working folder and open it

Open PowerShell in the location where you keep workshop files. Then run:

```powershell
New-Item -ItemType Directory -Force agentops-vbd | Out-Null
Set-Location agentops-vbd
Get-Location
```

Expected result: PowerShell prints a path ending in `agentops-vbd`. This folder is the workspace you will reuse in every lab.

### 2. Install the accelerator and verify the CLI

Install the published package from PyPI:

```powershell
python -m pip install agentops-accelerator
agentops --version
```

Expected result: The install command completes successfully, and `agentops --version` prints an installed AgentOps version.

### 3. Create the Contoso Travel Agent in the Foundry portal

Use the Foundry portal for this step. Keep PowerShell open because you will return to it in the next step.

1. Open <https://ai.azure.com> in a browser.
2. Sign in with the same account you use for your Azure subscription.
3. Create or open the Foundry project you will use for the workshop.
   - If you already have a project with a `gpt-4o-mini` model deployment, open it.
   - If you need a new project, create one using your workshop subscription and confirm that the project has a model deployment named `gpt-4o-mini`.
4. In the project, go to **Agents / Build**.
5. Select **New agent**.
6. Enter these values:

   | Field | Value |
   |---|---|
   | Name | `travel-agent` |
   | Model deployment | `gpt-4o-mini` |
   | Instructions | See the prompt below. |

7. Paste this short travel-assistant system prompt into the instructions field:

   ```text
   You are the Contoso Travel Agent, a concise travel planning assistant.

   Help users plan short leisure trips. Include practical notes about budget,
   transit, weather, and booking constraints when useful. Ask one clarifying
   question when the destination, duration, or traveler preference is missing.
   Do not claim that you can make live reservations, purchases, or booking
   confirmations.
   ```

8. Select **Save**.
9. Select **Publish** if the portal requires publishing to create a versioned agent.
10. Note the version shown by Foundry. For this workshop, record the agent identity as `travel-agent:1`. If your portal shows a different first published version, keep using `travel-agent:1` for this lab so the workshop spine stays consistent.
11. Find and copy the project endpoint:
    - Go to the project overview or project settings area.
    - Look for the project endpoint value.
    - It should look like `https://<resource>.services.ai.azure.com/api/projects/<project>`.
    - Save it somewhere temporary so you can paste it into PowerShell in the next step.

Expected result: Foundry contains a Prompt Agent named `travel-agent`, you know the workshop identity `travel-agent:1`, and you have copied the Foundry project endpoint.

### 4. Sign in to Azure and set the required environment variables

Return to PowerShell. Sign in to Azure first:

```powershell
az login
```

Expected result: A browser sign-in opens, you complete authentication, and the Azure CLI returns your signed-in subscription context.

Set the three required environment variables. Replace only the placeholder parts inside angle brackets for the first two values. Keep the deployment name as `gpt-4o-mini`.

```powershell
$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
$env:AZURE_OPENAI_ENDPOINT = "https://<openai-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
```

Expected result: PowerShell accepts the three assignments without output.

Verify that the variables are present in the current shell:

```powershell
$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT
$env:AZURE_OPENAI_ENDPOINT
$env:AZURE_OPENAI_DEPLOYMENT
```

Expected result: PowerShell prints your Foundry project endpoint, your Azure OpenAI endpoint, and `gpt-4o-mini`.

### 5. Initialize the AgentOps workspace

Run the guided setup:

```powershell
agentops init
```

When the wizard asks for values, use the workshop values from this lab:

| Prompt | Enter |
|---|---|
| Foundry project endpoint | The value you copied from Foundry. |
| Agent | `travel-agent:1` |
| Dataset path | Accept the starter value if offered. Lab 2 replaces it with `.agentops/data/travel-smoke.jsonl`. |

Expected result: The command completes and creates `agentops.yaml` plus a `.agentops/` workspace.

Now make the agent identity explicit in `agentops.yaml`:

```powershell
(Get-Content agentops.yaml) `
  -replace '^agent:.*$', 'agent: "travel-agent:1"' |
  Set-Content -Encoding utf8 agentops.yaml

Select-String -Path agentops.yaml -Pattern '^agent:'
```

Expected result: The final command prints `agent: "travel-agent:1"`.

The AgentOps concepts define the workspace shape like this:

```text
agentops.yaml          # flat config: agent, dataset, thresholds
.agentops/
|-- data/              # dataset rows (JSONL)
|-- results/           # run outputs + latest/ pointer
|-- agent/             # Doctor history and reports
`-- release/           # evidence.json/evidence.md when generated
```

You can inspect what exists now:

```powershell
Get-ChildItem -Force
Get-ChildItem -Force .agentops
```

Expected result: The root folder includes `agentops.yaml` and `.agentops`. The `.agentops` folder may already contain some of the managed subfolders, and later labs will populate `data`, `results`, `agent`, and `release`.

### 6. Sanity check the control plane and repo-side contract

Read the split this way:

> Foundry operates the agent; AgentOps turns that operating signal into repo-side release proof.

In this lab:

- Foundry is the control plane. It owns the Prompt Agent, the model deployment, the version, and the project endpoint.
- AgentOps is the repo-side release contract. It records which agent you are evaluating and where the workspace artifacts will land.

Run this quick check:

```powershell
agentops --version
Test-Path agentops.yaml
Test-Path .agentops
Select-String -Path agentops.yaml -Pattern '^agent: "travel-agent:1"'
```

Expected result: The version command prints a version, both `Test-Path` commands print `True`, and the final command finds `agent: "travel-agent:1"`.

## Checkpoint

Before you leave Lab 1, verify the three required artifacts:

```powershell
agentops --version
Test-Path agentops.yaml
Test-Path .agentops
Select-String -Path agentops.yaml -Pattern '^agent: "travel-agent:1"'
```

You are ready for Lab 2 when all of these are true:

- `agentops --version` prints a version.
- `agentops.yaml` exists.
- `agentops.yaml` contains `agent: "travel-agent:1"`.
- `.agentops/` exists.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `agentops` is not recognized or not found. | The Python scripts folder is not on `PATH`, or the shell was open before install. | Close and reopen PowerShell, then run `python -m pip install agentops-accelerator` again. If needed, use the same Python installation for install and commands. |
| `az login` signs in to the wrong tenant or subscription. | Your account belongs to multiple tenants or subscriptions. | Run `az account list -o table`, then set the intended subscription with `az account set --subscription "<subscription-id-or-name>"`. |
| AgentOps cannot connect to Foundry or cannot find the project. | `AZURE_AI_FOUNDRY_PROJECT_ENDPOINT` is missing, copied from the wrong project, or missing `/api/projects/<project>`. | Copy the project endpoint again from the Foundry project overview or settings page, then reset `$env:AZURE_AI_FOUNDRY_PROJECT_ENDPOINT`. |
| Evaluation setup later complains about the model deployment. | The deployment name does not match `gpt-4o-mini`, or the deployment does not exist in the Foundry project. | In Foundry, confirm the model deployment name is exactly `gpt-4o-mini`, or update the deployment so the workshop name exists. |

## What you just learned

- Foundry is the agent control plane: create, version, run, trace, monitor, evaluate, and investigate.
- AgentOps keeps the release contract close to the repo through `agentops.yaml` and `.agentops/`.
- A Foundry Prompt Agent can be referenced by version identity, such as `travel-agent:1`.
- This lab establishes the **Ship** pillar foundation: a named candidate agent and a repeatable workspace that later labs can gate and prove.

## Carry into the next lab

You now have `travel-agent:1` and an initialized `agentops.yaml`. Lab 2 uses them to design and run your first evaluation.
