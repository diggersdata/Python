#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:07:27 2022

@author: ived
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:19:02 2022

@author: ived
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import nltk
from nltk.corpus import names
import random
from nltk.classify import apply_features
nltk.download('names')



# def gender_features_tls(word):
#     return {'suffix1': word[-1:], 'suffix2': word[-2:]}
# # print(gender_features_az('John'))



def gender_features_icv(name):
    features = {}
    temp_name = name.lower()
    lenName = len(name)    
#     features["name_len"] = len(name)
    features["firstletter"] = name[0].lower() 
    features["lastletter"] = name[-1].lower() 
    features["prefix"] = name[:3].lower() if len(name) > 4 else name[:2].lower() 
    features["suffix"] = name[-3:].lower() if len(name) > 4 else name[-2:].lower()
    Vowel = ['a','e','i','o','u']
    Vclusters = []
    flag = False
    for vb in Vowel[::-1]:
        if vb in temp_name:
            n_vowels= temp_name.count(vb) # COunt how many times you see Vowels            
            temp_name = temp_name.replace(vb, "")
            Vclusters.append(vb)
            features[vb]=n_vowels
#             features["Len_vowel"] = features["Len_vowel"] + n_vowels

    return features


f = open('/Hackathon/Indian-Male-Names.csv').read()
f1 = open('/Hackathon/female.txt').read()
  
labeled_names = ([(word, 'male') for word in f.split()]+
             [(word1, 'female') for word1 in f1.split()])

random.shuffle(labeled_names)


featuresets_az = [(gender_features_icv(n), gender) 
               for (n, gender)in labeled_names]


train_set, test_set = featuresets_az[7000:], featuresets_az[:7000]
classifier_az = nltk.NaiveBayesClassifier.train(train_set)
accuracy_az= nltk.classify.accuracy(classifier_az, test_set)


  
print(classifier.classify(gender_features_az('ALAN')))
print(nltk.classify.accuracy(classifier_az, train_set))
# print(classifier.show_most_informative_features(5))
