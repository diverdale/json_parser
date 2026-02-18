# Coding Conventions

**Analysis Date:** 2026-02-18

## Naming Patterns

**Files:**
- Module files use lowercase with underscores: `json_parser.py`
- Package directory matches module name: `src/json_parser/`
- Test files follow pytest convention: `test_*.py`

**Classes:**
- PascalCase for class names: `JsonParser`, `JsonParserException`
- Exception classes suffixed with `Exception`: `JsonParserException`

**Functions:**
- Snake_case for function and method names: `get_data()`, `get_args()`, `get_json()`, `_search_dict()`
- Getter methods prefixed with `get_`: `get_data()`, `get_args()`, `get_json()`
- Private/internal methods use underscore prefix: `_search_dict()` (instance method, previously a nested function)

**Variables:**
- Snake_case for variable names: `json_obj`, `json_data`, `keys_to_search`, `found`, `nested_found`, `nested_key`, `nested_value`
- Descriptive names used throughout: `dct` for dictionary parameter, `keys_to_search` for pattern list

**Type hints:**
- Function parameters use type hints: `def __init__(self, msg: str)` in `JsonParserException`
- Return types not explicitly annotated in most methods

## Code Style

**Formatting:**
- No explicit formatter detected (black, isort, autopep8 not configured)
- Indentation: 4 spaces (standard Python)
- Lines follow implicit 80-100 character guideline
- Spacing around operators: `key not in found`, `isinstance(value, dict)`

**Linting:**
- No linting configuration detected (no .flake8, .pylintrc, setup.cfg, or ruff config)
- Code follows PEP 8 conventions implicitly

## Import Organization

**Order:**
1. Standard library imports: `import fnmatch`, `import sys, os`, `import json`
2. Application imports: `from json_parser import JsonParser`

**Path Aliases:**
- No path aliases detected
- Test setup uses `sys.path.append()` to inject `src/` directory for imports: `sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")`

## Error Handling

**Patterns:**
- Custom exception class `JsonParserException` extends `Exception`
- Constructor validation in `__init__()` raises exceptions for missing inputs:
  ```python
  if not obj:
      raise JsonParserException(msg='JSON object must be present')
  if not args:
      raise JsonParserException(msg='No keys present to parse')
  ```
- Exceptions use named parameter `msg=` when raising
- No try/except blocks in main logic; errors propagate upward

## Logging

**Framework:** Not implemented

**Patterns:**
- No logging framework imported or used
- No debug output in core logic
- Examples use `print(json.dumps(result, indent=4))` for output

## Comments

**When to Comment:**
- Module-level author comment at top: `# Dale Wright`
- Class-level docstrings provided for public classes

**JSDoc/TSDoc:**
- Uses Python docstrings for class documentation:
  ```python
  """
      The JsonParser class.

      Methods:
      __init__(self, obj, args)
          returns the JsonParser object
      ...
  """
  ```
- Docstring format: multi-line string describing class and listing methods
- Method-level docstrings not used

## Function Design

**Size:** Methods are concise (3-10 lines for getters, ~40 lines for main `get_data()`)

**Parameters:**
- Constructor takes two parameters: `obj` (JSON list), `args` (key list)
- `_search_dict()` method takes: `dct`, `keys_to_search`, `current_path`, `current_depth`, `max_depth`, `path` — state passed explicitly through recursion

**Return Values:**
- Getters return unmodified instance attributes
- `get_data()` returns list of dicts with extracted keys
- `search_dict()` returns dict with matched keys and values

## Module Design

**Exports:**
- Both classes exported from `src/json_parser/__init__.py`:
  ```python
  # JsonParserException
  # JsonParser
  ```
- Imported directly: `from json_parser import JsonParser`

**Barrel Files:**
- Package uses `__init__.py` as barrel file containing both `JsonParserException` and `JsonParser`

---

*Convention analysis: 2026-02-18*
