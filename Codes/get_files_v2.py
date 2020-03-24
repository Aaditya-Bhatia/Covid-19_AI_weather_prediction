#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:58:13 2020

@author: aadityabhatia

Exploring the WHO api for coronavirus
DATA DOWNLOAD : https://ourworldindata.org/coronavirus-source-data
WEATHER DATA: https://www.worldweatheronline.com/developer/my/#


"""



import pandas as pd
from wwo_hist import retrieve_hist_data
import os

dirName = '/Users/aadityabhatia/Projects/Coronavirus/'

# getting the coronavirus data
os.chdir(dirName+'corona_data')
fullData = pd.read_csv('full_data.csv')

# getting only the rows which have new cases
fullData = fullData[fullData.total_cases > 0]
fullData['date'] = pd.to_datetime(fullData.date)

print(fullData.date.min(), 'to', fullData.date.max())


# getting the full weather data
frequency = 24
start_date = '7-JAN-2020'
end_date = '16-MAR-2020'
api_key = 'c8a0ce63aa4f4f099c8164611201703'
#api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

locations = list(fullData.location.unique())
location_list = list(map(lambda val:val.replace(' ', '%20') , locations))

if not os.path.exists(dirName+'weather_data'):
    os.mkdir(dirName+'weather_data')
os.chdir(dirName+'weather_data')
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)