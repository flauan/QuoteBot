# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "AEfaWeBRYtY24o4REyYYa8G0x"
consumer_secret = "gfdjTTemHgtlU7XCuMeRWFaCiFixCfq4cTtH9G4SImepWSVjUv"
access_token = "907746599673180162-qVPHoJjn9RVwewe3qjERynchQCmFMtO"
access_token_secret = "p9QeZKmg7qr8JoOhbu6qYUcrSdzzJgUGlR58WuK4xRRUk"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

happy_quotes = [
    "HerokuTest: For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "HerokuTest: Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "HerokuTest: Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "HerokuTest: Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "HerokuTest: Happiness is a warm puppy. - Charles M. Schulz",
    "HerokuTest: The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "HerokuTest: Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create a function that tweets
def TweetOut(tweet_stat,ctr):

    api.update_status(str(ctr)+" "+tweet_stat)

ctr=1
for x in happy_quotes:
    TweetOut(x,ctr)
    time.sleep(3)
    ctr+=1
