import praw

def post_to_reddit(links, cash_tag, creds):
    reddit = praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        username=creds["username"],
        password=creds["password"],
        user_agent="cashfunnel/0.1"
    )

    comments = [
        f"Got ghosted? I used this AI revenge script from {cash_tag}. Brutal. {links[2]}",
        f"This $17 dopamine reset saved me from scroll addiction. {links[0]}",
        f"My AI girlfriend is smarter than my ex. Real talk. {links[1]}"
    ]

    subs = ["selfimprovement", "BreakUps", "depression", "AskReddit"]

    for sub in subs:
        try:
            submission = reddit.subreddit(sub).hot(limit=10).__next__()
            submission.reply(comments[subs.index(sub) % len(comments)])
            print(f"Posted in r/{sub}")
        except Exception as e:
            print(f"Failed in r/{sub}:", e)
