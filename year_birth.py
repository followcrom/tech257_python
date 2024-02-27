"""First part
define the variables age_int and name_str (set dummy/default/initial values)
make a calculation for the year in which the person was born
print out "OMG , you are years old so you were born in " with the correct values
"""

age_int = 50
name_str = "Jones"

print(f"OMG {name_str}, you are {age_int} years old so you were born in {2024 - age_int}.")

"""
Second Part
prompt the user for inputs and assign the variable age_int and name_str
remove the initial values set
"""

age_int = int(input("How old are you? "))
name_str = input("What is your name? ")

print(f"OMG {name_str}, you are {age_int} years old so you were born in {2024 - age_int}.")

"""
Third Part
calculate and print out the total number of hours this person has lived
"""
def calculate_hours(age):
    hours = age * 365 * 24
    return hours

hours = calculate_hours(age_int)

print(f"OMG {name_str}, you have been alive for {hours:.2f} hours.")


"""
If time
figure out a way to account for if the persons bithday has already happened this year or not
go look into the library 'time' to be more accurate with the hours lived
show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate
"""
from datetime import datetime

# Get today's date
today = datetime.today().date()

print(f"Today's date is: {today}")

# Prompt user for their date of birth in the format YYYY-MM-DD
dob_str = input("What is your date of birth (YYYY-MM-DD)? ")

# Convert the input string to a datetime object
dob = datetime.strptime(dob_str, "%Y-%m-%d")
# Assuming 'dob' is a datetime object
dob_edit = dob.strftime("%m-%d")
print(f"The month and day of your date of birth are: {dob_edit}")

today_edit = today.strftime("%m-%d")
print(f"The month and day for today are: {today_edit}")

print(f"OMG {name_str}, you are {age_int} years old so you were born in {2024 - age_int}.")

"""
Acceptance Criteria
program defines the variable age_int and name_str
program prints the string "OMG , you are years old so you were born in "
"""

