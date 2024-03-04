import os, sys, subprocess, json

print("\n-------------------------------------------")
# list a dir on Windows.
print(os.listdir("/mnt/c/Users/teedc"))

# can change to that dir, but be cautious with this.
# os.chdir("/mnt/c/Users/teedc")
# print("Current Directory:", os.getcwd())

print("\n-------------------------------------------")
# This line gets the directory of this file.
this_dir = os.path.dirname(__file__)
print("This Directory:", this_dir)

print("\n-------------------------------------------")
# This line gets the current working directory of the process running the script: the directory from which the script was invoked (check the terminal).
current_dir = os.getcwd()
print("Current Directory:", current_dir)

print("\n-------------------------------------------")

print("Directory List:", os.listdir(current_dir))

print("\n-------------------------------------------")

command = ["python", "../scripting/hello_world.py"]
# Run the command and display the output.
subprocess.run(command)

print("\n-------------------------------------------")
# Run the command and capture the verbose output. This code does not display the output until we print it.
result = subprocess.run(command, capture_output=True, text=True)

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

