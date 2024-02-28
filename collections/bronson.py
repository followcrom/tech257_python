list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

print("\n-------------------------------------------")
"""
Loop through the a list Under the starting code, write a for loop to print the double of each number in the list 'list_data'.
It should loop through the numbers in list_data - each item in the list should be called 'num' (for number)
Inside the loop, it should print out the double of each number in the list.
"""
for num in list_data:
    print("Number:", num * 2)


print("\n-------------------------------------------")
"""
Loop through the 'embedded_lists' list
Write another for loop to print the items inside of 'embedded_lists'. Each item in the list should be called 'data'
It should output this to the screen:
[1, 2, 3]
[4, 5, 6]
"""
for data in embedded_lists:
    print(data)


print("\n-------------------------------------------")
"""
Loop through the lists embedded inside a list
We need to access the data within the lists, so now we need an embedded loop.
Create another loop inside of the 'embedded_lists' for loop to list the individual items in the lists.You should end up with this output:
[1, 2, 3]
1
2
3
[4, 5, 6]
4
5
6"""
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)


print("\n-------------------------------------------")
"""
Loop through a dictionary 
rite another for loop to loop through the dictionary 'dict_data'. It should print the keys to the screen like this:
1
2
3
"""

for key, value in dict_data.items():
    print(key)

print("\n-------------------------------------------")
for item in dict_data.keys():
    print(item)

print("\n-------------------------------------------")
"""
Loop through a dictionary and print its values
Write another for loop to loop through the dictionary 'dict_data'.
Use to the dictionary's value() method to print the value for each key in the dictionary.
Output should be:
{'name': 'Bronson', 'money': '$0.05'}
{'name': 'Masha', 'money': '$3.66'}
{'name': 'Roscoe', 'money': '$1.14'}
"""

for value in dict_data.values():
    print(value)


print("\n-------------------------------------------")
"""
Loop to print the values of the dictionary items inside a dictionary
Copy and paste the last for loop as a starting point for this loop.
Generate an embedded for loop (a loop within a loop) to extract and print the values within the dictionary of each item in the dictionary.
Output should be:
Bronson
$0.05
Masha
$3.66
Roscoe
$1.14
"""

for value in dict_data.values():
    print(value['name'], end="\n")
    print(value['money'])


print("\n-------------------------------------------")
for value in dict_data.values():
    for val in value.values():
        print(val)

print("\n-------------------------------------------")
"""
Loop to print specific values of the dictionary items inside a dictionary
Write another for loop to loop through the dictionary 'dict_data' but this time only print out the money values.
Output should be:
$0.05
$3.66
$1.14
"""

for item in dict_data.values():
    print(item['money'])


print("\n-------------------------------------------")
"""
Loop through a list with a nested if statement
Write another loop to loop through the items in 'list_data' and include a nested (indented) if statement inside the loop
so that when it loops it checks the number/item in list:
if the number is less than 3, it prints 'less than 3'
if the number equals 3, it prints 'I found three'
if the number is greater than 3, it prints 'greater than 3'
Output should be:
less than 3
less than 3
I found three
greater than 3
greater than 3
"""

for num in list_data:
    if num < 3:
        print("Less than 3")
    elif num == 3:
        print("3 is the magic number")
    else:
        print("Greater than 3")

print("\n-------------------------------------------")
