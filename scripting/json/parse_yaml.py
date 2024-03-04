import os, json, sys
import yaml

# parent_dir = os.path.dirname(__file__)
# print(parent_dir)

print(sys.argv)

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file)
        file.close()
        print("YAML is valid")
    elif yaml.YAMLError:
        print("Caught an error")
    else:
        print(sys.argv[1] + "not found")
else:
    print("No arguments given")


# try:
#     # Attempt to load the YAML file
#     with open(file_path, 'r') as file:
#         data = yaml.safe_load(file)
# except yaml.YAMLError as exc:
#     # Catch YAML parsing errors
#     if hasattr(exc, 'problem_mark'):
#         mark = exc.problem_mark
#         # Extract the line and column where the error occurred
#         print(f"Error in {file_path}:")
#         print(f"Error position: Line {mark.line + 1}, Column {mark.column + 1}")
#         if hasattr(exc, 'context_mark') and exc.context_mark:
#             context_mark = exc.context_mark
#             print(f"Context position: Line {context_mark.line + 1}, Column {context_mark.column + 1}")
#         if hasattr(exc, 'problem'):
#             print(f"Problem: {exc.problem}")
#         if hasattr(exc, 'context'):
#             print(f"Context: {exc.context}")
# else:
#     # YAML file is valid
#     print("YAML file is valid.")