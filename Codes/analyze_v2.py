#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:45:03 2020

@author: aadityabhatia
"""


import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
dirName = '/Users/aadityabhatia/Documents/GitHub/Covid-19_AI_weather_prediction/'

fullData = pd.read_csv(dirName+'corona_data/full_data.csv')
fullData = fullData[fullData.total_cases > 0]
fullData['date'] = pd.to_datetime(fullData.date)
#world
world = fullData[fullData.location == 'World']
w = world.tail(10)
w['total_cases'] = w['total_cases']/10000
plt.plot(w['total_cases'], w.date,'bo')

fullData['location'] = fullData.location.apply(lambda val:val.replace(' ', '%20'))

fullData['date'] = pd.to_datetime(fullData.date)
fullData['incubationDateStart'] = fullData['date'] - timedelta(days=14)
fullData['incubationDateEnd'] = fullData['date'] - timedelta(days=7)

locations = fullData.location.unique()

data = pd.DataFrame()
data.to_csv(dirName+'corona_cases_past_weather_mar18.csv', index=False)

import pandas as pd
data = pd.read_csv(dirName+'corona_cases_past_weather_mar18.csv')

data['Label'] = 0
data.loc[data.new_cases > 0, 'Label'] = 1

print (len(data[data.new_cases >= 1]), len(data[data.Label ==1]))
print (len(data))


data.to_csv(dirName+'corona_model_features.csv', index=False)