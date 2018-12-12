"""
author: Richard Sherman
2018-12-12
lab24-rain-data.py, manipulates rain data from
City of Portland HYDRA Rainfall Network
Metro Learning Center Rain Gage
2033 NW Glisan St.
https://or.water.usgs.gov/non-usgs/bes/metro_center.rain
"""
# the file 'rain_data.txt' was processed outside of python

import datetime
import matplotlib

# import re
# todo: learn regular expressions

#open the rain data file
with open('rain_data.csv', 'r') as file:
    lines = file.read().split('\n')

# first line of file contains variable names (dict keys)
varnames = lines[0].split(',')
print(f'varnames = {varnames}')

# split all lines into lists of values
for i in range(len(lines)):
    lines[i] = (lines[i].split(','))
#print(f'raw data = {lines}')

# construct list of dicts with keys and values
data_list = []
for i in range(1, len(lines) - 1):
    # if '' in lines[i]:
    #     continue
    data_list.append(dict(zip(varnames, lines[i])))

# look at the data
# print(data_list)
print(data_list[0])
print(data_list[-1])
print(data_list[0]['Date'])

# strip out the dates to datetime format
for i in range(len(data_list)):
    data_list[i]['Date'] = datetime.datetime.strptime(data_list[i]['Date'], '%m/%d/%y')

# look at the data
print(data_list[0])
print(data_list[-1])

