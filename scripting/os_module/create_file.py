import os

direct = "this_dir"

parent_dir ="/home/followcrom/projects/pycharm-projects/github/tech257_python/scripting/"

path = os.path.join(parent_dir, direct)
print(path)

filename = "file2.txt"
filepath = os.path.join(path, filename)

with open(os.path.join(filepath), "w") as file10:
    toFile = "Contents of the file are here"
    file10.write(toFile)

print(f"File {filename} created.")
#
# with open(os.path.join(path, filename), "w") as file12:
#     contents = "Contents, contents"
#     file12.write(contents)


