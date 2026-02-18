# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-18)

**Core value:** Any Python developer can extract any key from any JSON structure in one line — without writing nested loops, try/excepts, or custom traversal code.
**Current focus:** Phase 2 complete — ready for Phase 3 (Packaging)

## Current Position

Phase: 2 of 3 (Power Features) — COMPLETE
Plan: 2 of 2 complete in current phase
Status: Phase complete
Last activity: 2026-02-18 — Plan 02-02 (case-insensitive key matching) complete

Progress: [████░░░░░░] 40%

## Performance Metrics

**Velocity:**
- Total plans completed: 4
- Average duration: 1.5 min
- Total execution time: 0.1 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 01-docs-and-ergonomics | 2 | 3 min | ~2 min |
| 02-power-features | 2 | 3 min | ~1.5 min |

**Recent Trend:**
- Last 5 plans: 01-01 (2 min), 01-02 (1 min), 02-01 (2 min), 02-02 (1 min)
- Trend: Stable

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- [Setup]: docs-first priority — README before feature work; drives Phase 1 containing both DOCS and API requirements together
- [Setup]: Path tracking is the next major differentiating feature — `search_dict()` needs refactoring out of nested function position before Phase 2
- [01-01]: README problem hook uses `response['data'][0]['user']['address']['city']` as the concrete pain point — visceral and universally recognizable
- [01-01]: No API reference table in README — keeps it scannable rather than exhaustive
- [01-02]: Use Union[str, dict, list] (typing module) not str|dict|list — Python 3.8 compat
- [01-02]: parse() delegates entirely to JsonParser — no duplicated logic
- [02-01]: _search_dict extracted as method so path/depth state passes cleanly through recursion
- [02-01]: Lists transparent to depth counting — only descending into a dict increments depth
- [02-01]: path=True wraps each match as {value, path} dict; duplicate keys produce list of path-value dicts
- [02-01]: max_depth=0 handled with early return to return empty dict immediately
- [02-02]: case_sensitive=True default — zero behavior change for all existing callers
- [02-02]: Lowercase both sides for fnmatch comparison — symmetric and correct for wildcard patterns
- [02-02]: Break-after-first-match prevents case-variant query key duplication (e.g. ['city', 'City'] produces one result)
- [02-02]: Output key always uses original JSON casing — naturally preserved, no extra logic needed

### Pending Todos

None yet.

### Blockers/Concerns

- `args` parameter name (should be `keys`) — backward-compat constraint means rename must be additive

## Session Continuity

Last session: 2026-02-18
Stopped at: Completed 02-02-PLAN.md (case-insensitive key matching). FEAT-03 implemented and tested. Phase 02-power-features complete.
Resume file: None
