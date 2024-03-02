# -*- coding: utf-8 -*-
"""Chat_Bot

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RMGOvGmXVA-GHYlVm8JvzGUGy6E-G7ax

**importing the required libraries**
"""

pip install numpy

import numpy as np
import nltk
import string
import random

"""**importing and reading the corups**

"""

f=open('/content/python_chatbot.txt', 'r',errors = 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

"""**example of sentence tokens**"""

sent_tokens[:2]

"""**example of word tokens**"""

word_tokens[:2]

"""**text preprocessing**"""

lemmer = nltk.stem.WordNetLemmatizer()

#wordNet is a semantically-oriented dictionary of English included in NLTK
def LemTokens (tokens):
  return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

"""**defining the greeting function**"""

GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREET_RESPONSES =["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greet (sentence):
  for word in sentence.split():
    if word.lower() in GREET_INPUTS:
      return random.choice(GREET_RESPONSES)

"""**response generation**"""

!pip install scikit-learn
!pip show scikit-learn

import sklearn
print(sklearn.__version__)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
  robo1_response=' '
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx=vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1+"I an sorry! T don't understand you"
    return robo1_response
  else:
    robo1_response = robo1_respomse+sent_tokens[idx]
    return robo1_response

"""**defining conversation start/end protocols**"""

flag=True
print("Bot: My name is sonali, let's have a conversation! Also, if you want to exit any time, just type Bye!")

while(flag==True):
  user_response = input()
  user_response=user_response.lower()
  if(user_response!='bye'):
    if(user_response== 'thanks' or user_response=='thank you' ):
      flag=False
      print("BOT: You are welcome..")
    else:
        if(greet(user_response)!=None):
          print("BOT: "+greet(user_response))
        else:
            sent_tokens.append(user_response)
            word_tokens=word_tokens+nltk.word_tokenize(user_response)
            final_words=list(set(word_tokens))
            print("BOT: ",end="")
            print(response(user_response))
            sent_tokens.remove(user_response)
  else:
      flag=False
      print("BOT:Goodbye! Take care <3" )