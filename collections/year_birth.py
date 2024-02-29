age_int = int(input("How old are you? "))
name_str = input("What is your name? ")

# print(f"OMG {name_str}, you are {age_int} years old so you were born in {2024 - age_int}.")


def calculate_hours(age):
    hours = age * 365 * 24
    return hours

# hours = calculate_hours(age_int)

# print(f"OMG {name_str}, you have been alive for {hours:.2f} hours.")


"""
If time
figure out a way to account for if the persons bithday has already happened this year or not
go look into the library 'time' to be more accurate with the hours lived
show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate
"""
from datetime import datetime

# Get today's date
today = datetime.now().date()

# Prompt the user to enter a date
dob = input("When we you born? (YYYY-MM-DD): ")

# Convert the user input to a datetime object
dob = datetime.strptime(dob, '%Y-%m-%d').date()

# Compare the user-entered date with today's date
if dob > today:
    print(f"OMG {name_str}, you are {age_int} years old so you were born in {2024 - age_int}.")
else:
    print(f"OMG {name_str}, you are {age_int} years old so you were born in {2023 - age_int}.")




"""
Acceptance Criteria
program defines the variable age_int and name_str
program prints the string "OMG , you are years old so you were born in "
"""

