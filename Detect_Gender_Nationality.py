# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:59:48 2022

@author: DATA DIGGERS 
"""

from names_dataset import NameDataset, NameWrapper
# The V3 lib takes time to init (the database is massive). Tip: Put it into the init of your app.
nd = NameDataset()


import pandas as pd
import numpy as np
h=pd.read_excel("C:\\Users\\Asus\\Desktop\\Data1.xlsx")

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
    d=str(h['executiveContact1'][i]).split('-')[0]
    d=d.split(' ')
    if len(d)>1:
        if d[len(d)-1]=='':
            z=d[len(d)-2]
        else:
            z=d[len(d)-1]        
    else:
        z=d[0]
    lastname.append(z)

lastname = pd.DataFrame(lastname, columns=['lastname'])


"""PrimaryLeadershipGender"""
for i in range(len(firstname)):
    if NameWrapper(nd.search(firstname['firstname'][i])).describe.split(',')[0] !='':
        gender.append(NameWrapper(nd.search(firstname['firstname'][i])).describe.split(',')[0])  
    else:
        gender.append(NameWrapper(nd.search(lastname['lastname'][i])).describe.split(',')[0])  
    
gender = pd.DataFrame(gender, columns=['PrimaryLeadershipGender'])

h['PrimaryLeadershipGender']=gender['PrimaryLeadershipGender']



"""PrimaryLeadershipNationality"""
for i in range(len(lastname)):
    if len(NameWrapper(nd.search(lastname['lastname'][i])).describe.split(',')[1])>1:
        country.append(NameWrapper(nd.search(lastname['lastname'][i])).describe.split(',')[1]) 
    else:
        country.append(NameWrapper(nd.search(firstname['firstname'][i])).describe.split(',')[1]) 
 
country = pd.DataFrame(country, columns=['PrimaryLeadershipNationality'])

h['PrimaryLeadershipNationality']=country['PrimaryLeadershipNationality']
final_df=h.iloc[:,:] # Select From 2nd to end

"""Output excel"""
#final_df.to_excel("Diversity_Owned_Data.xlsx")
#final_df.to_csv('Diversity_Owned_Data_delimited.csv', sep ='\t')

final_df=final_df[['dunsNum','dunsName', 'county', 'streetAddress', 'city', 'STATE',
       'zip', 'phone', 'executiveContact1', 'executiveContact2',
       'isWomanOwned', 'MinorityOwnedDesc', 'PrimaryLeadershipGender',
       'PrimaryLeadershipNationality']]

final_df=final_df.replace(np.nan, '')
np.savetxt("C:\\Users\\ASUS\\Diversity_Owned_Data_delimited.txt",final_df.values,delimiter='\t',header="dunsNum\tdunsName\tcounty\tstreetAddress\tcity\tSTATE\tzip\tphone\texecutiveContact1\texecutiveContact2\tisWomanOwned\tMinorityOwnedDesc\tPrimaryLeadershipGender\tPrimaryLeadershipNationality",fmt='%s')




