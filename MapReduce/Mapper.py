#!/usr/bin/python
from nltk.tokenize import word_tokenize
import re
import pandas as pd
from nltk.corpus import stopwords
import string

import nltk
nltk.download('stopwords')

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

import sys
skip_words = ["2018","might","trade","back","percent","email","called","around","between","tech","going","company","New","York","you're","said,","against","including","March","whether","information","including","public","help","few","then","Times","off","firm","re-enterYou","work","through","use","United","still","see","verify","think.By","use","million","still","see","first","newsletter","subscribe","told","may","much","because","In","get","many","them","select","--","take","know","says","such","think","many","clicking","address.","him","box.Invalid","users","former","him","years","used","made","being","think","these","any","time","-","down","now","way","me","where","He","there","did","2018,","even","new","last","interested","my","if","so","feedback","two","just","page.","Tell","But","do","must","Ms.","no","said.","Please","It","robot","those","only","most","make","to.View","was","my","if","so","just","while","go","the","to","a","of","and","in","that","on","for","is","with","Was","by","as","from","it","at","said","are","not","has","have","he","an","this","The","be","Mr.","his","you","about","had","who","I","or","its","their","more","what","they","were","your","but","would","will","which","been","all","she","her","up","after","than","also","we","like","one","us","can","over","could","other","when","into","out","how","some","our","and","And","before","A","since","want"]
for line in sys.stdin:
    line = line.strip()
    new_line = [term for term in tokenize(line) if term not in stop]
    for word in new_line:
        if word in skip_words:
            continue;
        print(word+"\t1")
