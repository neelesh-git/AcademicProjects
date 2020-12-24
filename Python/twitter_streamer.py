import json
import sys
sys.path.append('/Users/neeleshbhajantri/Desktop/Python')
import tweepy 

import twitter_credentials
import datetime, time


auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def timeline_tweets(api, username):
    page = 1
    deadline = False
    while True:
        tweets = api.user_timeline(username, page = page)
        
        for tweet in tweets:
            if (datetime.datetime.now() - tweet.created_at).days < 7:
                print(tweet.text.encode("utf-8"))
            else:
                deadend = True
                return
            if not deadend:
                page+1
                time.sleep(500)
                
timeline_tweets(api, 'donald trump')