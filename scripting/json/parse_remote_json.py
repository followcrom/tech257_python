import urllib.request
import json, os, sys

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    for key in data:
        value = data[key]
        print(f"{value} is the value for this key: {key}.")

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid")
    else:
        print(sys.argv[1] + "not found")
else:
    print("No arguments given")

