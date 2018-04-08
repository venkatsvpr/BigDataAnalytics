#!/usr/bin/python
from nltk.tokenize import word_tokenize
import re
import pandas as pd
from nltk.corpus import stopwords,wordnet
import string
import sys
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
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

delete_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r'[^\x00-\x7f]' #hex characters
    #r"(?:[a-z][a-z'\-_]+[a-z])" # words with - and '
    #r'(?:[\w_]+)', # other words
    #r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
delete_re = re.compile(r'('+'|'.join(delete_str)+')', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    tokens = tokens_re.findall(s)
    tokens = [token for token in tokens if not delete_re.search(token)]
    return tokens

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt','RT', 'via', 'new' , 'york' , 'one' , 'like' , 'would','also','us','ms','page','think','time', 'first','last','get','even','subscribe','days','city','mr','years','year','p','amp','man','video','live','please','love','much','could', 'u']
#freq_words  = ["facebook","trump","media","president","social","public","cambridge","users" ,"scandal","campaign", "voters","election","influence"]
#freq_words_ny = ["said" , "people", "facebook", "times", "trump", "please",  "many", "could", "see","two", "company", "twitter", "president", "day", "news" ]
freq_words = ["facebook","financial","aid","data","office","stole","howard","tyrone","hankerson","student-employee","twitter","news","google","want","information"]
for line in sys.stdin:
    if (len(line) == 0):
        continue;
    line = line.strip()
    line = line.lower();
    new_line = [term for term in tokenize(line) if not term in stop]
    d = dict()
    for word in new_line:
        if word in freq_words:
            d[word] = True
    for index,word in enumerate(freq_words):
        if word not in d:
            continue;
        for i2 in range(index+1,len(freq_words)):
            if (freq_words[i2] not in d):
                continue;
            print (freq_words[index]+","+freq_words[i2]+"\t1")
