customer_order_list = ["Prawns", "Gambas", "Tiger prawns", "Moth prawns", "Sly prawns"]

price_dict = {"Prawns": 5, "Gambas": 4, "Tiger prawns": 6, "Moth prawns": 2, "Sly prawns": 3}
bill = 0


for x in customer_order_list:
    if x in price_dict:
        print(x, price_dict[x])
        bill += price_dict[x]
        print(bill)

print(f"Total bill: £{bill}")

for value in price_dict.values():
    print(value)

print(price_dict.get('Sly prawns'))

price_dict['Messy prawns'] = 4

print(price_dict)

for key, value in price_dict.items():
    print(key, value)

for i in range(1,6):
    price_dict["Prawn Dish " + str(i)] = i

price_dict.pop("Prawn Dish 3")

print(price_dict)

customer_order_list_2 = ["Prawns", "Gambas", "Tiger prawns", "Moth prawns", "Sly prawns", "Prawn Dish 4"]
for item in customer_order_list_2:
    if item in price_dict:
        bill += price_dict[item]

print(bill)
