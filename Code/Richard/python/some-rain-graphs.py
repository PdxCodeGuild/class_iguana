#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:49:50 2019

@author: rs
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rain = pd.read_csv('/Users/rs/data/rain.csv')

rain.rename(columns={'0': 'date', '1': 'rain'}, inplace=True)
rain['date'] = pd.to_datetime(rain['date'])

rain_2017 = rain[rain.date.dt.year == 2017]

rain['year'] = rain.date.dt.year
rain['month'] = rain.date.dt.month

g1 = sns.relplot('month', 'rain', 
            kind = 'line' , 
            data = rain[rain.date.dt.year == 2017])
plt.title('Daily rain (cm), 2017')
g1 = g1.set_axis_labels('month', 'rain')


sns.relplot('month', 'rain', kind = 'line', hue = 'year', legend = False, data = rain)
plt.title('Unreadable, but pretty graph of rain (cm) by year')
plt.legend(['2000', '2001', '2002', '2003', '2004', '2005', '2006', 
            '2007', '2008', '2009', '2010', '2011', '2012', '2013', 
            '2014', '2015', '2016', '2017', '2018'], bbox_to_anchor=(1.05, 1), loc=2)

sns.relplot('month', 'rain', kind = 'line', row = 'year', data = rain)
plt.title('Daily rain (cm) by year')

sns.relplot('month', 'rain', kind = 'line', col = 'year', col_wrap = 3, data = rain)
plt.suptitle('Daily rain (cm) by year')
plt.xlabel('month')
