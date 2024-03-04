import os, json, sys
import yaml

# parent_dir = os.path.dirname(__file__)
# print(parent_dir)

this_dir = os.getcwd()
print(this_dir)

path_to_yaml = "output3.yml"
filepath = os.path.join(this_dir, "yml_files/", path_to_yaml)
print(filepath)

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], 'r') as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            print("YAML:", yaml_content)
            json_content = json.dumps(yaml_content, indent=4)
            print("JSON:", json_content)
            with open('output_file2.json', 'w') as json_file:
                json_file.write(json_content)
    else:
        print(sys.argv[1] + "not found")
else:
    print("No arguments given")

# with open(filepath, 'r') as yaml_file:
#     yaml_content = yaml.safe_load(yaml_file)
#     print(yaml_content)

# Convert the Python object to a JSON string
# json_content = json.dumps(yaml_content, indent=4)
# print(json_content)

# with open('output_file.json', 'w') as json_file:
#     json_file.write(json_content)



