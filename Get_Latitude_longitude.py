#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:17:38 2022

@author: ived
"""
# Import pandas package  
import pandas as pd 
import numpy as np
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
    
# Define a dictionary containing  data 
# data = {'City':['Bangalore', 'Mumbai', 'Chennai', 'Delhi']} 
h=pd.read_excel("C:\\Users\\ASUS\\Desktop\\data1.xlsx")
df = pd.DataFrame(h, columns=['City'])
df['City']  =h['city']
df=df.drop_duplicates() 
df.to_excel("GeoData.xlsx")
# declare an empty list to store
# latitude and longitude of values
# of city column
longitude = []
latitude = []
city=[]
locationDF = pd.DataFrame()
geolocator = Nominatim(user_agent="Data_diggers")
      
# each value from city column
# will be fetched and sent to
# function find_geocode

k=0
for i in  df['City']:	
    k=k+1
    print(k)
    """print(city)"""
    """print(longitude)"""
    """print(latitude)"""
    loc = geolocator.geocode(i)
    if loc is not None:
        latitude.append(loc.latitude)
        longitude.append(loc.longitude)
        city.append(i)
    else:
        city.append(i)
        latitude.append(None)
        longitude.append(None)


 
locationDF = pd.DataFrame (city, columns = ['City'])
locationDF['latitude'] = pd.DataFrame (latitude, columns = ['latitude'])
locationDF['longitude'] = pd.DataFrame (latitude, columns = ['longitude'])

locationDF.to_excel("locationDF.xlsx")

locationDF=locationDF[['City','latitude','longitude']]
np.savetxt("C:\\Users\\ASUS\\locationDF2.txt",locationDF.values,header="City\tlatitude\tlongitude" , delimiter='\t',fmt='%s')
