import os, json

path_to_json = "example.json"
json = json.loads(open(path_to_json).read())

for key in json:
    value = json[key]
    print(f"{value} is the value for this key: {key}.")