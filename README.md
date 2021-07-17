# PricesBot

## Quick Introduction
PricesBot is a Twitter bot that when mentioned, analyzes the tweet, and replies with the current price of all the valid cryptocurrencies on the mention's hashtags. It certifies the hashtag contains a valid cryptocurrency and only makes an API call requesting the prices of the cryptocurrencies mentioned, if it's a valid one.

## Understanding
PricesBot contains 4 main files.

### cryptocurrencies.json

A json file from [this repo](https://github.com/crypti/cryptocurrencies) that contains all of the
most popular cryptocurrency symbols. Used to intersect with the cryptocurrencies from the hashtags
the user entered on the mention.

### bot.py

`bot.py` is the main file, you can start the bot by running it.

On the beggining, the Twitter API is set up and `cryptocurrencies.json` is converted to a list.

Then there are 2 functions. One that stores the last seen ID from a particular tweet to a `.txt` file,
the other one that reads this ID. The ID of the last seen tweet is really important when retrieving
all the mentions to remember what was the last tweet that the bot replied (to avoid replying to the same
tweet twice)

Then, there's the `reply()` function, that waits for a tweet it hasn't replied yet, and
if it finds one, it will look for hashtags on the mention, filter all the valid cryptocurrencies from
the hashtags, and request to the Nomics API all the prices of the cryptocurrencies mentioned.
Then, using the Tweepy library, a reply is sent containing all the prices for the cryptocurrencies
requested.

### crypto.py

A file with a `lookup()` function that returns the price of a cryptocurrency based on its symbol.
You can also run this file with `python crypto.py 'CRYPTOCURRENCY'` using argv[1] as the symbol
to lookup. (such as BTC for Bitcoin.)

## Usage

Run the bot with the `python bot.py` command. It will print out `waiting...` until
you tweet a mention to @PricesBot with a hashtag containing a cryptocurrency.

If you do so, PricesBot will send you a mention containing the prices of all the cryptocurrencies
mentioned on the tweet sent. You have to specify the cryptocurrency symbols using a #hashtag.

## Example tweets

Requesting one cryptocurrency:

`@PricesBot #BTC`

Requesting two or more cryptocurrencies:

`@PricesBot #BTC #ETH #DOGE`

Requesting a currency with other hashtags:

`@PricesBot #BTC #Pokemon #ETH #DOGE #BAT #Nintendo #DOT`

Only Bitcoin, Etherium, Dogecoin, Basic Attention Token and Polkadot will be requested to the Nomics API.
Only valid currencies will be sent on the reply.

## Referenced

- [How to make a Twitter bot](https://www.youtube.com/watch?v=W0wWwglE1Vc&t=0s) by CSDojo.

- [Nomics API](https://nomics.com/)

- [Twitter API](https://developer.twitter.com/en)

- [Cryptocurrencies JSON](https://github.com/crypti/cryptocurrencies)

- [Tweepy Library](https://github.com/tweepy/tweepy)

- [Nomics Python](https://github.com/TaylorFacen/nomics-python)

- [Tweepy.org](https://www.tweepy.org/)
