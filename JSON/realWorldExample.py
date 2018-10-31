import requests
import json

# API for Bitcoin Prices
response = requests.get("https://api.coinmarketcap.com/v2/ticker/?limit=10&sort=id")
response_json = response.json()

print(response_json)

with open("crypto.json", 'w') as publicInfo:
    data = json.dump(response_json, publicInfo)

print(json.dumps(response_json, indent= 2))