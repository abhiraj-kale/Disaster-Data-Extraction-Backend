from itertools import count
import tweepy
import pandas as pd
import os, firebase

#Twitter Access
auth = tweepy.OAuthHandler( 'H9A5eK2Em8XDPiXC6vSWjPe5R','EEl5hdTFlq3dIf5CEDNDUVCqpiYlbG1vzsT5VdbCwQpnxnC9y1')
auth.set_access_token('1434164272137834501-YSv0SsVqqpIa9JF2Xy8nsCFFDVEawn','WmPx7MnxoF37LO0HfLR5cMsw68662iMVLWbxrfD30Vh6L')
api = tweepy.API(auth,wait_on_rate_limit = True)

def scrape_twitter(disaster, hashtag):
    df = pd.DataFrame(columns=['text', 'source', 'url'])
    msgs = []
    msg =[]
    query = "#".join(hashtag)
    tweets = api.search_tweets(q=query, lang="en", count=10)
    print(tweets)
    for tweet in tweets:
        msg = [tweet.created_at, tweet.text, tweet.user.screen_name, tweet.source, tweet.source_url, tweet.user.location] 
        msg = tuple(msg)
        msgs.append(msg)

    df = pd.DataFrame(msgs)
    for dummy in df.index:
        firebase.push_twitter_data(disaster, str(df[0][dummy]),str(df[1][dummy]),str(df[2][dummy]),str(df[3][dummy]),str(df[4][dummy]),str(df[5][dummy]))
        