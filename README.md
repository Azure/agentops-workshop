# AgentOps Workshop

This repository contains the working materials and GitHub Pages site for the **AgentOps Workshop**.

The workshop is organized around the AgentOps operating model: **Evaluate, Gate, Observe, Diagnose, Ship, Improve**. AgentOps Toolkit appears only as a practical implementation component for selected demo and lab flows, not as the main topic.

## Delivery tracks

| Track | Purpose | Status |
|---|---|---|
| [1-hour](1-hour/index.md) | Short session with agenda, slide plan, run of show, observability focus, and demo video plan. | Planned |
| [8-hour](8-hour/index.md) | Full-day workshop with multiple lab plans and a deeper observability lab. | Planning skeleton |

## Files

| File | Purpose |
|---|---|
| `.github\copilot-instructions.md` | Repository-specific guidance for GitHub Copilot and content generation. |
| `_config.yml` | Jekyll and Just the Docs configuration for GitHub Pages. |
| `index.md` | GitHub Pages home page. |
| `1-hour\` | Short session deliverables: agenda, slides, narrated video, speaker script, run of show. |
| `8-hour\` | Full-day workshop planning and lab placeholders. |
| `assets\` | Shared images, slide exports, videos, and sample data. |
| `prep\` | Authoring and preparation material: references, build tools, planning notes, intermediate artefacts. Excluded from the published site. See [`prep\README.md`](prep/README.md). |

## Main storyline

1. Agents are moving from prototype to production.
2. Production needs evidence: evals, gates, observability, safety, and ownership.
3. AgentOps provides the operating model.
4. Foundry remains the control plane.
5. AgentOps practices create the repo and CI/CD release-readiness loop.
6. Observability connects runtime behavior, traces, incidents, and production learnings back to evaluation.
7. The demo shows a regression caught before release, fixed, observed, and promoted with evidence.

## GitHub Pages

This repository is prepared for GitHub Pages using Jekyll and the Just the Docs theme.

After publishing the repository, the site should be available at:

`https://azure.github.io/agentops-workshop/`

If the repository name changes, update `baseurl` in `_config.yml`.

## Local preview

If Ruby and Bundler are installed:

```powershell
bundle install
bundle exec jekyll serve
```

Then open the local URL shown by Jekyll.

## Publishing checklist

Before making the repository public:

- Confirm `baseurl` matches the final repository name.
- Replace placeholder code of conduct and licensing materials with approved organization files.
- Review screenshots, traces, links, and sample data for sensitive information.
