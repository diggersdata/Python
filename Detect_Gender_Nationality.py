# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:59:48 2022

@author: Data Diggers
"""

from names_dataset import NameDataset, NameWrapper
# The V3 lib takes time to init (the database is massive). Tip: Put it into the init of your app.
nd = NameDataset()


import pandas as pd
h=pd.read_excel("/Users/ived/Desktop/Python_Gender_Identification/Hackathon_Data_MinorityWomenOwned_2022 v1.xlsx")

"""initial declaration"""
firstname=[]
lastname=[]
gender=[]
country=[]

"""Firstname """
for i in range(len(h['executiveContact1'])):
    firstname.append(str(h['executiveContact1'][i]).split(' ')[0])
firstname = pd.DataFrame(firstname, columns=['firstname'])

"""LastName"""
for i in range(len(h['executiveContact1'])):
    d=str(h['executiveContact1'][i]).split(' ')
    if len(d)>1:
        z=str(h['executiveContact1'][i]).split(' ')[1]
    else:
        z=str(h['executiveContact1'][i]).split(' ')[0]
    lastname.append(z)

lastname = pd.DataFrame(lastname, columns=['lastname'])


"""gender"""
for i in range(len(firstname)):
    gender.append(NameWrapper(nd.search(firstname['firstname'][i])).describe.split(',')[0])    
gender = pd.DataFrame(gender, columns=['PrimaryLeadershipGender'])

h['PrimaryLeadershipGender']=gender['PrimaryLeadershipGender']



"""country"""
for i in range(len(lastname)):
    if len(NameWrapper(nd.search(lastname['lastname'][i])).describe.split(',')[1])>1:
        country.append(NameWrapper(nd.search(lastname['lastname'][i])).describe.split(',')[1]) 
    else:
        country.append(NameWrapper(nd.search(firstname['firstname'][i])).describe.split(',')[1]) 
 
country = pd.DataFrame(country, columns=['PrimaryLeadershipOrigin'])

h['PrimaryLeadershipOrigin']=country['PrimaryLeadershipOrigin']


"""Output excel"""
h.to_excel("updatedGenderoFexecutiveContact2.xlsx")



