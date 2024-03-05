import requests
import random

def get_player_stats(ply_id):
    stats_dict = {}
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ply_id)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        stats = data['stats']
        # print(stats)
        stats_dict["name"] = data['name'].title()
        stats_dict["weight"] = data['weight']
        stats_dict["count"] = 0
        for stat in stats:
            if stat['stat']['name'] == 'attack':
                stats_dict["attack"] = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                stats_dict["defense"] = stat['base_stat']
            elif stat['stat']['name'] == 'special-attack':
                stats_dict["special attack"] = stat['base_stat']
            elif stat['stat']['name'] == 'special-defense':
                stats_dict["special defense"] = stat['base_stat']

    return stats_dict


ply_1 = random.randint(0,500)
ply_2 = random.randint(0,500)

ply_1_stats = get_player_stats(ply_1)
print(ply_1_stats)

ply_2_stats = get_player_stats(ply_2)
print(ply_2_stats)


print(f"Here we are for the poke-weight title bout. It's {ply_1_stats['name']} vs. {ply_2_stats['name']}.")
print(f'Round 1: {ply_1_stats["name"]} attack {ply_2_stats["name"]}. Fight!')

print(f"{ply_1_stats['name']}'s attack: {ply_1_stats['attack']}.")
print(f"{ply_2_stats['name']}'s defense: {ply_2_stats['defense']}")

if ply_1_stats['attack'] > ply_2_stats['defense']:
    print(f"{ply_1_stats['name']} wins Round 1!")
    ply_1_stats["count"] += 1
else:
    print(f"{ply_2_stats['name']} wins Round 1!")
    ply_2_stats["count"] += 1

print(f"Round 2: {ply_2_stats['name']} attack {ply_1_stats['name']}. Fight!")

print(f"Name: {ply_2_stats['name']}'s attack: {ply_2_stats['attack']}.")
print(f"Name: {ply_1_stats['name']}'s defense: {ply_1_stats['defense']}")

if ply_1_stats['defense'] > ply_2_stats['attack']:
    print(f"{ply_1_stats['name']} wins Round 2!")
    ply_1_stats["count"] += 1
else:
    print(f"{ply_2_stats['name']} wins Round 2!")
    ply_2_stats["count"] += 1


print("The decision is:")
if ply_1_stats["count"] > ply_2_stats["count"]:
    print(f"{ply_1_stats['name']} wins.")
elif ply_1_stats["count"] == ply_2_stats["count"]:
    print("It's a draw. Tie-breaker time. It's going to come down to who is heavier...")
    print(f"{ply_2_stats['name']}'s weight: {ply_2_stats['weight']}.")
    print(f"{ply_1_stats['name']}'s weight: {ply_1_stats['weight']}")
    if ply_1_stats['weight'] > ply_2_stats['weight']:
        print(f"{ply_1_stats['name']} wins by being heavier!")
    else:
        print(f"{ply_2_stats['name']} wins by being heavier!")
else:
    print(f"{ply_2_stats['name']} wins.")