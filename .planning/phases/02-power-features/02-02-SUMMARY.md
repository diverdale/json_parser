---
phase: 02-power-features
plan: 02
subsystem: api
tags: [python, json, case-insensitive, fnmatch, tdd]

# Dependency graph
requires:
  - phase: 02-power-features
    plan: 01
    provides: _search_dict() instance method with path and max_depth params
provides:
  - get_data(case_sensitive=False) matching keys regardless of capitalization
  - Wildcard patterns respect case_sensitive flag via fnmatch.fnmatch(key.lower(), pattern.lower())
  - Output keys always use original JSON casing when case_sensitive=False
  - case-variant query keys produce a single result entry (deduplication via break-after-first-match)
  - parse() supports case_sensitive param with default True (parity with get_data)
affects: [03-packaging, future-api-consumers]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "TDD Red-Green cycle for new feature flag"
    - "Lowercase-both-sides fnmatch for case-insensitive matching"
    - "Break-after-first-match deduplication of case-variant query keys"

key-files:
  created: []
  modified:
    - src/json_parser/__init__.py
    - tests/test_json_parser.py

key-decisions:
  - "case_sensitive=True default — zero behavior change for all existing callers"
  - "Lowercase both key and pattern for comparison (not just one side) — symmetric and correct for fnmatch wildcards"
  - "Output key always uses original JSON casing (the key variable from dct.items(), not the pattern) — naturally preserved without extra logic"
  - "Break after first matching pattern per JSON key prevents duplicate output when case-variant query keys provided (e.g. ['city', 'City'])"
  - "parse() updated to accept and forward case_sensitive for full parity with get_data()"

patterns-established:
  - "Feature flag defaulting to existing behavior: new params always default to the prior behavior value (True for case_sensitive, False for path, None for max_depth)"
  - "Single-match-per-key: break after first pattern match prevents both over-merging and case-variant duplication"

requirements-completed: [FEAT-03]

# Metrics
duration: 1min
completed: 2026-02-18
---

# Phase 2 Plan 02: Case-Insensitive Key Matching Summary

**case_sensitive=False flag added to get_data() and parse(), lowercasing both sides of fnmatch comparison with break-after-first-match deduplication and original JSON casing preserved in output**

## Performance

- **Duration:** 1 min
- **Started:** 2026-02-18T15:44:55Z
- **Completed:** 2026-02-18T15:46:40Z
- **Tasks:** 2 (RED + GREEN)
- **Files modified:** 2

## Accomplishments

- Implemented FEAT-03 case-insensitive key matching: `get_data(case_sensitive=False)` and `parse(..., case_sensitive=False)` now match JSON keys regardless of capitalization
- Wildcard patterns work case-insensitively when `case_sensitive=False` — `address*` matches `Address1`, `ADDRESS2`, etc.
- Output keys always use original JSON casing (not query key casing) — predictable, no surprises for callers
- Deduplication: case-variant query keys like `['city', 'City']` produce exactly one result entry per JSON key via break-after-first-match
- Default `case_sensitive=True` preserves exact-match behavior — zero regression for all existing callers

## Task Commits

Each task was committed atomically:

1. **Task 1: RED — failing tests for case-insensitive key matching** - `f4e130a` (test)
2. **Task 2: GREEN — implement case-insensitive matching in _search_dict** - `d5b4049` (feat)

**Plan metadata:** (docs commit follows)

_Note: TDD plan — test commit (RED) followed by implementation commit (GREEN)_

## Files Created/Modified

- `src/json_parser/__init__.py` - Added case_sensitive param to _search_dict(), get_data(), and parse(); updated matching logic and recursive calls
- `tests/test_json_parser.py` - Added 7 new FEAT-03 tests for exact key match, all-caps query, wildcard patterns, deduplication, output key casing

## Decisions Made

- **case_sensitive=True default:** All existing callers see zero change. Additive flag following the same pattern as path=False and max_depth=None.
- **Lowercase both sides for comparison:** `fnmatch.fnmatch(key.lower(), pattern.lower())` is symmetric and handles wildcard patterns correctly (a pattern like `Address*` lowercased to `address*` still matches `addressX` lowercased).
- **Output key = original JSON casing:** The `key` variable from `dct.items()` is always used as the result dict key — this is the natural behavior, no extra code needed.
- **Break-after-first-match for deduplication:** The existing `break` after the first matching pattern already prevents over-merging for single-pattern queries; it also ensures that when multiple patterns in the query list case-insensitively map to the same JSON key (e.g. `['city', 'City']`), only the first matching pattern triggers a write, eliminating duplicates.
- **parse() parity:** Updated to accept and forward `case_sensitive` so the one-liner convenience function maintains full parity with `get_data()`.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- FEAT-01 (path tracking), FEAT-02 (depth limiting), and FEAT-03 (case-insensitive matching) all implemented and tested
- All 26 tests pass; all existing callers unaffected (default params unchanged)
- _search_dict() is extensible — further params can be threaded through cleanly
- Phase 02-power-features complete; ready for Phase 03-packaging

---
*Phase: 02-power-features*
*Completed: 2026-02-18*

## Self-Check: PASSED

- src/json_parser/__init__.py: FOUND
- tests/test_json_parser.py: FOUND
- .planning/phases/02-power-features/02-02-SUMMARY.md: FOUND
- Commit f4e130a (RED tests): FOUND
- Commit d5b4049 (GREEN implementation): FOUND
