---
title: "Template: Readiness evidence package"
layout: default
nav_exclude: true
---

# Readiness evidence package

Produced in [Lab 3]({{ '/long/labs/lab-03-release-gates/' | relative_url }}). The single
reviewable record a human uses to approve (or block) a release. It is the artefact behind
the gated approval between qa and prod.

```markdown
# Readiness evidence package

agent_id:
agent_version:
release_id:
owner:
prepared: <date>

## 1. Target and version
- Agent: <name:version>
- Foundry project / deployment:
- Commit:

## 2. Evaluation evidence
- eval_run_id:
- Dataset: <name>, <row count> cases
- Result summary (link to report.md):
- Comparison vs baseline (deltas):

## 3. Gate result
- PR gate: pass / fail
- Deploy-to-qa gate: pass / fail
- Workflow run link:

## 4. Observability
- Trace ID convention:
- App Insights / Log Analytics link:
- Dashboards wired: yes / no

## 5. Safety and red team
- Content safety: 0 violations / N violations
- Red-team scan: link, open high findings

## 6. Known risks
| Risk | Severity | Mitigation | Owner |
|---|---|---|---|

## 7. Owner and escalation
- Accountable owner:
- On-call / escalation path:

## 8. Next eval improvements
- New cases queued from production traces:

## Decision
- go / no-go:
- Approver:
- Date:
```

The accelerator can project most of this automatically:
`agentops doctor --evidence-pack` writes `evidence.json` and `evidence.md` into
`.agentops/release/latest/`. Attach those to the release and link them from sections 2-4.
