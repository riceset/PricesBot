from helpers import lookup, api, retrieve_LSID, store_LSID

LSID = retrieve_LSID('ID.txt')
mentions = reversed(api.mentions_timeline(LSID))

for mention in mentions:

    print(f"{mention.id} - {mention.text}")

    LSID = mention.id
    store_LSID(LSID, 'ID.txt')

    if "#helloworld" in mention.text.lower():
        print("Found #HelloWorld!")
        api.update_status(f'@{mention.user.screen_name} Hello!', mention.id)
