import tweepy

def post_to_twitter(links, cash_tag, creds):
    auth = tweepy.OAuth1UserHandler(
        creds["api_key"], creds["api_secret"],
        creds["access_token"], creds["access_token_secret"]
    )
    api = tweepy.API(auth)

    tweets = [
        f"I used {cash_tag} to unlock this AI breakup guide. Changed me. {links[2]}",
        f"Dopamine fast with this $17 protocol. Thank me later. {links[0]}",
        f"My GPT girlfriend never ghosts me. Yours? {links[1]}"
    ]

    for tweet in tweets:
        try:
            api.update_status(tweet)
            print("Tweeted:", tweet)
        except Exception as e:
            print("Error:", e)
