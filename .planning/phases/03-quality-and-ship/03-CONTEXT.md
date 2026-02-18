# Phase 3: Quality and Ship - Context

**Gathered:** 2026-02-18
**Status:** Ready for planning

<domain>
## Phase Boundary

Two deliverables: (1) Achieve 90%+ test coverage with `pytest --cov`, and (2) Polish the PyPI package so it shows the README as long description, has proper classifiers, keywords, and is built at v0.1.0 ready for manual publish. No automated publishing — user triggers `poetry publish` manually when satisfied.

</domain>

<decisions>
## Implementation Decisions

### Coverage scope
- Run `pytest --cov` first to see actual gaps — don't guess what's missing
- Fill gaps identified by the coverage report (error paths AND edge cases equally)
- Coverage target: 90% is the floor; aim higher if pragmatic given the library's size
- Enforcement: report only — no `--cov-fail-under` flag; the number is informational
- Combination tests (path + max_depth + case_sensitive together): Claude's discretion — add if coverage gaps point there

### PyPI publishing process
- Publish method: **manual** — `poetry publish` run by the developer when ready
- Version: **v0.1.0** — first meaningful release (bump from current 0.0.x)
- Phase deliverable: **publish-ready only** — not actually uploaded in this phase
- Clean `dist/` of stale 0.0.1 artifacts, run `poetry build` to produce fresh v0.1.0 wheel and sdist
- `pyproject.toml` must be updated to version 0.1.0

### Package metadata
- License: **MIT**
- Intended audience: **Developers** — any Python dev working with JSON APIs
- GitHub repo URL: User has a repo — planner/executor must include a `[tool.poetry.urls]` entry with a `"Repository"` key; **the actual URL will be filled in by the developer** (leave as a placeholder comment or `TODO` in pyproject.toml)
- One-line description: Claude's discretion — write the best short description for this library's audience
- Classifiers: Python 3.8–3.12 versions, `Intended Audience :: Developers`, `Topic :: Software Development :: Libraries :: Python Modules`, `Topic :: Utilities`, appropriate `Programming Language :: Python :: 3.x` entries
- Keywords: Claude's discretion — searchable terms a developer would use to find this library

### Claude's Discretion
- Exact one-line PyPI description (short, benefit-focused, accurate)
- Which specific classifiers to include beyond the required ones
- Keyword list (searchable terms for PyPI search)
- Whether to add combination param tests (defer to coverage report gaps)
- Coverage target ceiling (90% floor, aim higher if straightforward)

</decisions>

<specifics>
## Specific Ideas

- The `dist/` folder currently has stale 0.0.1 artifacts — explicitly remove and rebuild
- GitHub repo URL is user-controlled; leave a clear placeholder so it can't be missed

</specifics>

<deferred>
## Deferred Ideas

- GitHub Actions CI matrix (Python 3.8–3.12 test runs) — user skipped this area; not in scope for Phase 3

</deferred>

---

*Phase: 03-quality-and-ship*
*Context gathered: 2026-02-18*
