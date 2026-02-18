---
phase: 01-docs-and-ergonomics
plan: 02
subsystem: api
tags: [json, python, typing, fnmatch, pytest, tdd]

# Dependency graph
requires: []
provides:
  - JsonParser accepts raw JSON strings (calls json.loads internally)
  - JsonParser accepts a single dict (wraps in list automatically)
  - Module-level parse() convenience function delegating to JsonParser
  - Malformed JSON strings raise JsonParserException (not raw JSONDecodeError)
  - Python 3.8-compatible Union[] type hints on __init__ and parse()
affects:
  - Phase 2 (any work touching JsonParser.__init__ input handling)
  - Phase 3 (API surface changes must stay backward compatible)

# Tech tracking
tech-stack:
  added: [json (stdlib), typing.Union/List/Any (stdlib)]
  patterns: [TDD red-green cycle, isinstance() guards before validation, type-safe Union hints]

key-files:
  created: []
  modified:
    - src/json_parser/__init__.py
    - tests/test_json_parser.py

key-decisions:
  - "Use Union[str, dict, list] (typing module) not str|dict|list — Python 3.8 compat"
  - "isinstance(str) and isinstance(dict) checks placed BEFORE not-obj truthiness check so parse-then-validate order works"
  - "Malformed JSON re-raised as JsonParserException to avoid leaking internal stdlib exception types to callers"
  - "parse() delegates entirely to JsonParser — no duplicated logic"

patterns-established:
  - "Input normalization pattern: coerce type early in __init__, then validate"
  - "Exception wrapping: catch stdlib exceptions, re-raise as domain exceptions"

requirements-completed: [API-01, API-02, API-03]

# Metrics
duration: 1min
completed: 2026-02-18
---

# Phase 1 Plan 02: JsonParser API Expansion Summary

**JsonParser now accepts JSON strings, bare dicts, and exposes a module-level parse() one-liner — all three API expansions driven by TDD, with Union[] type hints for Python 3.8 compatibility.**

## Performance

- **Duration:** ~1 min
- **Started:** 2026-02-18T14:53:42Z
- **Completed:** 2026-02-18T14:54:52Z
- **Tasks:** 2 (TDD RED + TDD GREEN)
- **Files modified:** 2

## Accomplishments

- JSON string input: `JsonParser(json.dumps([...]), keys)` and `JsonParser(json.dumps({...}), keys)` both work without caller calling json.loads
- Single dict input: `JsonParser({"name": "x"}, ["name"])` wraps automatically and returns `[{"name": "x"}]`
- Module-level `parse(data, keys)` is importable and equivalent to `JsonParser(data, keys).get_data()`
- Malformed JSON strings raise `JsonParserException` with descriptive message (not raw `json.JSONDecodeError`)
- All 3 original tests still pass — full backward compatibility preserved
- 8 new tests added, total test count goes from 3 to 11

## Task Commits

Each TDD phase was committed atomically:

1. **RED phase: Failing tests** - `0eeb976` (test)
2. **GREEN phase: Implementation** - `b4c0ebc` (feat)

**Plan metadata:** (docs commit — see below)

_Note: No REFACTOR phase needed — implementation was clean on first pass._

## Files Created/Modified

- `/Users/dalwrigh/dev/json_parser/src/json_parser/__init__.py` - Added `import json`, `from typing import Union, List, Any`; isinstance(str)/isinstance(dict) guards in `__init__`; module-level `parse()` function
- `/Users/dalwrigh/dev/json_parser/tests/test_json_parser.py` - Added `import json`, `import pytest`, `parse` import; 8 new test functions covering all three new API behaviors

## Decisions Made

- Used `Union[str, dict, list]` from `typing` rather than `str | dict | list` — required for Python 3.8 compatibility (union syntax is Python 3.10+)
- Placed `isinstance(str)` and `isinstance(dict)` checks BEFORE the `if not obj:` guard so that empty-string and empty-dict cases still correctly flow through to the existing validation error path
- Malformed JSON re-raised as `JsonParserException("Invalid JSON string: {e}")` — keeps all error types consistent for callers, no leaking of `json.JSONDecodeError`
- `parse()` contains zero logic of its own — fully delegates to `JsonParser(obj, keys).get_data()` to avoid any drift between the two paths

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None — all three API behaviors worked correctly on the first implementation attempt.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- API ergonomics complete for Phase 1 requirements API-01, API-02, API-03
- `search_dict()` remains a nested function inside `get_data()` — Phase 2 path tracking work will require extracting it (noted in STATE.md blockers)
- `args` parameter name preserved for backward compat — additive rename approach still needed before Phase 2

---
*Phase: 01-docs-and-ergonomics*
*Completed: 2026-02-18*

## Self-Check: PASSED

- FOUND: src/json_parser/__init__.py
- FOUND: tests/test_json_parser.py
- FOUND: 01-02-SUMMARY.md
- FOUND: commit 0eeb976 (RED - failing tests)
- FOUND: commit b4c0ebc (GREEN - implementation)
