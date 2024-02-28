"""
First part
Define a dictionary called story1. It should have the following keys:
'start', 'middle' and 'end'
"""


story_1 = {
    'start': 'In a vibrant realm, hidden by the mists of time, a young hero discovers an ancient map.',
    'middle': 'The map leads to a forgotten island where an enchanted crystal lies guarded by a dragon.',
    'end': 'After a cunning battle of wits and bravery, the hero retrieves the crystal, bringing prosperity back to their land.'
}

# Print the entire dictionary
print(story_1)


print("\n-------------------------------------------")
# Print the type of your dictionary
print(type(story_1))

print("\n-------------------------------------------")
# Print only the keys
print(story_1.keys())

print("\n-------------------------------------------")
# Print only the values
for key, value in story_1.items():
    print(value)

print("\n-------------------------------------------")
# Print the individual values using the keys (individually, lots of print commands)
print("Start:", story_1.get("start", None))
print("Middle:", story_1.get("middle", "Mid"))
print("End:", story_1.get("end"))
print("End:", story_1.get("fin", "Fin"))

print("\n-------------------------------------------")
# Now, let's add a new key:value pair:
# 'hero': yourSuperHero"""
story_1["hero"] = "Eldrin Stormseeker"

print("\n-------------------------------------------")
for key, value in story_1.items():
    print("Key:", key, " Value:", value)

print("\n-------------------------------------------")
#
print("\n-------------------------------------------")



# If time
# Improve the program. For example, can you make it a "Choose your own adventure" story?

choice = 3

while choice > 0:
    user_ch1 = int(input("Choose where to start: 1,2,or 3: "))
    if user_ch1 == 1:
        print(story_1["start"])
        choice -= 1
        continue
    elif user_ch1 == 2:
        print(story_1["middle"])
        choice -= 1
        continue
    else:
        print(story_1["end"])
        choice -= 1
        continue

