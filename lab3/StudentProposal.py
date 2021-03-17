import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('BitcoinTweets.json', 'a') as f:
                f.write(data)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        count = len(open('BitcoinTweets.json', 'r').readlines())/2
        if count < 50:
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Bitcoin'])

import re
import operator
import json
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") # download the stopword corpus on our computer
import string

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', '…', '’', u'\uFE0F']

fname = 'BitcoinTweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    count_hash = Counter()
    count_terms = Counter()
    for line in f.readlines():
        if line != "\n":
            tweet = json.loads(line)
            # Create a list with all the terms
            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            count_all.update(terms_stop)
            terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#') and term != '#']
            count_hash.update(terms_hash)
            terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]
            count_terms.update(terms_only)
    print("Top 10 tokens:")
    for word, index in count_all.most_common(10):
        print ('%s : %s' % (word, index))
    print("")
    print("Top 10 hashtags:")
    for word, index in count_hash.most_common(10):
        print ('%s : %s' % (word, index))
    print("")
    print("Top 10 terms:")
    for word, index in count_terms.most_common(10):
        print ('%s : %s' % (word, index))

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (6,6)
import matplotlib.pyplot as plt

sorted_x, sorted_y = zip(*count_all.most_common(10))
print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')
plt.title("Most common tokens")

plt.show()                  # show it on IDE
plt.savefig('StudentCaseStudyToken.png')     # save it on a file

plt.clf()
sorted_x, sorted_y = zip(*count_hash.most_common(10))
print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')
plt.title("Most common hashtags")

plt.show()                  # show it on IDE
plt.savefig('StudentCaseStudyHashtags.png')     # save it on a file

plt.clf()
sorted_x, sorted_y = zip(*count_terms.most_common(10))
print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')
plt.title("Most common terms")

plt.show()                  # show it on IDE
plt.savefig('StudentCaseStudyTerms.png')     # save it on a file