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

