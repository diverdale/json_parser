# Python JSON Paarser Library

[![license]](/LICENSE)

json_parser is a JSON parser library.

In json_parser, you can easily traverse large JSON objects and pick out the information that you need.

## Usage

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

keys = ['first_name', 'city', 'birthday']

data = JsonParser(json_data, keys)
result = data.get_data()
print(json.dumps(result, indent=4))
```

```json
[
    {
        "first_name": "John",
        "city": [
            "Springfield",
            "Springfield"
        ],
        "birthday": "1984-05-23"
    },
    {
        "first_name": "Jane",
        "city": "Springfield",
        "birthday": "1990-11-12"
    }
]
```

## Wildcards
Using the same code but chaning the keys to include wildcards

```python
keys = ['first_name', 'address*', 'birthday']
```
will get anything matching address (address, address1 and address2 in this case)

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

## Duplicate Keys
Duplicate keys will be combined into a sigle json element. 

```python
keys = ['first_name', 'street', 'birthday']
```
Changing keys to include street will return the following:

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





