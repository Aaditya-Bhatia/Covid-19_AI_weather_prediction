#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:37:15 2020

@author: aadityabhatia

1. Assuming the person got infected 7-14 days ago, we take the median temprature for that time!
2. Take all new cases

"""

import pandas as pd

dirName = '/Users/aadityabhatia/Projects/Coronavirus/'

fullData = pd.read_csv(dirName+'corona_data/full_data.csv')

fullData['location'] = fullData.location.apply(lambda val:val.replace(' ', '%20'))

locations = fullData.location.unique()


countryStats = pd.DataFrame()

for country in locations:
    
    weather = pd.read_csv(dirName+'weather_data/'+country+'.csv')
    weather['location'] = country
    weather['date'] = pd.to_datetime(weather.date_time)
    
    corona = fullData[fullData.location.str.contains(country)]
    corona['date'] = pd.to_datetime(corona.date)
    
    coronaWeather = pd.merge(weather, corona, on=['location', 'date'], how='inner')
    coronaWeather = coronaWeather.fillna(0)
    
#    currentStats = coronaWeather.groupby('location', as_index=False).agg({'maxtempC':'median', 
#                                        'mintempC':'median',
#                                        'humidity':'median',
#                                        'tempC':'median',
#                                        'HeatIndexC':'median',
#                                        'WindChillC':'median',
#                                        'new_cases':'sum'
#                                        })
#    print(currentStats)
    countryStats = countryStats.append(coronaWeather)
countryStats = countryStats.reset_index()
del countryStats['index']
countryStats.to_csv(dirName+'country_weather_corona_cases.csv', index=False)