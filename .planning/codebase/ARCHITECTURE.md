# Architecture

**Analysis Date:** 2026-02-18

## Pattern Overview

**Overall:** Single-responsibility library pattern with recursive tree traversal.

**Key Characteristics:**
- Stateless utility class that performs pattern-matching searches
- Pure functions without external dependencies (only stdlib `fnmatch`)
- Recursive depth-first traversal of nested dictionaries and lists
- Automatic aggregation of duplicate keys into lists

## Layers

**Public API Layer:**
- Purpose: Expose JsonParser class and exception handling
- Location: `src/json_parser/__init__.py`
- Contains: `JsonParser` class (initialization, getters, data extraction), `JsonParserException` (error handling)
- Depends on: Python stdlib (`fnmatch`)
- Used by: Example scripts, external consumers

**Core Logic Layer:**
- Purpose: Recursive search implementation
- Location: `src/json_parser/__init__.py` (nested function `search_dict` within `get_data()`)
- Contains: Pattern matching logic, nested traversal, duplicate key aggregation
- Depends on: `fnmatch.fnmatch()` for wildcard pattern matching
- Used by: `JsonParser.get_data()` method

## Data Flow

**Parsing Flow:**

1. User instantiates `JsonParser(json_obj, keys_to_find)`
   - `json_obj`: List of dictionaries (required)
   - `keys_to_find`: List of key patterns (required)

2. `get_data()` is called
   - Iterates through each dictionary in the input list
   - For each dict, calls `search_dict()` recursively

3. `search_dict()` performs depth-first traversal
   - At each level, matches dictionary keys against patterns using `fnmatch`
   - Recursively descends into nested dicts (any dict values)
   - Recursively descends into dicts within lists (any list values containing dicts)
   - Accumulates matches in a `found` dictionary

4. Duplicate Key Handling
   - First occurrence: stored as single value
   - Subsequent occurrences: converted to list, values appended
   - Nested results from lower levels merged using same list-aggregation logic

5. Returns list of result dictionaries (one per input dict)

**State Management:**
- No state maintained between calls
- Each call to `get_data()` starts fresh
- Intermediate state only exists in `found` dict during traversal

## Key Abstractions

**JsonParser Class:**
- Purpose: Encapsulate initialization validation and provide stable public interface
- Examples: `src/json_parser/__init__.py` lines 10-95
- Pattern: Facade pattern - hides recursive complexity behind simple method interface

**search_dict() Nested Function:**
- Purpose: Recursive pattern-matching traversal engine
- Examples: `src/json_parser/__init__.py` lines 51-88
- Pattern: Recursive depth-first search with in-place accumulation

**JsonParserException:**
- Purpose: Custom exception for validation errors
- Examples: `src/json_parser/__init__.py` lines 5-7
- Pattern: Custom exception for domain-specific errors

## Entry Points

**Public Methods:**

`__init__(obj, args)`
- Location: `src/json_parser/__init__.py` lines 29-41
- Triggers: Instantiation of JsonParser
- Responsibilities: Validate inputs (non-empty obj and args), store as instance variables

`get_data()`
- Location: `src/json_parser/__init__.py` lines 50-95
- Triggers: User calls method on JsonParser instance
- Responsibilities: Iterate input list, invoke `search_dict()` on each dict, return aggregated results

`get_args()`
- Location: `src/json_parser/__init__.py` lines 43-44
- Triggers: User needs to retrieve original search keys
- Responsibilities: Return stored args list

`get_json()`
- Location: `src/json_parser/__init__.py` lines 46-47
- Triggers: User needs to retrieve original input
- Responsibilities: Return stored json_obj list

## Error Handling

**Strategy:** Fail-fast validation on initialization

**Patterns:**
- Empty JSON object raises `JsonParserException('JSON object must be present')` (line 32-33)
- Empty args list raises `JsonParserException('No keys present to parse')` (line 35-36)
- Invalid dict items in traversal are silently skipped (line 93: `if isinstance(item, dict)`)
- Non-dict/non-list values treated as leaf nodes (no further recursion)

## Cross-Cutting Concerns

**Logging:** Not implemented - library is silent by design

**Validation:** Only at initialization - input shape checked, no runtime type checking during traversal

**Pattern Matching:** Uses `fnmatch.fnmatch()` (Unix shell-style wildcards: `*`, `?`, `[seq]`)

**Key Merging:** When same key appears multiple times:
- First match: stored as-is
- Subsequent matches: converted to list, values appended
- Nested list results: extended into parent list

---

*Architecture analysis: 2026-02-18*
