import requests, json

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6DN", "BH22 9UL"]})

headers = {"Content-Type": "application/json"}

url = "https://api.postcodes.io/postcodes/"

response = requests.post(url, data=json_body, headers=headers)

returned = response.json()
print(type(returned))
results = returned["result"]

for result in results:
    country = result["result"]["country"]
    parliamentary_constituency = result["result"]["parliamentary_constituency"]
    print(parliamentary_constituency)
    # print(country)
