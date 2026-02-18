# json-key-parser

## What This Is

A lightweight Python library for extracting specific key-value pairs from deeply nested JSON structures. `JsonParser` takes a JSON array of dicts and a list of key patterns, recursively searches every level, and returns only the matching keys — with duplicate values elegantly merged. Zero external dependencies.

## Core Value

Any Python developer can extract any key from any JSON structure in one line — without writing nested loops, try/excepts, or custom traversal code.

## Requirements

### Validated

- ✓ Recursive key extraction from arbitrarily nested dicts and lists — existing
- ✓ Wildcard key matching via `fnmatch` (e.g. `address*` matches `address`, `address1`, `address2`) — existing
- ✓ Duplicate key values merged into lists automatically — existing
- ✓ Zero external dependencies (stdlib only) — existing
- ✓ PyPI distribution as `json-key-parser` — existing (v0.0.2)

### Active

- [ ] Comprehensive README with real-world examples and quick-start guide
- [ ] Full type hints throughout public API for IDE support
- [ ] Accept raw JSON strings and file paths as input (not just pre-parsed list-of-dicts)
- [ ] Accept single dict input in addition to list-of-dicts
- [ ] Convenience module-level function (e.g. `json_parser.parse(data, keys)`)
- [ ] Path tracking — return the dot-notation path where each key was found
- [ ] Depth limit option — restrict how deep the search recurses
- [ ] Case-insensitive key matching option
- [ ] Comprehensive test suite (90%+ coverage, edge cases, error cases)
- [ ] CI/CD with GitHub Actions (test on Python 3.8–3.12)
- [ ] PyPI metadata polish — classifiers, long description from README, keywords

### Out of Scope

- YAML/XML parsing — JSON-focused, don't dilute the identity
- JSON schema validation — different tool category
- Write/mutation operations — read-only extraction only
- Async/streaming support — keep it simple for v1 extensibility

## Context

Existing codebase is a working prototype at `src/json_parser/__init__.py`. Core recursive logic is solid. The `search_dict()` function is a nested function inside `get_data()` — this pattern works but will need refactoring for path tracking to be implementable cleanly.

The `args` parameter name (should be `keys`) is a minor usability issue. Constructor currently only validates truthiness of inputs, not shape.

Two near-identical build artifacts exist in `dist/` (v0.0.1 and v0.0.2 both present) — worth cleaning up.

## Constraints

- **Backward compatibility**: Existing `JsonParser(obj, args)` API must continue to work as callers upgrade
- **Zero runtime deps**: Only stdlib — this is a selling point, protect it
- **Python 3.8+**: Minimum version from pyproject.toml; type hints must be compatible (use `Optional`, `List` etc. not `X | Y` syntax)
- **Poetry**: Primary build system — don't switch, keep lockfile in sync

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| docs-first priority for adoption | Devs won't try unloved/undocumented libraries | — Pending |
| Growing/extensible architecture | Not a one-trick script — more features will come | — Pending |
| Path tracking as next major feature | Solves the "which address1 or address2 did this come from?" problem elegantly | — Pending |

---
*Last updated: 2026-02-18 after initialization*
