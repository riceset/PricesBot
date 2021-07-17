import re
import tweepy
from time import sleep
from crypto import lookup
from symbols import symbols
from twitter import api, store_LSID, retrieve_LSID


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
        print(f'{currencies}\nCount: "{len(currencies)}"')

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
