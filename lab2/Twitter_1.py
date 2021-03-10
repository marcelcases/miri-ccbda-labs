"""
Task 2.2.1: Accessing your twitter account information
"""

import os
import tweepy
from tweepy import OAuthHandler


consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# print the main information of your Twitter account
user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Followers: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))