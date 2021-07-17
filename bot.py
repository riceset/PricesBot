import os
import re
import json
import tweepy
from sys import exit
from crypto import lookup
from nomics import Nomics
from time import sleep

""" Sets up the Twitter API """

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Retrieve the last seen ID
def retrieve_LSID(FILE):
    with open(FILE) as file:
        LSID = int(file.read().strip())
    return LSID


# Stores the last seen ID
def store_LSID(LSID, FILE):
    with open(FILE, 'w') as file:
        file.write(str(LSID))


# Converting cryptocurrencies JSON into a dictionary
CRYPTOCURRENCIES_JSON = f"{os.getcwd()}/cryptocurrencies.json"
CRYPTOCURRENCIES = {}

with open(CRYPTOCURRENCIES_JSON) as JSON:
    CRYPTOCURRENCIES = json.load(JSON)

# A list of all the keys on the dictionary
symbols = [symbol for symbol in CRYPTOCURRENCIES.keys()]

def reply():

    print('Waiting...')

    LSID = retrieve_LSID('ID.txt')
    mentions = api.mentions_timeline(LSID)

    for mention in reversed(mentions):

        # prints the mention
        print(f"{mention.id} - {mention.text}")

        # looks for hashtags
        pattern = re.compile(r"#(\w+)")
        hashtags = pattern.findall(mention.text)

        hashtags = [hashtag.upper() for hashtag in hashtags]

        # stores the tweet ID (used to ignore the current tweet on the next call)
        LSID = mention.id
        store_LSID(LSID, 'ID.txt')

        # creates a list with valid currencies (mentioned on the hashtags)
        currencies = list(set(hashtags).intersection(symbols))

        # prints all the valid currencies - count
        print(f'{currencies}\n"{len(currencies)}"')

        prices = []

        # gets the price of each currency
        for currency in currencies:
            price = lookup(currency)
            prices.append(price)
            sleep(1)

        username = mention.user.screen_name
        reply_tweet = '@' + username + '\n'

        # prepares the string to be tweeted
        for currency, price in zip(currencies, prices):
            temp_string = '#' + currency + ': ' + price + '\n'
            reply_tweet += temp_string

        print(f"reply:\n{reply_tweet}")

        # tweets back
        try:
            api.update_status(reply_tweet, mention.id)

        except tweepy.error.TweepError:
            # If the response cannot fit 280 characters.
            api.update_status('@' + username + "Error: The response is too long. Please try again.", mention.id)


while True:
    reply()
    sleep(2)
