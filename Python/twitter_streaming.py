#!/usr/bin/env python
# encoding: utf-8
import sys
import tweepy #https://github.com/tweepy/tweepy
import json

#Twitter API credentials
consumer_key = "zqGFT00l8zXyvzkDRpgKSRY7K"
consumer_secret = "crKxiKxYAaEI7SyxuCRWjCLYbIxfGBId6xJGLOxeHEtbMUH1tu"
access_key = "2952479108-xS59KQJmyTWqfPU9IRC1gTrLBhN5Mt7bXWIhK2l"
access_secret = "SS4kMCLfea8SdjXN3VFWQoeca5sIdVAI14ris9Q7VCxZR"

#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#method to get a user's last tweets
def get_tweets(username):
	#set count to however many tweets you want
    with open('andersoncooper_hashtags.json', 'w') as f:
        
        number_of_tweets = 10000
        for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
                json.dump(tweet._json, f)  
                f.write("\n")


get_tweets('#andersoncooper')





#if we're running this as a script
'''
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
'''