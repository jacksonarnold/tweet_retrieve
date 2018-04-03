from twarc import Twarc
import csv

# Replace with your keys and tokens
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

# Files
tweetList = r"NCHB2-idsab.txt"
csv_write = csv.writer(open("tweets.csv", "wb"))

# Hydrate tweets (remove break to go through entire list)
i = 0
for tweet in t.hydrate(open(tweetList)):
    text = tweet["full_text"].encode('utf-8')
    csv_write.writerow([tweet["id"], text])
    i += 1
    if i == 5:
        break

