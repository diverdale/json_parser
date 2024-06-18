import json
from json_parser import JsonParser

with open('people.json', 'r') as f:
    json_data = json.load(f)
test_data = []

keys = ['*name', 'birthday', 'address*']
data = JsonParser(json_data, keys)

result = data.get_data()
print(json.dumps(result, indent=4))
