"""
Task 2.2.2: Accessing Tweets
"""

import os
import json
import tweepy
from tweepy import OAuthHandler


consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def task222():
    # to read our own Twitter home timeline, limiting the number of showed tweets to 1
    for status in tweepy.Cursor(api.home_timeline).items(1):
        print(status.text)

    # metadata of the latest tweet shown on the home timeline
    for status in tweepy.Cursor(api.home_timeline).items(1):
        print(json.dumps(status._json, indent=2))

    # to retrieve a list of the last 10 followed accounts
    for follower in tweepy.Cursor(api.friends).items(10):
        print(follower.name, "\t\t", follower.screen_name)

    # to print a list of tweets previously made by the account
    for tweet in tweepy.Cursor(api.user_timeline).items(8):
        print(tweet.text)


#task222()

"""
Task 2.3: Tweet pre-processing
"""
import re

# retrieves the 10 most recent tweets
# in English of the user's home timeline and tokenizes the content
# in order to allow future language analysis

def task23():
    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""

    regex_str = [
        emoticons_str,
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
        r'(?:[\w_]+)',  # other words
        r'(?:\S)'  # anything else
    ]

    tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

    def tokenize(s):
        return tokens_re.findall(s)

    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens

    # tweet = 'RT @JordiTorresBCN: just an example! :D http://JordiTorres.Barcelona #masterMEI'
    # print(preprocess(tweet))

    count = 0
    for status in tweepy.Cursor(api.home_timeline).items():
        if status.lang == "en":
            print(preprocess(status.text))
            count += 1
        if count == 10:
            break


task23()
