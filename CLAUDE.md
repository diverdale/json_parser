# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python library for extracting specific keys from JSON objects. `JsonParser` takes a JSON array of dicts and a list of key names, then recursively searches and returns only matching keys. Supports wildcard matching (`fnmatch`) and merges duplicate keys found at different nesting levels into lists.

## Build & Test

```bash
# Run all tests
pytest tests/

# Run a single test
pytest tests/test_json_parser.py::test_get_data

# Install dependencies
pip install -r requirements.txt
```

## Architecture

- **`src/json_parser.py`** — Single module containing `JsonParser` class and `JsonParserException`. The core logic is in `get_data()` which uses a recursive `search_dict()` to traverse nested dicts/lists.
- **`tests/test_json_parser.py`** — Tests import from `src/` via `sys.path` manipulation (no package install required).
- **`examples/`** — Usage examples with sample JSON files.

## Key Behaviors

- Input must be a list of dicts (iterated at top level in `get_data()`).
- Keys are matched using `fnmatch.fnmatch`, so `address*` matches `address`, `address1`, `address2`.
- When the same key is found multiple times (e.g. `street` in nested `address1` and `address2`), values are combined into a list.
- Build uses both `pyproject.toml` (Poetry) and `setup.py`; Poetry is the primary build system.
