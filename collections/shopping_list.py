shopping_lst = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_lst)

print("-------------------------------------------\n")
print(type(shopping_lst))

print("-------------------------------------------\n")
print(shopping_lst[0])

print("-------------------------------------------\n")
print(shopping_lst[-1])

print("-------------------------------------------\n")
shopping_lst[1] = "rice"
print(shopping_lst[1])

print("-------------------------------------------\n")
shopping_lst.append("carrots")

print(len(shopping_lst))

print("-------------------------------------------\n")
new_lst = ["toffee", "coffee"]
shopping_lst = shopping_lst + new_lst
print(shopping_lst)

print("-------------------------------------------\n")
shopping_lst.remove("bananas")
print(shopping_lst)

print("-------------------------------------------\n")
shopping_lst.pop(-1)
print(shopping_lst)