from math_operations import *

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")


user_num_1 = int(input("Input 1st number: "))
user_num_2 = int(input("Input 2nd number: "))

while True:
    operator = input("Select an operator: +,-,*,/ ")
    if operator == '+':
        print(add(user_num_1, user_num_2))
        break
    elif operator == '-':
        print(subtract(user_num_1, user_num_2))
        break
    elif operator == '*':
        print(multiply(user_num_1, user_num_2))
        break
    elif operator == '/':
        print(divide(user_num_1, user_num_2))
        break
    else:
        print("Please select an operator: +,-,*,/ ")
