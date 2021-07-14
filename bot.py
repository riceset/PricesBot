from helpers import lookup, api

# tweets = api.home_timeline()
mentions = api.mentions_timeline()

for mention in mentions:
    print(f"{mention.id} - {mention.text}")
