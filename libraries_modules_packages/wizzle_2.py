
import requests

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content[:1000])