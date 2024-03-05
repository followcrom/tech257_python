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

print("\n-------------------------------------------")
y = json.dumps(x)
print(y)
print(type(y))

print("\n-------------------------------------------")
with open("output.json", "w") as file:
    json.dump(x, file)
    file.close()

print("\n-------------------------------------------")
with open("output.json", "r") as file_2:
    contents = file_2.read()
    print(contents)

print("\n-------------------------------------------")
print(type(contents))

print("\n-------------------------------------------")
with open("output.json", "r") as file_3:
    contents_2 = json.load(file_3)
    print(contents_2)

print(type(contents_2))

print("\n-------------------------------------------")
contents_3 = json.loads(contents)
print(contents_3)

print(type(contents_3))
