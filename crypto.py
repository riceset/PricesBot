import os
from sys import argv
from nomics import Nomics

def lookup(symbol):

    # Gets the API Key from an environment variable
    api_key = os.environ.get("CRYPTO_KEY")

    try:
        nomics = Nomics(api_key)
        info = nomics.Currencies.get_currencies(ids = symbol)

        # gets the price of the cryptocurrency
        info = info[0]
        price = float(info['price'])

        # Formats value as USD ($00.00)
        price = f"${price:,.2f}"

        return price

    except IndexError:
        return None


if len(argv) == 2:
    coin = argv[1].upper()
    price = lookup(coin)
    
    if price is not None:
        print(f"{coin}: {price}")
