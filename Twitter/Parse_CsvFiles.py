#!/usr/bin/python
import pandas as pd
data = pd.read_csv("twitter_facebook_April_1.tweets.csv")
f = open("april_1.txt","w+")
count = 0
for line in data["text"]:
    f.write(line)
    count += 1
print (" Files written successfully  : Total successfull:",count)
f.close()
