#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:56:08 2020

@author: aadityabhatia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dirName = '/Users/aadityabhatia/Projects/Coronavirus/'
df = pd.read_csv(dirName + 'country_weather_corona_cases.csv')

df.new_cases.corr(df.WindChillC, method="pearson") #0.02
df.new_cases.corr(df.mintempC, method="pearson") #0.03
df.new_cases.corr(df.humidity, method="pearson") #
df.new_cases.corr(df.WindChillC, method="pearson") 



fig, ax = plt.subplots()
#ax.plot(df.mintempC, df.new_cases, 'bo')
ax.plot(df.humidity, df.new_cases, 'bo')
ax.plot(df.mintempC, df.new_cases, 'bo')


