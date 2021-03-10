import nltk
nltk.download('punkt')
nltk.download('stopwords')

import re
from collections import Counter
from nltk.corpus import stopwords

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    no_punctuation = re.sub(r'[^\w\s]', '', lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
sw = stopwords.words('english')
filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)
print(count.most_common(10))
print(sum(count.values()))
