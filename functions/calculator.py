def add(num_1, num_2):
    return num_1 + num_2

print("Add:", add(4,5))

def subtract(num_1, num_2):
    return num_1 - num_2

print("Subtract:", subtract(4,5))

def multiply(num_1, num_2):
    return num_1 * num_2

print("Multiply:", multiply(4,5))

def divide(num_1, num_2):
    return num_1 / num_2

print("Divide:", divide(4,5))

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

