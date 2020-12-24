import tweepy
import json
####input your credentials here
consumer_key = "zqGFT00l8zXyvzkDRpgKSRY7K"
consumer_secret = "crKxiKxYAaEI7SyxuCRWjCLYbIxfGBId6xJGLOxeHEtbMUH1tu"
access_key = "2952479108-xS59KQJmyTWqfPU9IRC1gTrLBhN5Mt7bXWIhK2l"
access_secret = "SS4kMCLfea8SdjXN3VFWQoeca5sIdVAI14ris9Q7VCxZR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
with open('myogiadityanath_hashtag.json', 'w') as f:

    for tweet in tweepy.Cursor(api.search,q="#yogiadityanath",count=1000,
                           since="2017-04-03").items():
        print (tweet.created_at, tweet.text)
        json.dump(tweet._json, f)  
        f.write("\n")