import sys, os
import json
import pytest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from json_parser import JsonParser, JsonParserException, parse

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


# --- API-01: Raw JSON string input ---

def test_string_input_array():
    """JsonParser accepts a JSON array string and returns correct results."""
    result = JsonParser(json.dumps([{"name": "Alice"}]), ["name"]).get_data()
    assert result == [{"name": "Alice"}]

def test_string_input_dict():
    """JsonParser accepts a JSON object string (single dict) and wraps it."""
    result = JsonParser(json.dumps({"name": "Bob"}), ["name"]).get_data()
    assert result == [{"name": "Bob"}]

def test_string_input_malformed():
    """Malformed JSON string raises JsonParserException, not raw JSONDecodeError."""
    with pytest.raises(JsonParserException):
        JsonParser("bad json", ["name"])


# --- API-02: Single dict input ---

def test_single_dict_input():
    """JsonParser accepts a bare dict and returns a one-element list."""
    result = JsonParser({"name": "Alice", "age": 30}, ["name"]).get_data()
    assert result == [{"name": "Alice"}]

def test_single_dict_nested():
    """JsonParser accepts a dict with nested keys and extracts them correctly."""
    result = JsonParser({"nested": {"city": "Portland"}}, ["city"]).get_data()
    assert result == [{"city": "Portland"}]


# --- API-03: Module-level parse() function ---

def test_parse_function_list():
    """parse() with a list-of-dicts returns correct results."""
    result = parse([{"name": "Alice"}], ["name"])
    assert result == [{"name": "Alice"}]

def test_parse_function_dict():
    """parse() with a single dict returns a one-element list."""
    result = parse({"name": "Alice"}, ["name"])
    assert result == [{"name": "Alice"}]

def test_parse_function_string():
    """parse() with a JSON string returns correct results."""
    result = parse(json.dumps([{"name": "Alice"}]), ["name"])
    assert result == [{"name": "Alice"}]
