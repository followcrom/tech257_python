import random

ran_num = random.randint(1,10)
print(ran_num)


import os

print(os.getcwd())

def print_username():
    # username = os.environ.get('USERNAME') # for Windows
    username = os.environ.get('USER')
    print(f"The current user is: {username}")

print(print_username())


def cpu_cores():
    cpu_core = os.cpu_count()
    print(cpu_core)

print("Total CPU Cores:", cpu_cores())

import datetime

print(f"Today's date: {datetime.date.today()}")

import sys
# print("Current path:", sys.path)


# list standard python library
import builtins

for name in dir(builtins):
    if name[0].islower():
        print(name)



