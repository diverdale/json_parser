# Roadmap: json-key-parser

## Overview

Starting from a working prototype, this roadmap takes json-key-parser from an undocumented library to a polished, featureful PyPI package. Phase 1 gets the library documented and ergonomically improved. Phase 2 adds the power features that differentiate it. Phase 3 ensures quality and a professional PyPI presence.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Docs and Ergonomics** - Write the README and expand the input API so the library is immediately usable
- [ ] **Phase 2: Power Features** - Add path tracking, depth limiting, and case-insensitive matching
- [ ] **Phase 3: Quality and Ship** - Achieve 90%+ test coverage and polish the PyPI package page

## Phase Details

### Phase 1: Docs and Ergonomics
**Goal**: The library is documented and accepts the full range of inputs any developer would naturally try
**Depends on**: Nothing (first phase)
**Requirements**: DOCS-01, DOCS-02, API-01, API-02, API-03
**Success Criteria** (what must be TRUE):
  1. A developer landing on the README can copy a working 3-line extraction example from the top of the page
  2. A developer can see real-world examples (network configs, API responses, nested people data) in the README and understand the library's range
  3. A developer can pass a raw JSON string directly to JsonParser without pre-parsing it
  4. A developer can pass a single dict (not wrapped in a list) to JsonParser and get results
  5. A developer can call `json_parser.parse(data, keys)` as a one-liner without instantiating the class
**Plans**: TBD

### Phase 2: Power Features
**Goal**: Users can control how the search runs — depth, case sensitivity — and discover where in the structure their matches came from
**Depends on**: Phase 1
**Requirements**: FEAT-01, FEAT-02, FEAT-03
**Success Criteria** (what must be TRUE):
  1. A developer can pass `path=True` (or equivalent) to `get_data()` and receive dot-notation paths alongside each matched value (e.g. `address1.street`)
  2. A developer can pass `max_depth=2` to limit recursion and verify that keys beyond that depth are not returned
  3. A developer can pass `case_sensitive=False` and match keys regardless of their capitalization in the source JSON
**Plans**: TBD

### Phase 3: Quality and Ship
**Goal**: The library has a professional test suite and a PyPI page that accurately represents its capabilities
**Depends on**: Phase 2
**Requirements**: QUAL-01, QUAL-02
**Success Criteria** (what must be TRUE):
  1. Running `pytest --cov` reports 90% or higher coverage, including empty input, deeply nested structures, no-match cases, and all error paths
  2. The PyPI package page at pypi.org/project/json-key-parser displays the full README as the long description
  3. The PyPI page lists Python 3.8-3.12 classifiers, relevant topic classifiers, and searchable keywords so the package appears in relevant searches
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Docs and Ergonomics | 0/TBD | Not started | - |
| 2. Power Features | 0/TBD | Not started | - |
| 3. Quality and Ship | 0/TBD | Not started | - |
