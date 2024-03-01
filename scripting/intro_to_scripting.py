import os, sys, subprocess, json

# os.mkdir("")

if len(sys.argv) > 1:
    print("Yup")


# Define the command to run the Python script.
# Make sure to use the correct path to the Python interpreter and the script file.
command = ["python", "hello_world.py"]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the standard output of the command
# print("Output:", result)
#
# print("stdout", result.stdout)
#
# print("args", result.args)

# Check if the command was executed successfully
if result.returncode == 0:
    print("Script executed successfully")
else:
    print("Error in script execution")

# Print the standard error if any
# print("Errors:", result.stderr)

x = {
    "name": "john", "age": 30, "city": "London"
}

print(type(x))

y = json.dumps(x)
print(y)