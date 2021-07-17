import json
import os

# Converting cryptocurrencies JSON into a dictionary
CRYPTOCURRENCIES_JSON = f"{os.getcwd()}/cryptocurrencies.json"
CRYPTOCURRENCIES = {}

with open(CRYPTOCURRENCIES_JSON) as JSON:
    CRYPTOCURRENCIES = json.load(JSON)

# A list of all the keys on the dictionary
symbols = [symbol for symbol in CRYPTOCURRENCIES.keys()]
