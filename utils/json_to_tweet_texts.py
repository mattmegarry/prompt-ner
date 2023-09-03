import json
import os

num_tweets = 100

with open('sultana_517.json') as f:
  data = json.load(f)

all_tweets = ''
for i in range(num_tweets):
    all_tweets += data[i]['text']

with open(f'{num_tweets}_tweets.txt', 'w') as f:
    f.write(all_tweets)
