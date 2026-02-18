# Requirements: json-key-parser

**Defined:** 2026-02-18
**Core Value:** Any Python developer can extract any key from any JSON structure in one line — without writing nested loops, try/excepts, or custom traversal code.

## v1 Requirements

### Documentation

- [ ] **DOCS-01**: User can find a working extraction example in 3 lines or fewer at the top of the README
- [ ] **DOCS-02**: User can see real-world examples (network device configs, API responses, nested people data) in README

### API Ergonomics

- [ ] **API-01**: User can pass a raw JSON string as the `obj` argument (JsonParser parses it internally)
- [ ] **API-02**: User can pass a single dict as `obj`, not just a list-of-dicts
- [ ] **API-03**: User can call module-level `parse(data, keys)` as a one-liner alternative to the class interface

### Features

- [ ] **FEAT-01**: User can retrieve the dot-notation path where each key match was found (e.g. `address1.street` vs `address2.street`)
- [ ] **FEAT-02**: User can limit recursion depth via `max_depth` parameter to avoid deep traversal of large structures
- [ ] **FEAT-03**: User can perform case-insensitive key matching by passing `case_sensitive=False`

### Quality & Packaging

- [ ] **QUAL-01**: Test suite achieves 90%+ coverage including edge cases (empty input, deeply nested, no matches, mixed types) and all error cases
- [ ] **QUAL-02**: PyPI package page displays README as long description with full Python version classifiers, topic classifiers, and searchable keywords

## v2 Requirements

### Developer Experience

- **DX-01**: All public methods have complete docstrings with parameter descriptions and return types
- **DX-02**: Full type hints on all public API methods (`__init__`, `get_data`, `get_args`, `get_json`, `parse`)

### CI/CD

- **CI-01**: GitHub Actions workflow runs pytest against Python 3.8, 3.10, and 3.12 on every push and pull request

## Out of Scope

| Feature | Reason |
|---------|--------|
| YAML/XML parsing | JSON-focused — don't dilute the identity |
| JSON schema validation | Different tool category entirely |
| Write/mutation operations | Read-only extraction is the core value |
| Async/streaming large files | Keep it simple; not a primary use case |
| OAuth/auth handling | Library concern, not this library's job |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| DOCS-01 | — | Pending |
| DOCS-02 | — | Pending |
| API-01 | — | Pending |
| API-02 | — | Pending |
| API-03 | — | Pending |
| FEAT-01 | — | Pending |
| FEAT-02 | — | Pending |
| FEAT-03 | — | Pending |
| QUAL-01 | — | Pending |
| QUAL-02 | — | Pending |

**Coverage:**
- v1 requirements: 10 total
- Mapped to phases: 0
- Unmapped: 10 ⚠️

---
*Requirements defined: 2026-02-18*
*Last updated: 2026-02-18 after initial definition*
