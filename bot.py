import os
import re
import json
import tweepy
from sys import exit
from crypto import lookup
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

        print(f"{mention.id} - {mention.text}")

        pattern = re.compile(r"#(\w+)")
        hashtags = pattern.findall(mention.text)

        hashtags = [hashtag.upper() for hashtag in hashtags]

        LSID = mention.id
        store_LSID(LSID, 'ID.txt')

        currencies_list = list(set(hashtags).intersection(symbols))
        currencies_dict = dict.fromkeys(currencies_list, None)

        for currency in currencies_dict:
             print(lookup(currency))

        # username = mention.user.screen_name
        # reply_tweet = f"@{username} {selected_symbol}"

        # print(reply_tweet)

            # api.update_status(reply_tweet, mention.id)


while True:
    reply()
    sleep(2)
