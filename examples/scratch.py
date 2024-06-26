import json
from json_parser import JsonParser

with open("bakery.json", "r") as f:
    json_data = json.load(f)

keys = ['name', 'batter', 'topping']

data = JsonParser(json_data, keys)
result = data.get_data()
print(json.dumps(result, indent=4))