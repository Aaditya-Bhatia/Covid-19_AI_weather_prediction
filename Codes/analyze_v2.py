#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:45:03 2020

@author: aadityabhatia
"""


import pandas as pd
from datetime import timedelta
dirName = '/Users/aadityabhatia/Projects/Coronavirus/'

fullData = pd.read_csv(dirName+'corona_data/full_data.csv')
fullData = fullData[fullData.total_cases > 0]

fullData['location'] = fullData.location.apply(lambda val:val.replace(' ', '%20'))

fullData['date'] = pd.to_datetime(fullData.date)
fullData['incubationDateStart'] = fullData['date'] - timedelta(days=14)
fullData['incubationDateEnd'] = fullData['date'] - timedelta(days=7)

locations = fullData.location.unique()

data = pd.DataFrame()
for country in locations:

    weather = pd.read_csv(dirName+'weather_data/'+country+'.csv')
    weather['location'] = country
    weather['date'] = pd.to_datetime(weather.date_time)
    
    corona = fullData[fullData.location == (country)]
    for i, row in corona.iterrows():
        startDate = row['incubationDateStart']
        endDate = row['incubationDateEnd']
        weather_per_case = weather[(weather.date >= startDate) & (weather.date <= endDate)]
        weather_av = weather_per_case.groupby('location', as_index=False).agg({
                'maxtempC':'median', 'mintempC':'median', 'FeelsLikeC':'median', 'HeatIndexC':'median',
                'WindChillC':'median', 'humidity':'median', 'tempC':'median'
                })

        conditions_ = pd.merge(row.to_frame().T, weather_av, on='location')
        data = data.append(conditions_)
 
data = data.reset_index()
del data['index']
data.to_csv(dirName+'corona_cases_past_weather_mar18.csv', index=False)

import pandas as pd
data = pd.read_csv(dirName+'corona_cases_past_weather_mar18.csv')

data['Label'] = 0
data.loc[data.new_cases > 0, 'Label'] = 1

print (len(data[data.new_cases >= 1]), len(data[data.Label ==1]))
print (len(data))


data.to_csv(dirName+'corona_model_features.csv', index=False)