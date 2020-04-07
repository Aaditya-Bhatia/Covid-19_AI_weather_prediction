#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:49:57 2020

@author: aadityabhatia

Problem statement:
    
The keywords field contains search queries typed in by users into Google and the brand and product name 
are of the product that Google serves to that user based on the query.
We're trying to ascertain whether Google is serving a relevant product to the user on two dimensions. 
First, if the user has typed in a brand, has the user typed in the brand of the product shown?
 Second, if the user has given enough information in the query to specifically identify the product,
 is it the product that Google has shown?
 We have manually pre-classified the data in the attached for the purposes of developing your model.

"""

import pandas as pd

df = pd.read_csv('/Users/aadityabhatia/Projects/upwork/queries_updated.csv')

'''
questions for Chan:
1. I don't see the use of ML here. 
The procedure that I followed here is:
1. Performing stemming and lemmatization
2. Convert into embeddings (TF)
3. Perform string matching / 
BS
Jaccard similarity matrix
4. Make clustering models to group the similarity matrix of the 2 cols
5. Make classification models to classify if the matrix has similarity or not! If it is then we return 1 or yes.

Non_BS:
String matching to 
'''


import pandas as pd
from math import log, e
import numpy as np
import string
import pandas as pd
import nltk
import unidecode
from nltk.corpus import stopwords
import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
nlp = spacy.load("en", disable=['parser', 'tagger', 'ner'])
stops = stopwords.words("english")
punctuations = string.punctuation
for p in punctuations:
    stops.append(p)
stops.append('') 

def getLemma(comment):
    lemmatized = []
    comment = unidecode.unidecode(str(comment).lower())
    tokens = nlp(comment) # This has been tokenized  + formatting added (\n\r)
    for token in tokens: 
        token = token.lemma_.strip() 
        if token not in stops:
            lemmatized.append(token)
    return lemmatized
#    return ' '.join(lemmatized)

df['query_lemma'] = df['query'].apply(getLemma)
df['brand_lemma'] = df['brand'].apply(getLemma)
df['product_lemma'] = df['product'].apply(getLemma)

# new
df['Brand_check_Aaditya'] = 0
df['Product_check_Aaditya'] = 0

for i, row in df.iterrows():
    l2 = row['query_lemma']
    l1 = row['brand_lemma']    
    for item1 in l1:
        if item1 in l2:
            df.set_value(i, 'Brand_check_Aaditya', 1)
            break
    l2 = row['query_lemma']
    l1 = row['product_lemma']    
    for item1 in l1:
#        print (item1, 'in', l2)
        print (item1)
        if item1 in l2:
            df.set_value(i, 'Product_check_Aaditya', 1)
            break

from sklearn.metrics import accuracy_score
df['brand_check'] = df.brand_check.replace(to_replace=['N', 'Y'], value=[0, 1])
df['product_check'] = df.product_check.replace(to_replace=['N', 'Y'], value=[0, 1])
print(accuracy_score(df.brand_check.values  ,  df.Brand_check_Aaditya.values))
print(accuracy_score(df.product_check.values  ,  df.Product_check_Aaditya.values))

temp = df[df.product_check != df.Product_check_Aaditya]
temp.to_csv('temp.csv')


df['brand_check'] = df.brand_check.replace(to_replace=[0,1], value=['N', 'Y'])
df['product_check'] = df.product_check.replace(to_replace=[0,1], value=['N', 'Y'])
df['Brand_check_Aaditya'] = df.Brand_check_Aaditya.replace(to_replace=[0, 1], value=['no', 'yes'])
df['Product_check_Aaditya'] = df.Product_check_Aaditya.replace(to_replace=[0, 1], value=['no', 'yes'])

df.to_csv('/Users/aadityabhatia/Projects/upwork/queries_updated_processed.csv', index=0)


'''
testing
'''
import pandas as pd
dt = pd.read_csv('/Users/aadityabhatia/Projects/upwork/queries_updated_processed.csv')
temp = dt[dt.product_check != dt.Product_check_Aaditya]
temp.to_csv('/Users/aadityabhatia/Projects/upwork/temp.csv')


temp[['query', 'product', 'product_check', 'query_lemma', 'product_lemma',
'Product_check_Aaditya']].to_csv('/Users/aadityabhatia/Projects/upwork/temp_product.csv')