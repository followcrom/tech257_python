import os, json
import yaml

parent_dir ="/home/followcrom/projects/pycharm-projects/github/tech257_python/scripting/json/yml_files"

path_to_yaml = "output3.yml"
filepath = os.path.join(parent_dir, path_to_yaml)
print(filepath)

# Open and read the YAML file
with open(filepath, 'r') as yaml_file:
    yaml_content = yaml.safe_load(yaml_file)
    print(yaml_content)

# Convert the Python object to a JSON string
json_content = json.dumps(yaml_content, indent=4)


# Optionally, save the JSON content to a file
# with open('output_file.json', 'w') as json_file:
#     json_file.write(json_content)

# Print the JSON content to the console
print(json_content)

