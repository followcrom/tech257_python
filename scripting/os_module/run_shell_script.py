import os, subprocess

script_dir = os.path.dirname(__file__)
print(script_dir)

script_absolute_path = os.path.join(script_dir + "/script.sh")
commands = ["sh", script_absolute_path]

subprocess.run(commands)
