import os
from sys import argv
from nomics import Nomics

def lookup(symbol):
    # Gets the API Key from an environment variable
    api_key = os.environ.get("CRYPTO_KEY")

    # Gets info about the currency in JSON format
    try:
        nomics = Nomics(api_key)
        info = nomics.Currencies.get_currencies(ids = symbol)
        info = info[0]

        price = '$' + info['price']
        return price

    except IndexError:
        return None

if len(argv) == 2:
    coin = lookup(argv[1])
    if not coin == None:
        for item in coin:
            print(f"{item}: {coin[item]}")
