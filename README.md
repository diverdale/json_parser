[![PyPI version](https://img.shields.io/pypi/v/json-key-parser.svg)](https://pypi.org/project/json-key-parser/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](/LICENSE)
[![PyPI Downloads](https://pypistats.com/api/badges/json-key-parser)](https://pypistats.com/packages/json-key-parser)

# json-key-parser

You know the pattern. You get a response back from an API and you need three fields buried
inside it. So you write `response['data'][0]['user']['address']['city']`, wrap it in a
try/except because some records have the key and some don't, repeat for the next field, and
suddenly you have twenty lines of boilerplate for what should be a one-liner.
`json-key-parser` lets you declare the keys you want and hands them back — no traversal
code, no try/excepts, no nested loops.

## Quick Start

```python
from json_parser import JsonParser

data = [{"first_name": "Alice", "last_name": "Smith", "birthday": "1990-04-15",
         "address": {"street": "12 Oak Ave", "city": "Portland", "zip": "97201"}},
        {"first_name": "Bob", "last_name": "Jones", "birthday": "1985-09-30",
         "address": {"street": "88 Pine St", "city": "Seattle", "zip": "98101"}}]

result = JsonParser(data, ["first_name", "last_name", "birthday"]).get_data()
```

**Output:**

```json
[
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "birthday": "1990-04-15"
    },
    {
        "first_name": "Bob",
        "last_name": "Jones",
        "birthday": "1985-09-30"
    }
]
```

## Why json-key-parser?

- **Declare keys, skip the traversal** — one call replaces nested loops across every record
- **Wildcard patterns** — `address*` matches `address`, `address1`, `address2`, and any other variation
- **Duplicate values merged automatically** — no deduplication code needed when a key appears at multiple levels
- **Works at any nesting depth** — one level or ten, it finds the keys you asked for
- **Zero dependencies** — pure Python stdlib, nothing to pin or audit

## Wildcard Matching

Using the same data from above, `address*` matches any key that starts with `address`:

```python
result = JsonParser(data, ["address*"]).get_data()
```

**Output:**

```json
[
    {
        "address": {
            "street": "12 Oak Ave",
            "city": "Portland",
            "zip": "97201"
        }
    },
    {
        "address": {
            "street": "88 Pine St",
            "city": "Seattle",
            "zip": "98101"
        }
    }
]
```

This is especially useful when records are inconsistently structured — one record might have
`address`, another `address1` and `address2`. The pattern catches all of them without
needing to know which variant each record uses.

## Duplicate Key Merging

When the same key appears at more than one nesting level inside a single record, the values
are automatically combined into a list. No deduplication code required.

```python
contacts = [
    {
        "first_name": "Alice",
        "address1": {"street": "12 Oak Ave", "city": "Portland"},
        "address2": {"street": "99 River Rd", "city": "Portland"}
    },
    {
        "first_name": "Bob",
        "address": {"street": "88 Pine St", "city": "Seattle"}
    }
]

result = JsonParser(contacts, ["first_name", "street"]).get_data()
```

**Output:**

```json
[
    {
        "first_name": "Alice",
        "street": [
            "12 Oak Ave",
            "99 River Rd"
        ]
    },
    {
        "first_name": "Bob",
        "street": "88 Pine St"
    }
]
```

Alice has two addresses, so `street` becomes a list of both values. Bob has one address, so
`street` stays a plain string. The shape matches the data — you don't have to handle it
yourself.

## Installation

```bash
pip install json-key-parser
```

## License

MIT. See the [LICENSE](/LICENSE) file for details.
