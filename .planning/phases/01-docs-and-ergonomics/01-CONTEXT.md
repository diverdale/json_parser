# Phase 1: Docs and Ergonomics - Context

**Gathered:** 2026-02-18
**Status:** Ready for planning

<domain>
## Phase Boundary

Write a comprehensive README and expand `JsonParser` to accept raw JSON strings, single dicts, and provide a module-level `parse()` one-liner. Documentation and input ergonomics only — new search features (path tracking, depth, case sensitivity) belong in Phase 2.

</domain>

<decisions>
## Implementation Decisions

### README structure
- Problem statement first — open with "Tired of writing nested loops for JSON?" framing before showing code
- Badges at the top (PyPI version, Python versions, license)
- Installation section: `pip install json-key-parser` only (no Poetry instructions)
- Quick-start only approach — document the core pattern clearly, keep it short and scannable
- Do NOT enumerate every public method — link to inline code or keep README lean

### Example scenarios
- Quick-start example uses person/contact data (first_name, address, phone) — universally relatable
- Additional examples inline in README (self-contained, copy-paste ready — not referencing examples/ folder)
- Number of additional examples and whether to show wildcard/duplicate handling in quick-start: Claude's discretion — whatever demonstrates the library's range most clearly

### Claude's Discretion
- Whether to show wildcards and duplicate handling in the quick-start or in dedicated sections
- Number of real-world examples beyond the quick-start (show the library's range)
- Exact wording of the problem statement hook
- README section ordering after quick-start (Features, Why this library, etc.)
- Error behavior for new input types (malformed JSON strings, wrong shapes) — use sensible Python conventions

</decisions>

<specifics>
## Specific Ideas

- The problem statement should resonate with any Python developer who has wrestled with `response['data'][0]['user']['address']['city']` style extraction
- Person/contact data for quick-start — people data already exists in `examples/people_list.py`, can draw from that

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 01-docs-and-ergonomics*
*Context gathered: 2026-02-18*
