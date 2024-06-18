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

keys = ['first_name', 'street', 'birthday']

data = JsonParser(json_data, keys)
result = data.get_data()
print(json.dumps(result, indent=4))