"""
What is None in Python?

When is it commonly used?
None is often used as a default value

What's the equivalent in some other programming languages?
Null, nil, NaN

Most important: What happens when you convert None to a boolean?

Write a piece of Python code to prove it
Write a piece of Python code to...
assign x to be None
print whether my variable x is equal to None
"""

# Converting None to a boolean
x = None
boolean_value = bool(x)

print(boolean_value)  # This will print: False



if x == None:
    print("Truth")
else:
    print("Falsehood")

# same id in memory
print(x is None)

