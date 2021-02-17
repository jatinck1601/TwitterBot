import tweepy
import time

CONSUMER_KEY = 'now shown'
CONSUMER_SECRET='not shown'

ACCESS_KEY='hidden'
ACCESS_SECRET='hidden'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

hashtag = '#cancelPTUexams'
tweetnumber = 100

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(1)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(1)

searchBot()
