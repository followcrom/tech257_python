# age = input("What is your age? ")
#
# print(f" Your age is {age}")
#

# SET VARIABLE user_prompt TO TRUE
user_prompt = True

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt is True:
    age = input("What is your age? ")
    if (age.isdigit()) and (int(age) < 118):
        user_prompt = False
        break
    else:
        print("Please try again. Use reasonable digits.")

print(f"Your age is {age}")