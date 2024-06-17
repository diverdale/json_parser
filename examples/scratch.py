import json

def find_key_value_pairs(nested_list, keys_to_search):
    def search_dict(dct, keys_to_search):
        found = {}
        for key, value in dct.items():
            if key in keys_to_search:
                found[key] = value
            if isinstance(value, dict):
                found.update(search_dict(value, keys_to_search))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        found.update(search_dict(item, keys_to_search))
        return found

    result = []
    for item in nested_list:
        if isinstance(item, dict):
            result.append(search_dict(item, keys_to_search))
    return result

# Example usage:
with open("people.json", "r") as f:
    nested_list_of_dicts = json.load(f)

keys = ['full_name', 'city']
matched_key_value_pairs = find_key_value_pairs(nested_list_of_dicts, keys)

print(matched_key_value_pairs)