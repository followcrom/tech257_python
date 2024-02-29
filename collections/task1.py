name = "Lassie"
years = 7
height_cm = 60.2

# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."

print(f"{name} is {years} old and {height_cm} cm tall.")



print("--------------------------------------\n")

pi = 3.14159265359

print("Pi to 3 decimal places: {}".format(round(pi,3)))


# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print("Pi to 3 decimal places: {}".format(round(pi,5)))

print("--------------------------------------\n")
score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")

print("--------------------------------------\n")
# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"You scored {score_as_decimal * 100}%")

print(f"You scored {score_as_decimal:.2%}")

print("--------------------------------------\n")
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"You scored {score_as_decimal * 100:.2f}%")

print("--------------------------------------\n")
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
print(f"You scored {score_as_decimal:.0%}")