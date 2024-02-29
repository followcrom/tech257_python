# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hello, welcome to Jack Rabbit Slim's please see our list of starters:")

# Print a list of starters
starters = ["Prawns", "Gambas", "Tiger prawns", "Moth prawns", "Sly prawns"]
print("Starters:", starters)

# Take an input for the user for their starter
while True:  # This creates an infinite loop
    starter_choice = input("And for your starter? ")

    if starter_choice in starters:
        print(f"Great choice! {starter_choice} will be served shortly.")
        break  # Exit the loop once a valid choice is made
    else:
        print("Sorry, that is not on the chef's menu.")

# Print a list of mains
mains = ["Prawn soup", "Gambas soup", "Duck soup", "Lebanese", "Fried duck"]
print("Mains:", mains)

# Take an input for the user for their main course
while True:  # This creates an infinite loop
    main_choice = input("And for your main? ")

    if main_choice in mains:
        print(f"Great choice! {main_choice} will be served shortly.")
        break  # Exit the loop once a valid choice is made
    else:
        print("Sorry, that is not on the chef's menu.")

# Print a list of desserts
desserts = ["Prawn cake", "Gambas cake", "Duck cake", "Lebanese cake", "Fried cake"]
print("Desserts:", desserts)
# Take an input for the user for their dessert
while True:  # This creates an infinite loop
    dessert_choice = input("And for your dessert? ")

    if dessert_choice in desserts:
        print(f"Great choice! {dessert_choice} will be served shortly.")
        break  # Exit the loop once a valid choice is made
    else:
        print("Sorry, that is not on the chef's menu.")

# Print all of the user's choices
print(starter_choice, end='\n')
print(main_choice, end='\n')
print(dessert_choice, end='\n')


# level 2
# Use at least one f-string
print(f"So madam, you'll be having the {starter_choice}, followed by the {main_choice}, and to finish the {dessert_choice}.")

# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
customer_order_list = [starter_choice, main_choice, dessert_choice]

price_dict = {"Prawns": 5, "Gambas": 4, "Tiger prawns": 6, "Moth prawns": 2, "Sly prawns": 3}
bill = 0


for item in customer_order_list:
    if item in price_dict:
        print(item)
        bill += price_dict[item]
    else:
        bill += 2.5

print(f"Total bill: £{bill}")
# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.