"""
Use your code from the "Task: Get name, age and DOB details from a user".
name = "Lassie"
years = 7
height_cm = 60.2

# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."
"""

"""
print(f"{name} is {years} old and {height_cm} cm tall.")


Ask the user for their height in cm and save it to the variable height
Save height as a float in the list, and print the height from the list.
"""

name = input("What's your name? ")
age = int(input("How old are you? "))
dob = int(input("When were you born? "))
print(f"{name} is {age} old and you was born on {dob}.")

print("\n-------------------------------------------")
"""
Mix the name, age and DOB into one list user_details_list
Print the user's name, age and DOB from the list
"""
user_details_list = [name, age, dob]
print("Name:", user_details_list[0])
print("Age:", user_details_list[1])
print("D.O.B:", user_details_list[2])

print("\n-------------------------------------------")
# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
if isinstance(age, int):
    print(f"Age var is an integer.")
else:
    print(f"Age var is not an integer.")

print("\n-------------------------------------------")
"""
Ask the user for their height in cm and save it to the variable height
Save height as a float in the list, and print the height from the list.
"""
height = float(input("How tall are you? "))
user_details_list.append(height)
print("Height:", user_details_list[-1])