import json

class JsonParserException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class JsonParser:
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
        data = []
        for x in self.json_obj:
            for key in self.args:
                data.append(key + ": " + str(x.get(key)))
        data_json = [{}]
        for item in data:
            key, val = item.split(":", 1)
            if key in data_json[-1]:
                data_json.append({})
            data_json[-1][key] = val
        return data_json