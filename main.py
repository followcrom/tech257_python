hi = "Hello World!"

# find out if 'hi' is made up of letters only (use one of the strings methods) - print the boolean to the screen
print("--------------------------------------\n")
print(isinstance(hi, str))

print("--------------------------------------\n")
print(hi.isalpha())

# find out if 'hi' is made up only of lowercase letters (use one of the strings methods) - print the boolean to the screen
print("--------------------------------------\n")
print(hi.islower())

# find out if 'hi' is made up only of uppercase letters (use one of the strings methods) - print the boolean to the screen
print("--------------------------------------\n")
print(hi.isupper())

# find out if 'hi' ends with an exclamation mark (use one of the strings methods) - print the boolean to the screen
print("--------------------------------------\n")
print(hi.endswith("!"))
# find out if 'hi' starts with a capital "h" (use one of the strings methods) - print the boolean to the screen

print("--------------------------------------\n")
print(hi.startswith("H"))