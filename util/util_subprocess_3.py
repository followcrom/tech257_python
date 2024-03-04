import os, subprocess

print("\n-------------------------------------------")
# Define a Linux command or script you want to run
command = ['echo', 'Hello from Ubuntu!']

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

print("\n-------------------------------------------")
print("Full output:", result)

print("\n-------------------------------------------")
# Print the standard output of the command
print("stdout", result.stdout)

print("\n-------------------------------------------")
print("args", result.args)

print("\n-------------------------------------------")
# Print the standard error if any. stderr is a string, so we can check if it is empty.
if result.stderr != "":
    print("Errors:", result.stderr)
else:
    print("No Errors")

print("\n-------------------------------------------")
# Check if the command was executed successfully
if result.returncode == 0:
    print("Script executed successfully")
else:
    print("Error in script execution")

print("\n-------------------------------------------")
# Define a series of commands separated by semicolons (;)
commands = ['sh', '../scripting/os_module/script.sh']

# Run the commands using the shell
result = subprocess.run(commands, capture_output=True, text=True)

# Print the command output (stdout)
print(result.stdout)

print("\n-------------------------------------------")
# script_dir = os.path.dirname(__file__)
# print(script_dir)
#
# script_absolute_path = os.path.join(script_dir + "/script.sh")
# commands = ["sh", script_absolute_path]

