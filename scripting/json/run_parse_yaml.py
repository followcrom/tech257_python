import os
import subprocess

this_dir = os.getcwd()
print(this_dir)

output = input("YAML file name: ")
output_pth = os.path.join(this_dir, "yml_files/", output)
print(output_pth)

command = ["python", "parse_yaml.py", output_pth]
subprocess.run(command)
