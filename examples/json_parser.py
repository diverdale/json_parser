# Dale Wright

# Parse JSON objects by key name

class JsonParserException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class JsonParser:
    """
        The JsonParser class.

        Methods:

        __init__(self, obj, args)
            returns the JsonParser object

        get_args(self):
            returns the arguments

        get_json(self):
            returns the JSON object

        get_data(self):
            returns the parsed JSON data
    """
    
    def __init__(self, obj, args):

        if not obj:
            raise JsonParserException(
                msg='JSON object must be present'
            )
        if not args:
            raise JsonParserException(
                msg='No keys present to parse'
            )

        self.json_obj = obj
        self.args = args

    def get_args(self):
        return(self.args)
    
    def get_json(self):
        return(self.json_obj)

    
    def get_data(self):
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
        for item in self.json_obj:
            if isinstance(item, dict):
                result.append(search_dict(item, self.args))
        return result