import json

import requests

url = "https://api.postcodes.io/postcodes/rh140be"

response = requests.get(url)

# print(response["result"])

print("Status Code:", response.status_code)

print("Headers:", response.headers)

print("Content:", response.content)

print("JSON Content:", response.json())

json_data = response.json()
print(type(json_data))

print("Content dig:", json_data["result"]["country"])

for key, value in json_data.items():
    print(f"{value} is the value for this key: {key}.")


