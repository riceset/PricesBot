import os
import tweepy
from nomics import Nomics

""" Defines a function to lookup a cryptocurrency via its symbol """

def lookup(symbol):
    # Gets the API Key from an environment variable
    api_key = os.environ.get("CRYPTO_KEY")

    # Gets info about the currency in JSON format
    try:
        info = Nomics(api_key).Currencies.get_currencies(ids = symbol.upper())

    # Returns some relevant information
        return {
            "name": info[0]["name"],
            "price": info[0]["price"],
            "symbol": info[0]["symbol"],
            "logo": info[0]["logo_url"]
        }

    except IndexError:
        return None


""" Sets up the Twitter API """

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Retrieve last seen ID
def retrieve_LSID(FILE):
    with open(FILE, 'r') as file:
        LSID = int(file.read().strip())
    return LSID

# Stores last seen ID
def store_LSID(LSID, FILE):
    with open(FILE, 'w') as file:
        file.write(str(LSID))
