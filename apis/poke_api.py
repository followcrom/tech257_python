import requests
import random

ply_1 = random.randint(0,500)
ply_2 = random.randint(0,500)

# Get the pokemon's data from the API
ply_1_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ply_1)
ply_2_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ply_2)

ply_1_response = requests.get(ply_1_url)
ply_2_response = requests.get(ply_2_url)

if ply_1_response.status_code == 200:
    data = ply_1_response.json()
    stats = data['stats']
    ply_1_name = data['name']
    ply_1_weight = data['weight']
    for stat in stats:
        if stat['stat']['name'] == 'attack':
            ply_1_attack = stat['base_stat']
        elif stat['stat']['name'] == 'defense':
            ply_1_defense = stat['base_stat']


if ply_2_response.status_code == 200:
    data = ply_2_response.json()
    stats = data['stats']
    ply_2_name = data['name']
    ply_2_weight = data['weight']
    for stat in stats:
        if stat['stat']['name'] == 'attack':
            ply_2_attack = stat['base_stat']
        elif stat['stat']['name'] == 'defense':
            ply_2_defense = stat['base_stat']


ply_1_count = 0
ply_2_count = 0

print(f"Here we are for the heavyweight title bout. It's {ply_1_name.title()} vs. {ply_2_name.title()}.")
print(f"Round 1: {ply_1_name.title()} attack {ply_2_name.title()}. Fight!")

print(f"{ply_1_name.title()}'s attack: {ply_1_attack}.")
print(f"{ply_2_name.title()}'s defense: {ply_2_defense}")

if ply_1_attack > ply_2_defense:
    print(f"{ply_1_name.title()} wins Round 1!")
    ply_1_count += 1
else:
    print(f"{ply_2_name.title()} wins Round 1!")
    ply_2_count += 1

print(f"Round 2: {ply_2_name.title()} attack {ply_1_name.title()}. Fight!")

print(f"Name: {ply_2_name.title()}'s attack: {ply_2_attack}.")
print(f"Name: {ply_1_name.title()}'s defense: {ply_1_defense}")

if ply_1_defense > ply_2_attack:
    print(f"{ply_1_name.title()} wins Round 2!")
    ply_1_count += 1
else:
    print(f"{ply_2_name.title()} wins Round 2!")
    ply_2_count += 1


print("The decision is:")
if ply_1_count > ply_1_count:
    print(f"{ply_1_name.title()} wins.")
elif ply_1_count == ply_1_count:
    print("It's a draw. Tie-breaker time. It's going to come down to who is heavier...")
    print(f"{ply_2_name.title()}'s weight: {ply_2_weight}.")
    print(f"{ply_1_name.title()}'s weight: {ply_1_weight}")
    if ply_1_weight > ply_2_weight:
        print(f"{ply_1_name.title()} wins by being heavier!")
    else:
        print(f"{ply_2_name.title()} wins by being heavier!")
else:
    print(f"{ply_2_name.title()} wins.")