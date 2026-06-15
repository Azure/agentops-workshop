# AgentOps Overview — Spoken Narration

## Part 1 — Evaluate (3:30)

### Intro (card)

> Evaluate really comes down to one question: is this agent good enough to ship? Before any deploy, AgentOps turns that judgment into a measurable, repeatable gate. So let me walk you through how I build it, starting with the data.

### Build the eval dataset

> First, I'm creating a small, honest dataset. I open the file in the editor and write three travel prompts — Lisbon, Seattle, Tokyo. Then I pair each one with the answer I expect. Those expected answers are my contract with the gate.

### agentops doctor / eval init / eval run

> With that dataset in place, I wire up the gate. It starts with a quick preflight that confirms my config is valid, and that the Foundry evaluators are ready: coherence, fluency, text similarity, response completeness. Then I run agentops eval init, and it generates my evaluation recipe and wires it into agentops dot yaml. I open that file. It declares the agent, the dataset, the prompt, the model — gpt 4o mini — and it points to the eval recipe. One file ties the whole gate together. Then I run agentops eval run. It delegates to Azure AI Foundry, writes the results and a report, and comes back with the verdict: threshold status, passed. Same dataset, same evaluators — so the gate is consistent and auditable, run after run.

### Weighted rubrics + ASSERT safety checks

> But that smoke gate is just my floor. Real traffic is messier than a few single-shot prompts, so I evolve the dataset into conversation-aware rows — a three-day Lisbon food trip, a low-budget Seattle weekend, a family Tokyo plan with two kids. Then I harden the rubric. Instead of one blunt score, I describe what a great answer looks like, and Foundry's custom rubric evaluator turns that into weighted, named criteria — correct itinerary, adherence to constraints like kids and budget, clear and honest notes. And here's the part I love: every run comes back as a per-dimension scorecard. Smoke-core lands at zero-point-nine-two, and I can see exactly why — the itinerary passes, the practical notes a notch lower, each with a written reason from the judge. It's explainable, not just a single number. And the rubric lives in my repo, so when a teammate disagrees, they argue with a pull request, not a Microsoft Teams message.

### Red Team adversarial run + evidence pack

> Quality is only part of shipping safely — so I add two more gates, and I scaffold both with GitHub Copilot. First, I ask the agentops-governance skill to wire up ASSERT against my agent. It installs the package, writes the config, and runs deterministic safety checks — prompt injection, PII leak, jailbreak — generating its own adversarial test cases and scoring each one. Then I do the same for Red Team. The same GitHub Copilot skill scaffolds the runner, and Azure AI Evaluation attacks my agent across real risk categories — violence, hate, self-harm — using strategies like base64 and rot13. My attack success rate comes back at twelve and a half percent, under my twenty percent gate. And finally, one Doctor command packages all of it — the evals, the safety checks, the Red Team run — into a single evidence pack I can hand to my security partner.

### End card

> And that's the heart of Evaluate: answering "can we ship it, and how do we know?" with evidence instead of opinion. A few honest examples became a full gate — a weighted quality rubric, ASSERT safety checks, and an adversarial Red Team run, every threshold versioned in my repo and packaged into one evidence pack I can hand to an approver. The next challenge is making that gate run automatically.

## Part 2 — Ship (2:01)

### Intro (card)

> Evaluating locally is only half the story. So now I make those gates run automatically: on every pull request, on every deploy. Let me show you how I wire that up, end to end.

### agentops workflow generate

> Now I turn those gates into CI. One command - agentops workflow generate - and I get two GitHub Actions workflows: a pull-request gate, and a dev deploy.

### Copilot CLI wires repo + Entra + OIDC

> But those workflows still need to reach Azure, and wiring that up used to be a weekend project: OIDC, federated credentials, secrets, environment variables. With the Copilot CLI in my workspace, it is one prompt. It reads the AgentOps skill, verifies my role assignments, creates my GitHub repo, creates the Entra app with a federated credential, and writes the OIDC variables straight into my dev environment. No long-lived secrets in the repo, no manual click-ops in the portal. My repo and Azure are now connected, and the pull-request gate is armed.

### First green PR → merge → dev deploy + foundry-agent.json

> Here is my first real pull request, a simple prompt change. The PR gate kicks off automatically. It stages the candidate, runs the same eval recipe I just showed you, and either green-lights the merge or blocks it. This one passes. So I merge to main, and the dev deploy workflow takes over. It re-evaluates the merged candidate in dev, records the deployment, and writes foundry-agent dot json, a tiny manifest with the prompt hash, the commit hash, and the workflow run URL. That is my provenance. From one line in that record, I can answer what is in dev right now, who shipped it, when, and which eval allowed it. No tribal knowledge, no spreadsheets, no guessing what shipped.

### End card

> And that is what Ship really means in AgentOps: the same gate I built locally now runs on every pull request and every deploy, with OIDC instead of secrets, and a tiny foundry-agent dot json manifest as my single source of truth for what is live. The next challenge is seeing how that agent actually behaves once real users arrive.

## Part 3 — Observe (2:02)

### Intro (card)

> Once my agent is live, the gate is not enough on its own: I need to see what it actually does in production. So now I turn on the telemetry layer, and let me walk you through every request and every score, in real time.

### Traces tab

> Now that my agent is live, every request becomes a trace. Each row in the Traces tab is one conversation, with duration, token counts, an estimated cost, and the evaluation scores attached. I can sort by cost, filter by agent version, or click into the full waterfall - the same observability surface I would expect for a service, applied to my agent.

### Operate cockpit

> The Operate cockpit is my live view. Prompt Shields alerts on the left, my agent inventory, the cost trend, the success rate, and Ask AI on the right for natural-language questions across everything I see. This is what I put on the on-call wall: one screen, all my agents, end to end.

### Promote traces into eval dataset

> And this is where evaluation becomes a loop, not a one-off. Any interesting trace - a failure, an edge case, a high-cost outlier - I can promote into my eval dataset with one click. Fifteen rows here, with lineage tracked back to the original traces. My next gate is tighter than today's, because it includes what production actually did.

### KQL on Log Analytics

> And it is all OpenTelemetry under the hood. Every eval score lands in Log Analytics as gen ai dot evaluation dot result, so I can write the KQL I already know - average coherence by conversation, per hour, over the last twenty-four hours. No vendor lock-in on my data; my existing dashboards keep working.

### End card

> And that is the heart of Observe: every conversation becomes a trace, every eval score becomes telemetry, and the interesting traces feed straight back into my eval dataset. Production is not a black box, it is the next iteration of my gate. The next challenge is what happens when something does break - and how I prove the release is still safe to ship.

## Part 4 — Own (3:14)

### Intro (card)

> Shipping is easy; owning is the hard part. So now I get into day-two operations: catching regressions before they reach my users, and proving release-readiness with evidence, not opinions. Let me show you both flavors of blocked.

### Regression caught at PR time

> Here is how it goes wrong. I open a pull request with a prompt edit - well-intentioned, looks fine in review. The PR gate runs the same eval recipe and reports a regression: coherence drops, similarity drops, the threshold fails. My release evidence flips to blocked. The Doctor - AgentOps' health check - shows the criticals on screen: regression coherence, regression similarity, latest evaluation failed. The bad prompt never reaches main, never reaches dev, never reaches my users. It was caught by an evaluator and a gate, not by a customer complaint, and the post-mortem writes itself, because every step is durable in git and in the Actions log.

### One-line revert + bad prompt joins the regression dataset

> My fix is a one-line revert. I restore the known-good prompt, push, and re-run the same gate on the same dataset. This time everything is green - coherence five point zero, similarity four point six six seven, every threshold passes. And here is the part that matters most: that bad prompt is now a permanent row in my regression dataset. The next time someone touches that area of the prompt, this exact failure has to pass again before the gate lets it through. The incident hardened my gate. That is the AgentOps loop - every regression I catch makes the next one harder to ship.

### Production-only blocked: latency p95, error rate

> That regression was caught at pull-request time. There is a second flavor of blocked I will hit once I am in production. I run the same gate against the live agent, and the rows themselves can pass - but Doctor, looking at production telemetry, still blocks the release. The criticals here are not quality, they are latency p ninety-five in production, and the error rate in production. Same command, same gate, completely different signal. The evidence pack, written to dot agentops slash release slash latest slash evidence dot md, captures both - so my release reviewer sees the full picture in one file, not five tabs.

### agentops cockpit (localhost dashboard)

> And for day-to-day visibility, I run agentops cockpit - it opens a local dashboard on localhost. Every finding has a Fix recommendation that links back to the exact AgentOps source - so I do not just see something is wrong, I get a concrete next step. Across the bottom: error rate at zero percent, p ninety-five around eleven seconds, five workflow runs, eighty percent success, latest PR passed. Same evidence as the markdown, but interactive - this is what stays open on my second monitor.

### End card

> And that is the AgentOps story end to end: I evaluate before I ship, I ship through gates that run on every pull request, I observe what real traffic actually does, and I own the agent the way I own any production service - with regressions caught at PR time and a release reviewer who sees evidence, not opinions. Every loop closes back into the next gate. The bar moves up, never down.
