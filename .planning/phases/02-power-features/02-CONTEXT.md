# Phase 2: Power Features - Context

**Gathered:** 2026-02-18
**Status:** Ready for planning

<domain>
## Phase Boundary

Add three new controls to `get_data()`: path tracking (return dot-notation paths alongside matched values), depth limiting (stop recursion at a given nesting level), and case-insensitive matching. No new output types, no new top-level commands — this is an API extension to the existing `JsonParser` class and `parse()` shortcut.

</domain>

<decisions>
## Implementation Decisions

### Path return format
- Claude's discretion — pick the most Pythonic, readable, and consistent format
- Must work correctly when the same key matches multiple times (current behavior merges values into a list)
- Every match should carry its own path so callers can distinguish identical values from different locations

### Depth semantics
- Claude's discretion — define what "depth 1" means and document it clearly
- Handle list traversal consistently (document whether lists consume a depth level or not)
- Handle edge cases (max_depth=0, max_depth=None) sensibly

### Case-insensitive matching
- `case_sensitive=False` applies to **everything** — exact key names AND wildcard patterns
  - e.g. `"address*"` with `case_sensitive=False` matches `"Address1"`, `"ADDRESS_city"`, etc.
- When the caller's key list contains case-variant duplicates (e.g. `["city", "City"]`) with `case_sensitive=False`, merge into a single result key — don't produce two entries
- Output key name (original JSON casing vs query casing): Claude's discretion — pick the most predictable behavior

### Backward compatibility
- All new parameters must default to preserving existing behavior:
  - `path=False` (no paths in output by default)
  - `max_depth=None` (no depth limit by default)
  - `case_sensitive=True` (current behavior by default)
- Existing callers that don't pass the new params must not see any change in output

### Claude's Discretion
- Path return format (tuple vs dict vs flat key — pick the most Pythonic)
- Depth counting semantics (what counts as "depth 1", whether lists consume a level)
- Output key name when case_sensitive=False (query key vs original JSON key)
- Whether `parse()` module-level function also receives the new parameters
- Whether new params live on `get_data()` only or a separate method is better
- Whether to clean up the existing `*args` signature (backward compat required if changed)
- max_depth=0 edge case handling

</decisions>

<specifics>
## Specific Ideas

No specific requirements — open to standard approaches.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 02-power-features*
*Context gathered: 2026-02-18*
