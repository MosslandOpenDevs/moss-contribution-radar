# moss-contribution-radar

AI-powered contribution radar for discovering, scoring, and operationalizing open-source PR opportunities for Mossland builders.

## Why this exists

Open-source contributors waste time hunting for issues that are:

- actually actionable,
- aligned with their stack,
- active enough to get reviewed,
- and valuable enough to strengthen their portfolio.

`moss-contribution-radar` turns that messy search process into a repeatable pipeline:

1. ingest candidate repositories, issues, and PR-friendly signals,
2. score contribution opportunities,
3. generate contributor-facing briefs,
4. track outreach and execution status.

## Problem statement

Most contributors discover opportunities through ad-hoc browsing on GitHub, social feeds, and Discord communities. That approach creates three problems:

- **Low signal density** — too many stale or beginner-trap issues.
- **Poor personal fit** — issues rarely match the contributor's skills or goals.
- **Weak execution flow** — even when a good issue is found, there is no clean handoff into action.

## Vision

Build a lightweight contribution intelligence platform that helps Mossland builders consistently find and close meaningful OSS contributions.

The platform should answer:

- Which repos are most worth watching this week?
- Which issues are realistically mergeable in the next 7–14 days?
- Which opportunities best match a contributor's skills?
- What is the fastest path from discovery to submitted PR?

## MVP

The MVP focuses on a narrow but useful loop:

- Pull repositories and issues from GitHub
- Normalize repository health/activity signals
- Score issues for contribution potential
- Surface a ranked shortlist
- Generate a contribution brief for each shortlisted issue

### Core MVP features

- **Repository watchlist ingestion**
  - manually curated seed repositories
  - topic-based GitHub search support
- **Opportunity scoring**
  - issue freshness
  - maintainer activity
  - label quality (`good first issue`, `help wanted`, etc.)
  - repository responsiveness
  - language/tag match
- **Contributor matching**
  - lightweight user skill profile
  - preferred languages/domains
  - difficulty and urgency filters
- **Contribution brief generation**
  - repo context summary
  - issue summary
  - probable implementation area
  - first-step checklist
- **Workflow status tracking**
  - discovered
  - shortlisted
  - claimed
  - in progress
  - PR opened
  - merged / closed

## Proposed architecture

```text
GitHub APIs / curated repo list
            ↓
      Ingestion pipeline
            ↓
   Normalized opportunity store
            ↓
      Scoring + ranking engine
            ↓
  Brief generator / action dashboard
```

### Suggested stack

- **Backend:** Python + FastAPI
- **Data jobs:** Python cron / scheduled tasks
- **Storage:** SQLite for MVP, Postgres later
- **Frontend:** Next.js or simple React dashboard
- **Integrations:** GitHub REST/GraphQL APIs
- **AI layer:** LLM-generated contribution briefs and summaries

## Data model overview

### `repositories`
- `id`
- `full_name`
- `description`
- `language`
- `stars`
- `forks`
- `open_issues_count`
- `last_push_at`
- `health_score`

### `opportunities`
- `id`
- `repo_id`
- `issue_number`
- `title`
- `labels`
- `created_at`
- `updated_at`
- `score`
- `difficulty`
- `status`
- `brief_markdown`

### `contributors`
- `id`
- `name`
- `skills`
- `preferred_languages`
- `interests`
- `difficulty_band`

## Scoring dimensions

A first-pass score can combine:

- repository activity recency
- issue freshness
- comment velocity
- maintainers replying in the last N days
- issue label quality
- issue size / ambiguity heuristics
- contributor-skill overlap

Example formula:

```text
opportunity_score =
  0.25 * repo_health +
  0.20 * maintainer_responsiveness +
  0.20 * issue_actionability +
  0.20 * contributor_fit +
  0.15 * merge_likelihood
```

## Example use cases

### 1. New contributor onboarding
A beginner wants 3 Python issues that are active, well-scoped, and likely to be reviewed quickly.

### 2. Portfolio-driven contributor
An experienced builder wants higher-signal repos in AI infra, agents, or data tooling.

### 3. Community ops
A community lead wants to publish a weekly "best issues to tackle" digest for Mossland Open Devs.

## Milestones

### Phase 1 — Research and ingestion
- define target personas
- create seed repo watchlist
- implement GitHub ingestion
- persist normalized repo/issue data

### Phase 2 — Scoring and ranking
- build heuristics engine
- rank opportunities
- validate results on a small curated set

### Phase 3 — Brief generation and workflow
- generate issue briefs
- add claim / status workflow
- export weekly shortlist

### Phase 4 — Productization
- simple dashboard
- contributor profiles
- recurring automated updates

## Repo structure target

```text
moss-contribution-radar/
├── README.md
├── docs/
│   ├── architecture.md
│   └── plans/
├── app/
│   ├── api/
│   ├── scoring/
│   ├── ingestion/
│   └── models/
├── scripts/
├── tests/
└── data/
```

## Immediate next steps

1. Finalize MVP scope and target persona
2. Write architecture and implementation plan docs
3. Scaffold backend project structure
4. Implement GitHub ingestion for a curated repo list
5. Build first heuristic scoring pass
6. Expose ranked opportunities through a simple API

## Repository goals

This repository should become:

- a practical contributor discovery engine,
- a reusable dataset pipeline for OSS opportunity analysis,
- and a community-facing tool for Mossland Open Devs.

## License

TBD
