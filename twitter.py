import os
import tweepy

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
