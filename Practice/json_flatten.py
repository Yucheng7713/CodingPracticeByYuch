class JSONParser:
    def jsonFlatten(self, json):
        new_json = dict()
        for key, object in json.items():
            if type(object) == dict:
                # Recursively parse the dict until we get a pure flatten json
                nested_flatten_json = self.jsonFlatten(object)
                for sub_key, sub_object in nested_flatten_json.items():
                    new_json[key + '.' + sub_key] = sub_object
            else:
                new_json[key] = object
        return new_json

    # Use without recursion
    def jsonFlatten_II(self, json):
        new_json = dict()
        stack = [json]
        key_stack = []
        while stack:
            d = stack.pop()
            for k, v in d.items():
                if type(v) == int:
                    if key_stack:
                        j_key = ".".join(key_stack + [k])
                    else:
                        j_key = k
                    new_json[j_key] = v
                else:
                    stack.append(v)
                    key_stack.append(k)

        return new_json


d_json = dict()
d_json['a'] = 5
d_json['b'] = 6
d_json['c'] = dict()
d_json['c']['f'] = 9
d_json['c']['g'] = dict()
d_json['c']['g']['m'] = 17
d_json['c']['g']['n'] = 3

parser = JSONParser()
print(parser.jsonFlatten_II(d_json))