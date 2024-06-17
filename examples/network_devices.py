import json
from json_parser import JsonParser

with open('device_list.json', 'r') as f:
    temp_data = json.load(f)
    
json_data = temp_data['response']

keys = ['hostname', 'serialNumber', 'managementIpAddress', 'platformId']
data = JsonParser(json_data, keys)

result = data.get_data()
print(json.dumps(result, indent=4))
