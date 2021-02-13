# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:21:31 2018

@author: Vaanis-Laptop
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:02:42 2020

@author: Vaanis-Laptop

"""
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, RegexpTokenizer
from textblob import TextBlob

sid = SentimentIntensityAnalyzer()

file2= open("Positive.txt","r")
contents= file2.read()
contents= contents.lower()
positive= word_tokenize(contents)
num_p= len(positive)

file1 = open("Negative.txt", "r")
contents= file1.read()
contents= contents.lower()
negative=word_tokenize(contents)
num_n= len(negative)

count_p=0
count_n=0
sum_p=0
sum_n=0


for word in positive:
    check= sid.polarity_scores(word)['compound']
    if (check) >= 0.1:
        sum_p= sum_p+ check
        count_p= count_p+1

for word in negative:
    check= sid.polarity_scores(word)['compound']
    if check <= -0.1:
        sum_n= sum_n+check
        count_n= count_n+1
        
av_p= sum_p/count_p
av_n= sum_n/count_n


def send2():
    return av_p, av_n