import json
import os
import sys
import yaml

# Checking if there is a file passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python json2yaml.py <source_json_file.json> <target_yaml_file.yaml>")

# print(source_content)

# Process the conversion - Use yaml library
# y_file_1 = yaml.dump(source_content)
# print(y_file_1)

# print(yaml.dump(json.load(open(sys.argv[1])), default_flow_style=False))

# Save the conversion in a new file (output.yaml)

yml_dir = "yml_files"
parent_dir ="/home/followcrom/projects/pycharm-projects/github/tech257_python/scripting/json"

path = os.path.join(parent_dir, yml_dir)
# print(path)
# os.mkdir(path)

filename = sys.argv[2]
filepath = os.path.join(path, filename)

with open(os.path.join(filepath), "w") as file_1:
    file_1.write(yaml.dump(source_content))

print(f"File {filename} created.")
