"""
Create a frozen set named frozen_set containing elements "hello", "world".
Try to add "!" to frozen_set. What happens?
"""

frozen_set = frozenset(["hello", "world"])

# frozen_set.add("!")
# AttributeError: 'frozenset' object has no attribute 'add'

print(frozen_set)

print("\n-------------------------------------------")
# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = set(["let's", "learn"])
print(normal_set)

print("\n-------------------------------------------")
# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(frozen_set)


print("\n-------------------------------------------")
# Print normal_set.
print(normal_set)

print("\n-------------------------------------------")
# Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.

print("\n-------------------------------------------")
# What makes a frozen set different to a normal set? Explain.