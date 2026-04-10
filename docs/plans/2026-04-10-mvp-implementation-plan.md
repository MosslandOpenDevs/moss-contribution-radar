# Moss Contribution Radar MVP Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build an MVP that ingests GitHub repository and issue data, scores contribution opportunities, and exposes ranked contribution briefs through a small API.

**Architecture:** A Python backend ingests repo + issue metadata from GitHub into a local SQLite database, computes heuristic opportunity scores, and serves ranked results via FastAPI. The system is intentionally small, local-first, and easy to iterate on before moving to multi-user infra.

**Tech Stack:** Python, FastAPI, SQLite, SQLModel or SQLAlchemy, httpx, pytest, pydantic.

---

## Assumptions

- Initial scope is API-first; UI can come later.
- GitHub is the only external data source for MVP.
- A curated seed repository list is sufficient for the first iteration.
- LLM-generated briefs are optional in v1 and can begin as templated summaries.

## Deliverables

- API service with health and opportunities endpoints
- SQLite-backed normalized schema
- GitHub ingestion job for repositories/issues
- Heuristic scoring engine
- Contribution-brief generator
- Tests for ingestion, scoring, and API responses
- Documentation for local setup and usage

---

### Task 1: Initialize Python project scaffold

**Objective:** Create the base folder layout and dependency manifest.

**Files:**
- Create: `pyproject.toml`
- Create: `app/__init__.py`
- Create: `app/main.py`
- Create: `app/config.py`
- Create: `tests/__init__.py`
- Create: `.gitignore`

**Step 1: Write failing startup smoke test**

Create `tests/test_health.py` expecting the API app to load and return 200 from `/health`.

**Step 2: Run test to verify failure**

Run: `pytest tests/test_health.py -v`
Expected: FAIL because app modules do not exist yet.

**Step 3: Write minimal implementation**

Add FastAPI app bootstrap in `app/main.py` with a `/health` route returning `{"status": "ok"}`.

**Step 4: Run test to verify pass**

Run: `pytest tests/test_health.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add pyproject.toml app tests .gitignore
git commit -m "feat: scaffold api service"
```

### Task 2: Define database models

**Objective:** Create normalized persistence for repositories, issues, and opportunities.

**Files:**
- Create: `app/db.py`
- Create: `app/models.py`
- Modify: `tests/test_health.py`
- Create: `tests/test_models.py`

**Step 1: Write failing model test**

Add tests asserting repository and opportunity models can be instantiated and persisted into SQLite.

**Step 2: Run test to verify failure**

Run: `pytest tests/test_models.py -v`
Expected: FAIL because model classes do not exist.

**Step 3: Write minimal implementation**

Implement models such as:
- `Repository`
- `Issue`
- `Opportunity`
- optional `ContributorProfile`

Add DB session helpers in `app/db.py`.

**Step 4: Run test to verify pass**

Run: `pytest tests/test_models.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add app/db.py app/models.py tests/test_models.py
git commit -m "feat: add core persistence models"
```

### Task 3: Add repository seed configuration

**Objective:** Support a curated watchlist of repositories.

**Files:**
- Create: `data/seed_repos.yaml`
- Create: `app/repo_sources.py`
- Create: `tests/test_repo_sources.py`

**Step 1: Write failing test**

Assert the repo source loader can parse a YAML seed list and normalize full repo names.

**Step 2: Run test to verify failure**

Run: `pytest tests/test_repo_sources.py -v`
Expected: FAIL because the loader is missing.

**Step 3: Write minimal implementation**

Implement YAML loading, validation, and normalization.

**Step 4: Run test to verify pass**

Run: `pytest tests/test_repo_sources.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add data/seed_repos.yaml app/repo_sources.py tests/test_repo_sources.py
git commit -m "feat: add curated repo source loader"
```

### Task 4: Implement GitHub ingestion client

**Objective:** Fetch repository and issue metadata from GitHub.

**Files:**
- Create: `app/github_client.py`
- Create: `app/ingestion.py`
- Create: `tests/test_github_client.py`
- Create: `tests/test_ingestion.py`

**Step 1: Write failing tests**

Mock GitHub responses and verify:
- repository metadata parsing
- issue listing parsing
- pagination handling for at least one multi-page case

**Step 2: Run tests to verify failure**

Run: `pytest tests/test_github_client.py tests/test_ingestion.py -v`
Expected: FAIL because client and ingestion modules do not exist.

**Step 3: Write minimal implementation**

Use `httpx` with explicit timeout and GitHub token support via env var.

**Step 4: Run tests to verify pass**

Run: `pytest tests/test_github_client.py tests/test_ingestion.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add app/github_client.py app/ingestion.py tests/test_github_client.py tests/test_ingestion.py
git commit -m "feat: ingest github repo and issue metadata"
```

### Task 5: Build heuristic scoring engine

**Objective:** Convert normalized issue data into ranked contribution opportunities.

**Files:**
- Create: `app/scoring.py`
- Create: `tests/test_scoring.py`

**Step 1: Write failing tests**

Create scoring tests covering:
- label bonus for `good first issue`
- freshness decay
- maintainer responsiveness effect
- contributor language match bonus

**Step 2: Run tests to verify failure**

Run: `pytest tests/test_scoring.py -v`
Expected: FAIL because scoring module does not exist.

**Step 3: Write minimal implementation**

Implement:
- component sub-scores
- weighted final score
- normalized score range (e.g. 0–100)

**Step 4: Run tests to verify pass**

Run: `pytest tests/test_scoring.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add app/scoring.py tests/test_scoring.py
git commit -m "feat: rank contribution opportunities"
```

### Task 6: Generate contribution briefs

**Objective:** Produce human-readable execution briefs for shortlisted opportunities.

**Files:**
- Create: `app/briefs.py`
- Create: `tests/test_briefs.py`

**Step 1: Write failing tests**

Assert generated briefs include:
- repo name
- issue title
- why it was recommended
- first-step checklist

**Step 2: Run tests to verify failure**

Run: `pytest tests/test_briefs.py -v`
Expected: FAIL because brief generator does not exist.

**Step 3: Write minimal implementation**

Start with deterministic template-based briefs; keep the interface extensible for future LLM summaries.

**Step 4: Run tests to verify pass**

Run: `pytest tests/test_briefs.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add app/briefs.py tests/test_briefs.py
git commit -m "feat: add contribution brief generation"
```

### Task 7: Expose ranked opportunities via API

**Objective:** Serve sorted opportunities for downstream clients.

**Files:**
- Modify: `app/main.py`
- Create: `app/schemas.py`
- Create: `tests/test_opportunities_api.py`

**Step 1: Write failing API test**

Assert `/opportunities` returns a JSON array sorted by score descending.

**Step 2: Run test to verify failure**

Run: `pytest tests/test_opportunities_api.py -v`
Expected: FAIL because the endpoint is not implemented.

**Step 3: Write minimal implementation**

Implement the endpoint with optional filters:
- language
- label
- minimum score
- status

**Step 4: Run test to verify pass**

Run: `pytest tests/test_opportunities_api.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add app/main.py app/schemas.py tests/test_opportunities_api.py
git commit -m "feat: expose ranked opportunities api"
```

### Task 8: Add ingestion CLI / script entrypoint

**Objective:** Make local refreshes and cron execution straightforward.

**Files:**
- Create: `scripts/refresh_data.py`
- Modify: `pyproject.toml`
- Create: `tests/test_refresh_script.py`

**Step 1: Write failing test**

Assert the refresh script runs the ingestion and scoring pipeline without crashing when GitHub responses are mocked.

**Step 2: Run test to verify failure**

Run: `pytest tests/test_refresh_script.py -v`
Expected: FAIL because script entrypoint is missing.

**Step 3: Write minimal implementation**

Add a script that:
- loads seed repos
- ingests repository/issue data
- computes scores
- persists opportunities

**Step 4: Run test to verify pass**

Run: `pytest tests/test_refresh_script.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add scripts/refresh_data.py pyproject.toml tests/test_refresh_script.py
git commit -m "feat: add refresh pipeline entrypoint"
```

### Task 9: Document architecture and local usage

**Objective:** Make the project understandable for contributors.

**Files:**
- Create: `docs/architecture.md`
- Modify: `README.md`

**Step 1: Write architecture doc**

Describe the ingestion, storage, scoring, and API flow with clear boundaries.

**Step 2: Add local run instructions**

Include setup, environment variables, test commands, and a sample refresh flow.

**Step 3: Verify docs coherence**

Read both files and ensure commands and paths match the actual scaffold.

**Step 4: Commit**

```bash
git add docs/architecture.md README.md
git commit -m "docs: add architecture and local usage guide"
```

### Task 10: Final verification pass

**Objective:** Ensure the MVP is shippable for the first public iteration.

**Files:**
- Modify as needed based on findings from verification

**Step 1: Run full test suite**

Run: `pytest -v`
Expected: all tests pass.

**Step 2: Run app locally**

Run: `uvicorn app.main:app --reload`
Expected: API starts and `/health` responds with 200.

**Step 3: Run refresh pipeline**

Run: `python scripts/refresh_data.py`
Expected: repository and issue data are fetched and scored without exceptions.

**Step 4: Sanity-check opportunities endpoint**

Run: `curl http://127.0.0.1:8000/opportunities`
Expected: ranked JSON results.

**Step 5: Commit final polish**

```bash
git add .
git commit -m "chore: finalize mvp baseline"
```

---

## Suggested first seed repositories

Start with a deliberately small set:

- `fastapi/fastapi`
- `pallets/flask`
- `huggingface/transformers`
- `langchain-ai/langchain`
- `openai/openai-python`
- `microsoft/TypeScript`

## Environment variables

- `GITHUB_TOKEN` — optional but recommended to avoid low rate limits
- `GITHUB_API_BASE_URL` — optional override for testing
- `DATABASE_URL` — defaults to local SQLite path

## Verification checklist

- [ ] API bootstraps locally
- [ ] SQLite schema initializes correctly
- [ ] GitHub ingestion handles pagination and empty issue lists
- [ ] Scoring is deterministic for identical inputs
- [ ] `/opportunities` sorts by descending score
- [ ] Brief output is readable and actionable
- [ ] README setup instructions match the codebase

## Notes

- Keep the first version deterministic and inspectable.
- Do not add embeddings, vector DBs, or agent orchestration in v1.
- Prefer explicit heuristics first, then layer AI summaries on top.
- Optimize for contributor usefulness, not architectural sophistication.
