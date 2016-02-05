# Made By Darragh Browne
# using the guide at http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
import tweepy, time, sys
from tweepy import OAuthHandler


CONSUMER_KEY = 'YourKeyHere'
CONSUMER_SECRET = 'YourKeyHere'
OAUTH_TOKEN = 'YourKeyHere'
OAUTH_TOKEN_SECRET = 'YourKeyHere'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
argfile = str(sys.argv[1])

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()
# time.sleep determines the delay between tweets in seconds , be aware if you tweet too often twitter will kick you out
for line in f:
    api.update_status(status=line)
    time.sleep(240)
