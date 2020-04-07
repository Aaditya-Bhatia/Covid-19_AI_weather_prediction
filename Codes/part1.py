#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:18:34 2020

@author: aadityabhatia
"""

# which countries reached saturation in coronavirus cases
import pandas as pd
import matplotlib.pyplot as plt

dirName = '/Users/aadityabhatia/Documents/GitHub/Covid-19_AI_weather_prediction/'

fullData = pd.read_csv(dirName+'corona_data/full_data.csv')
fullData = fullData[fullData.total_cases > 0]

china = fullData[fullData.location.str.contains('China')]
korea = fullData[fullData.location.str.contains('Korea')]

print('Korea range is 20Jan to 21 Feb')
print('China range is 31st Dec to 8 Mar')

world = fullData[fullData.location == 'World']

world.total_cases.hist()