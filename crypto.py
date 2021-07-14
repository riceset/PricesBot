import os
from nomics import Nomics

""" Defines a function to lookup a cryptocurrency via its symbol """

def lookup(symbol):
    # Gets the API Key from an environment variable
    api_key = os.environ.get("CRYPTO_KEY")

    # Gets info about the currency in JSON format
    try:
        info = Nomics(api_key).Currencies.get_currencies(ids = symbol.upper())
        return info[0]["price"]

    except IndexError:
        return None
