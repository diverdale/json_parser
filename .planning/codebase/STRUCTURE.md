# Codebase Structure

**Analysis Date:** 2026-02-18

## Directory Layout

```
json_parser/
├── src/                    # Source code
│   └── json_parser/        # Main package
│       └── __init__.py     # JsonParser class and JsonParserException
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_json_parser.py # Unit tests
├── examples/               # Usage examples and sample data
│   ├── json_parser.py      # Standalone copy (duplicate of src)
│   ├── people_list.py      # Example: extract names and addresses
│   ├── network_devices.py  # Example: extract device properties
│   ├── scratch.py          # Development/experimentation script
│   ├── people.json         # Sample JSON data
│   ├── device_list.json    # Sample JSON data
│   ├── bakery.json         # Sample JSON data
│   └── legislators.json    # Sample JSON data
├── dist/                   # Built distributions (wheels, tarballs)
├── pyproject.toml          # Poetry configuration and dependencies
├── requirements.txt        # Python dependencies (pip)
├── CLAUDE.md               # Project instructions for Claude Code
├── README.md               # Project documentation
└── LICENSE                 # MIT License

```

## Directory Purposes

**`src/`:**
- Purpose: Production source code
- Contains: Python package implementation
- Key files: `src/json_parser/__init__.py`

**`src/json_parser/`:**
- Purpose: Main package directory
- Contains: Core `JsonParser` class, `JsonParserException`, all application logic
- Key files: `__init__.py` (single file containing entire library)

**`tests/`:**
- Purpose: Unit tests
- Contains: Test suite and test data
- Key files: `tests/test_json_parser.py` (unit tests), `tests/__init__.py`

**`examples/`:**
- Purpose: Usage demonstrations and documentation by example
- Contains: Example scripts, sample JSON datasets, standalone copy of JsonParser
- Key files: `people_list.py`, `network_devices.py` (runnable examples); `people.json`, `device_list.json` (test data)

**`dist/`:**
- Purpose: Built distribution packages
- Contains: Generated wheel and tarball files
- Generated: Yes (created by build system)
- Committed: No (ignored by git)

## Key File Locations

**Entry Points:**
- `src/json_parser/__init__.py`: Main library entry point, contains JsonParser class

**Configuration:**
- `pyproject.toml`: Poetry project configuration, dependencies, package metadata
- `requirements.txt`: Simple pip requirements list (maintains compatibility)
- `.python-version`: Python version specification (currently Python 3.8+)

**Core Logic:**
- `src/json_parser/__init__.py`: Single file containing JsonParser class and JsonParserException

**Testing:**
- `tests/test_json_parser.py`: Unit tests including basic extraction, duplicate key handling, wildcard patterns
- `tests/__init__.py`: Empty init file

**Examples:**
- `examples/people_list.py`: Demonstrates wildcard pattern matching (`*name`, `address*`)
- `examples/network_devices.py`: Demonstrates extraction from nested API responses
- `examples/json_parser.py`: Standalone copy of implementation (for reference/testing)
- `examples/scratch.py`: Development scratch space

## Naming Conventions

**Files:**
- Snake case: `test_json_parser.py`, `network_devices.py`
- Configuration: lowercase + extension: `pyproject.toml`, `requirements.txt`

**Directories:**
- Lowercase plural or semantic name: `src/`, `tests/`, `examples/`, `dist/`

**Python Module:**
- Package name: `json_parser` (matches import statement)
- All code in `__init__.py` (single-file module)

## Where to Add New Code

**New Feature (additional extraction methods):**
- Primary code: `src/json_parser/__init__.py` (add methods to JsonParser class)
- Tests: `tests/test_json_parser.py` (add test functions)

**New Example:**
- Implementation: `examples/[example_name].py`
- Test data: `examples/[data_name].json` (if needed)

**Utilities/Helpers:**
- If reusable: Add to `src/json_parser/__init__.py` as module-level functions or JsonParser methods
- If example-specific: Add to `examples/` directory

**Dependencies:**
- Update both: `pyproject.toml` (Poetry) and `requirements.txt` (pip)

## Special Directories

**`.planning/`:**
- Purpose: Planning and analysis documentation
- Contains: Architecture, structure, testing patterns, and concern documents
- Generated: Yes (created by analysis tooling)
- Committed: Yes (to version control)

**`.pytest_cache/`:**
- Purpose: Pytest cache
- Generated: Yes (by pytest)
- Committed: No (ignored by git)

**`__pycache__/`:**
- Purpose: Compiled Python bytecode
- Generated: Yes (by Python runtime)
- Committed: No (ignored by git)

---

*Structure analysis: 2026-02-18*
