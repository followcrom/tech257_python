import os

direct = "this_dir"

parent_dir ="/home/followcrom/projects/pycharm-projects/github/tech257_python/scripting/"

path = os.path.join(parent_dir, direct)
print(path)

os.mkdir(path)
