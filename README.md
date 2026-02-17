# json_parser

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](/LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

A lightweight Python library for extracting specific keys from complex, nested JSON structures. Rather than manually traversing deeply nested objects, `json_parser` lets you declare the keys you care about and recursively retrieves their values — with support for wildcard matching and automatic merging of duplicate keys.

## Features

- **Key-based extraction** — Specify the keys you need and let the parser handle the traversal.
- **Wildcard matching** — Use glob-style patterns (e.g., `address*`) to match multiple keys at once.
- **Recursive search** — Automatically searches through nested dictionaries and lists.
- **Duplicate key merging** — When the same key appears at multiple levels, values are combined into a list.
- **Zero dependencies** — Uses only the Python standard library.

## Installation

```bash
pip install json-parser
```

Or install from source:

```bash
git clone https://github.com/diverdale/json_parser.git
cd json_parser
pip install .
```

## Quick Start

```python
import json
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
            "city": "Springfield",
            "zip_code": "62704"
        },
        "birthday": "1984-05-23"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "full_name": "Jane Smith",
        "address": {
            "street": "742 Evergreen Terrace",
            "city": "Springfield",
            "zip_code": "62701"
        },
        "birthday": "1990-11-12"
    }
]

keys = ["first_name", "last_name", "birthday"]

result = JsonParser(json_data, keys).get_data()
print(json.dumps(result, indent=4))
```

**Output:**

```json
[
    {
        "first_name": "John",
        "last_name": "Doe",
        "birthday": "1984-05-23"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "birthday": "1990-11-12"
    }
]
```

## Wildcard Matching

Use glob-style patterns to match keys dynamically. For example, `address*` matches `address`, `address1`, and `address2`:

```python
keys = ["first_name", "address*", "birthday"]
result = JsonParser(json_data, keys).get_data()
```

**Output:**

```json
[
    {
        "first_name": "John",
        "address1": {
            "street": "1208 Elm Street",
            "city": "Springfield",
            "zip_code": "62704"
        },
        "address2": {
            "street": "4965 Harvest Rd",
            "city": "Springfield",
            "zip_code": "62704"
        },
        "birthday": "1984-05-23"
    },
    {
        "first_name": "Jane",
        "address": {
            "street": "742 Evergreen Terrace",
            "city": "Springfield",
            "zip_code": "62701"
        },
        "birthday": "1990-11-12"
    }
]
```

## Duplicate Key Merging

When the same key is found at multiple nesting levels within a single record, the values are automatically combined into a list:

```python
keys = ["first_name", "street", "birthday"]
result = JsonParser(json_data, keys).get_data()
```

**Output:**

```json
[
    {
        "first_name": "John",
        "street": [
            "1208 Elm Street",
            "4965 Harvest Rd"
        ],
        "birthday": "1984-05-23"
    },
    {
        "first_name": "Jane",
        "street": "742 Evergreen Terrace",
        "birthday": "1990-11-12"
    }
]
```

## API Reference

### `JsonParser(obj, args)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `obj` | `list[dict]` | A list of JSON objects (dicts) to search. |
| `args` | `list[str]` | Key names or glob patterns to extract. |

Raises `JsonParserException` if `obj` or `args` is empty.

#### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `get_data()` | `list[dict]` | Extracts and returns matching key-value pairs from each record. |
| `get_json()` | `list[dict]` | Returns the original JSON input. |
| `get_args()` | `list[str]` | Returns the list of keys/patterns. |

## Running Tests

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.
