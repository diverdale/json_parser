# Codebase Concerns

**Analysis Date:** 2026-02-18

## Code Quality & Maintainability

**Nested function with high cyclomatic complexity:**
- Issue: `search_dict()` is a deeply nested function inside `get_data()` with repeated conditional logic patterns for handling dict/list type checking and duplicate key merging
- Files: `src/json_parser/__init__.py` (lines 51-88)
- Impact: Difficult to debug, test independently, and modify; similar duplicate key merging logic appears in three locations (lines 56-61, 68-73, 82-87)
- Fix approach: Extract `search_dict()` as a method on the class; create helper methods for "merge_found_values()" to consolidate duplicate logic; consider refactoring type checking and merging into separate functions

**Repeated duplicate key merging logic:**
- Issue: Lines 56-61, 68-73, and 82-87 implement nearly identical logic for converting singular values to lists and appending duplicates
- Files: `src/json_parser/__init__.py`
- Impact: Maintenance burden; any fix to the merge logic must be applied in three places; inconsistencies could be introduced
- Fix approach: Extract into a helper method like `_merge_value(key, new_value, found_dict)` and call it from all three locations

**Missing type hints:**
- Issue: No type annotations on methods or function signatures
- Files: `src/json_parser/__init__.py` (entire file)
- Impact: Reduced IDE support, autocomplete, and static analysis; harder for new contributors to understand expected types
- Fix approach: Add type hints to `__init__()`, `get_data()`, `get_args()`, `get_json()` and the inner `search_dict()` function; use `typing` module for complex types

## Test Coverage Gaps

**Limited test scenarios:**
- Issue: Only 3 tests covering basic functionality (`get_data`, `get_args`, duplicate key merging)
- Files: `tests/test_json_parser.py`
- Impact: Edge cases and error conditions not validated; wildcard patterns not tested; deeply nested structures not covered
- Priority: High
- Missing coverage:
  - `fnmatch` wildcard matching patterns (e.g., `address*`, `*name`, `street?`)
  - Error cases: empty dicts, deeply nested structures (5+ levels), circular references
  - Edge cases: None values, numeric keys, special characters in keys, Unicode keys
  - Large datasets (performance/memory behavior)
  - Mixed type values in duplicate key lists
  - Non-dict items in top-level list (lines 92-94 only checks `isinstance(item, dict)` but doesn't test non-dict behavior)

**No exception testing:**
- Issue: `JsonParserException` is raised for missing `obj` or `args` but no test validates these exceptions
- Files: `tests/test_json_parser.py` (missing tests for lines 31-38 validation)
- Risk: Input validation behavior could regress silently
- Priority: Medium

**No integration tests:**
- Issue: Tests only use single record with fixed structure; no tests with multiple records or varying structures
- Files: `tests/test_json_parser.py`
- Risk: Interactions between multiple items in `json_obj` list not validated
- Priority: Medium

## Potential Runtime Issues

**Non-dict items in top-level list silently skipped:**
- Issue: If user passes `[{"key": "value"}, "not_a_dict"]`, non-dict items are silently skipped (line 93 checks but doesn't handle)
- Files: `src/json_parser/__init__.py` (line 92-94)
- Impact: Silent data loss; user won't know some records weren't processed
- Fix approach: Raise `JsonParserException` or add logging; document behavior clearly

**No validation of args parameter structure:**
- Issue: `args` is only checked for truthiness (line 35-37) but not validated as iterable or list of strings
- Files: `src/json_parser/__init__.py` (lines 35-38)
- Impact: If user passes non-iterable or non-string items, error will occur inside `fnmatch.fnmatch()` at runtime with unclear traceback
- Fix approach: Add type validation in `__init__()` to check `args` is list and all items are strings; raise `JsonParserException` with clear message

**Unhandled edge case: empty found results:**
- Issue: If no keys match any patterns, an empty dict `{}` is appended to results for each input record
- Files: `src/json_parser/__init__.py` (lines 91-95)
- Impact: May not be desired behavior; user may expect only records with matches or a different empty representation
- Fix approach: Document this behavior explicitly in docstring; consider option to filter out empty results

## Documentation Gaps

**Docstring needs expansion:**
- Issue: Class docstring (lines 11-27) lists method signatures but lacks examples, behavior descriptions, or parameter types
- Files: `src/json_parser/__init__.py`
- Impact: Harder for new users/developers to understand without reading source code
- Fix approach: Update docstring with parameter types, return types, exceptions, and examples

**Behavior ambiguity not documented:**
- Issue: Duplicate key merging produces lists that can be scalar or list of scalars; impact on JSON serialization unclear
- Files: README.md, `src/json_parser/__init__.py`
- Impact: User confusion about output shape; example on line 143-147 in README shows inconsistent output (sometimes string, sometimes list)
- Fix approach: Document clearly that duplicate key values become lists; show examples in docstring and README

**Wildcard matching behavior underdocumented:**
- Issue: Uses `fnmatch.fnmatch()` but documentation doesn't explain all patterns (`?`, `[seq]`, `[!seq]`)
- Files: README.md (line 91)
- Impact: Users may expect different wildcard behavior (e.g., regex-style)
- Fix approach: Document exact `fnmatch` patterns supported with examples

## Build & Packaging Issues

**Dual build system configured:**
- Issue: Both `pyproject.toml` (Poetry) and presumed `setup.py` exist; unclear which is primary
- Files: `pyproject.toml` and `setup.py` (if present)
- Impact: Build inconsistency; installation may fail or use wrong config
- Fix approach: Verify only Poetry is used; remove `setup.py` if it exists; ensure only one build backend

**Package version duplication:**
- Issue: Version hardcoded in `pyproject.toml` (line 3: "0.0.2"); should use single source of truth
- Files: `pyproject.toml`
- Impact: Easy to forget updating version; version mismatch between PyPI and git tags
- Fix approach: Use dynamic versioning from git tags or single version file; implement automated version bumping

## Robustness Gaps

**No validation of fnmatch patterns:**
- Issue: Invalid patterns passed in `args` are not validated; `fnmatch.fnmatch()` may behave unexpectedly
- Files: `src/json_parser/__init__.py` (line 55)
- Impact: Silent failures or unexpected behavior with malformed patterns
- Fix approach: Document pattern format; consider catching fnmatch exceptions

**JSON object input type not strictly validated:**
- Issue: `obj` checked for truthiness (line 31) but not checked if it's actually a list or list of dicts
- Files: `src/json_parser/__init__.py` (lines 31-34)
- Impact: If user passes `{"key": "value"}` instead of list, error occurs deep in `get_data()` with unclear traceback
- Fix approach: Validate `obj` is list and contains only dicts; raise `JsonParserException` with clear message

---

*Concerns audit: 2026-02-18*
