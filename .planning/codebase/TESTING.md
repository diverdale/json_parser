# Testing Patterns

**Analysis Date:** 2026-02-18

## Test Framework

**Runner:**
- pytest 8.2.2
- Config: No explicit `pytest.ini` or `setup.cfg` config file (uses defaults)

**Assertion Library:**
- Built-in Python `assert` statements

**Run Commands:**
```bash
pytest tests/                          # Run all tests
pytest tests/test_json_parser.py       # Run specific test file
pytest tests/test_json_parser.py::test_get_data  # Run single test
```

## Test File Organization

**Location:**
- Separate directory: `tests/` at project root
- Located at `/Users/dalwrigh/dev/json_parser/tests/`

**Naming:**
- Test module: `test_json_parser.py`
- Test functions prefixed with `test_`: `test_get_data()`, `test_get_args()`, `test_dupe_keys()`

**Structure:**
```
json_parser/
├── src/
│   └── json_parser/
│       └── __init__.py          # Module under test
├── tests/
│   ├── __init__.py              # Empty init file
│   └── test_json_parser.py       # All tests in single file
```

## Test Structure

**Suite Organization:**
```python
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from json_parser import JsonParser

json_data = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
        "address1": {
            "street": "1208 Elm Street",
            "city": "Springfield",
            "zip_code": "62704"
        },
        "address2": {
            "street": "4965 Harvest Rd",
            "city": "Boston",
            "zip_code": "12345"
        },
        "birthday": "1984-05-23"
    }
]

def test_get_data():
    keys = ['first_name']
    data = JsonParser(json_data, keys)
    result = data.get_data()
    assert(result[0]['first_name']) == "John"

def test_get_args():
    keys = ['first_name', 'last_name']
    data = JsonParser(json_data, keys)
    result = data.get_args()
    assert result == ['first_name', 'last_name']

def test_dupe_keys():
    keys = ['street']
    data = JsonParser(json_data, keys)
    result = data.get_data()
    assert (len(result[0]['street'])) == 2
```

**Patterns:**
- Test data defined at module level: `json_data` (reused across tests)
- Each test function defines its own `keys` list
- Instantiate `JsonParser` fresh for each test
- Immediate assertions without helper methods

**Setup/Teardown:**
- No setup or teardown fixtures used
- Test data is static module-level variable
- Each test is self-contained and idempotent

## Mocking

**Framework:** Not used

**Patterns:**
- No mocking framework imported (unittest.mock not used)
- All tests use real `JsonParser` class with real data

**What to Mock:**
- Currently no external dependencies to mock (fnmatch is from stdlib)

**What NOT to Mock:**
- JsonParser methods are tested directly without mocks

## Fixtures and Factories

**Test Data:**
```python
json_data = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
        "address1": {
            "street": "1208 Elm Street",
            "city": "Springfield",
            "zip_code": "62704"
        },
        "address2": {
            "street": "4965 Harvest Rd",
            "city": "Boston",
            "zip_code": "12345"
        },
        "birthday": "1984-05-23"
    }
]
```

**Location:**
- Module-level variable in `tests/test_json_parser.py`
- Reused across all three test functions
- Contains nested dicts for testing recursive search and duplicate key merging

## Coverage

**Requirements:** No coverage enforcement detected

**View Coverage:**
```bash
# Install pytest-cov if needed
pytest --cov=src tests/
```

## Test Types

**Unit Tests:**
- Single test class (`JsonParser`) tested directly
- Tests focus on public methods: `get_data()`, `get_args()`, `get_json()`
- Current coverage: 3 tests

**Integration Tests:**
- Not present

**E2E Tests:**
- Not present
- Examples directory contains manual integration examples: `examples/people_list.py`, `examples/network_devices.py`

## Common Patterns

**Assertion Pattern:**
```python
# Direct assert with inline instantiation
def test_get_data():
    keys = ['first_name']
    data = JsonParser(json_data, keys)
    result = data.get_data()
    assert(result[0]['first_name']) == "John"
```

**Testing Exception Handling:**
- Not currently tested (no test for `JsonParserException` raise on empty obj/args)

**Testing Edge Cases:**
- Duplicate key merging tested: `test_dupe_keys()` verifies `street` key found in both `address1` and `address2` is merged into a list
- No tests for edge cases: empty args, null/None values, deeply nested structures, wildcard patterns

## Test Dependency Management

**Dependencies:**
- `pytest==8.2.2` in `requirements.txt`
- Standard library only: `sys`, `os`, `json`, `fnmatch`

**Installation:**
```bash
pip install -r requirements.txt
# or
pip install pytest==8.2.2
```

---

*Testing analysis: 2026-02-18*
