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
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# import re
# todo: learn regular expressions

#open the rain data file
with open('rain_data.csv', 'r') as file:
    lines = file.read().split('\n')
# print(len(lines))

# first line of file contains variable names (dict keys)
varnames = lines[0].split(',')
# print(f'varnames = {varnames}')

# split all lines into lists of values
for i in range(len(lines)):
    lines[i] = (lines[i].split(','))
#print(f'raw data = {lines}')

# construct list of dicts with keys and values
data_list = []
for i in range(1, len(lines) - 1):
    if ' ' in lines[i] or '-' in lines[i] or '' in lines[i]:
        continue
    data_list.append(dict(zip(varnames, lines[i])))

# look at the data
print(data_list)
print(data_list[0])
# print(data_list[-1])
# print(data_list[-1]['Date'])
# print(len(data_list))

# strip out the dates to datetime format
for i in range(len(data_list)):
    data_list[i]['Date'] = datetime.datetime.strptime(data_list[i]['Date'], '%m/%d/%y')
for i in range(len(data_list)):
    data_list[i]['Year'] = data_list[i]['Date'].year

# look at the data
print(data_list[0])

# print(len(data_list))

#
# # delete rows with missing rain data
# data_list.pop()                         # last row
# for i in range(len(data_list)):
#     if data_list[i]['Total'] == '-':
#         data_list.pop(i)

# recast 'Total' to int
for i in range(len(data_list)):
    data_list[i]['Total'] = int(data_list[i]['Total'])
# print(data_list[0])

# calculate sum of daily 'Total' rain
sum_rain = 0
for row in data_list:
    sum_rain += row['Total']

# calculate mean of daily 'Total' rain
mean_rain = sum_rain / len(data_list)

# calculate squared deviances from mean
for i in range(len(data_list)):
     data_list[i]['sq_deviance_rain'] = (data_list[i]['Total'] - mean_rain) ** 2

# calculate sum of squared deviances
sum_sq_deviance_rain = 0
for row in data_list:
    sum_sq_deviance_rain += row['sq_deviance_rain']


# calculate variance of 'Total' rain
var_rain = sum_sq_deviance_rain / len(data_list)

# calculate min and max
max_rain = 0
for i in range(len(data_list)):
    if data_list[i]['Total'] > max_rain:
        max_rain = data_list[i]['Total']
min_rain = max_rain
for i in range(len(data_list)):
    if data_list[i]['Total'] < min_rain:
        min_rain = data_list[i]['Total']

# find the date with the most rain
for i in range(len(data_list)):
    if data_list[i]['Total'] == max_rain:
        most_rain_date = data_list[i]['Date']
    else:
        continue

print(f'\nSummary statistics for rain, {data_list[-1]["Date"]} to {data_list[0]["Date"]}: ')
print(f' N = {len(lines)} \n \
n_missing = {len(lines) - len(data_list)} \n \
mean = {round(mean_rain, 2)} \n \
variance = {round(var_rain, 2)} \n \
standard deviation = {round(var_rain ** (1/2), 2)} \n \
max = {max_rain} \n \
min = {min_rain} \n \
')

print(f'\nThe day with the most rain was {most_rain_date}.')

# get yearly data sets
# the following does nothing but reproduce the original data set and order it by date
# what I'm trying to do is subset the data by year
rain_data_by_year = []
for year in range(2003, 2018):           # these are the years with complete data (though with some small missing-ness)
    for row in data_list:
        if row['Date'].year == year:
            rain_data_by_year.append(row)

print(rain_data_by_year[0:3])
# rain_data_by_year.sort(key = 'Date')          # this doesn't work

# plt.plot(data_list['Date'], data_list['Total'])   # this doesn't work
