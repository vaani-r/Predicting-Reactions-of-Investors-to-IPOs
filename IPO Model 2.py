# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:45:00 2018

@author: Vaanis-Laptop
"""

import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from question1 import send2
import string
import re

sid = SentimentIntensityAnalyzer()

#Finding the optimum value

file2= open("Positive.txt","r")
contents= file2.read()
contents= contents.lower()
positive= word_tokenize(contents)

file1 = open("Negative.txt", "r")
contents= file1.read()
contents= contents.lower()
negative=word_tokenize(contents)

#Calling function from other program
av_p, av_n = send2()

test_p=3
test_n=5
comp=0
value_n=0
value_p=0


file_input= input("Enter file location: ")
file= open(file_input,"r",errors='ignore')
contents= file.read()

#Processing the text
#Converting to lowercase and counting the number of words
contents= contents.lower()
#Remove numbers
contents= re.sub(r"\d+",'',contents)

while test_p <=4 and test_n>=4:
   pos={}
   neg={}
   for word in positive:
       check= sid.polarity_scores(word)['compound']
       if (check) >= 0.1:
          pos.update({word:(check*test_p)})
       else:
          pos.update({word:(av_p*test_p)}) 
        
   for word in negative:
       check= sid.polarity_scores(word)['compound']
       if check <= -0.1:
          neg.update({word:(check*test_n)})
       else:
          neg.update({word:(av_n*test_n)})
          
   final_Lex={}       
   final_Lex.update(sid.lexicon)       
   final_Lex.update(pos)
   final_Lex.update(neg) 
   sid.lexicon= final_Lex
   scores= sid.polarity_scores(contents)
   if (scores['compound'] > comp) and (scores['compound'] > 0):
       comp= scores['compound']
       value_n=test_n
       value_p=test_p
   test_p= test_p+0.001
   test_n= test_n-0.001

print(comp)
print(value_n)
print(value_p)





