#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:44:15 2019

@author: rs
"""

import requests
import re
import datetime
import pprint
import matplotlib.pyplot as plt

# download data from a single rain-measurement location
rain = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain').text
# print(rain)

# select the 'date' and 'total' columns
data = re.findall('(\d{2}-\w{3}-\d{4}) +(\d+)', rain)
print(data[0])

# convert the first 'column' to datetime, the second 'column' to int
for i in range(len(data)):
    data[i] = datetime.datetime.strptime(data[i][0], '%d-%b-%Y'), int(data[i][1])
print(data[0])

# calculate mean, variance, standard deviation
total_rain = 0
for i in range(len(data)):
    total_rain += data[i][1]
mean_daily_rain = total_rain / len(data)

sum_sq_deviance = 0
for i in range(len(data)):
    sum_sq_deviance += (data[i][1] - mean_daily_rain) ** 2
rain_variance = sum_sq_deviance / len(data)
rain_sd = rain_variance ** 0.5

# calculate min and max
max_daily_rain = 0
for i in range(len(data)):
    if data[i][1] > max_daily_rain:
        max_daily_rain = data[i][1]

min_daily_rain = max_daily_rain
for i in range(len(data)):
    if data[i][1] < min_daily_rain:
        min_daily_rain = data[i][1]

# find the date with the most rain
for i in range(len(data)):
    if data[i][1] == max_daily_rain:
        most_rain_date = data[i][0]
    else:
        continue

# print summary stats
print(f'\nSummary statistics for rain, {data[-1][0]} to {data[0][0]}: ')
print(f' N = {len(data)} \n \
mean = {round(mean_daily_rain, 2)} \n \
variance = {round(rain_variance, 2)} \n \
standard deviation = {round(rain_variance ** 0.5, 2)} \n \
max = {max_daily_rain} \n \
min = {min_daily_rain} \n \
')
print(f'\nThe day with the most rain was {most_rain_date}.\n')

# get range of years in data

years = [row[0].year for row in data]
years = list(set(years))
years.sort()
# print(years)
end_year = years[-1]
start_year = years[0]

# calculate yearly totals of rain
total_yearly_rain = {}
for year in range(start_year, end_year + 1):
    total_yearly_rain[year] = 0
    for i in range(len(data)):
        if data[i][0].year == year:
            total_yearly_rain[year] += data[i][1]
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(total_yearly_rain)


# get the length of each year
days_in_year = {}
for year in range(start_year, end_year + 1):
    days_in_year[year] = 0
    for i in range(len(data)):
        if data[i][0].year == year:
            days_in_year[year] += 1
# pp.pprint(days_in_year)        

# calculate yearly average rain and print it
average_rain_by_year = {}
for year in range(start_year, end_year + 1):
    average_rain_by_year[year] = round(total_yearly_rain[year] / days_in_year[year], 2)
print('Average rain by year:')
pp.pprint(average_rain_by_year)        

fig, ax = plt.subplots()
ax.bar(average_rain_by_year.keys(), average_rain_by_year.values())
ax.set_xlabel('Year')
ax.set_ylabel('Rain, hundredths of inch')
ax.set_title(f'Average daily rain, {start_year} - {end_year}')
ax.set_xticks(years)
plt.xticks(rotation = 45)

# calculate total rain by month
months = [row[0].month for row in data]
months = list(set(months))
months.sort
total_monthly_rain = {}
for month in months:
    total_monthly_rain[month] = 0
    for i in range(len(data)):
        if data[i][0].month == month:
            total_monthly_rain[month] += data[i][1]
pp.pprint(total_monthly_rain)    

# get the length of each month
days_in_month = {}
for month in months:
    days_in_month[month] = 0
    for i in range(len(data)):
        if data[i][0].month == month:
            days_in_month[month] += 1
pp.pprint(days_in_month)

# calculate average rain by month
average_rain_by_month = {}
for month in months:
    average_rain_by_month[month] = round(total_monthly_rain[month] / days_in_month[month], 2)
pp.pprint(average_rain_by_month)

fig, ax = plt.subplots()
ax.bar(average_rain_by_month.keys(), average_rain_by_month.values())
ax.set_xlabel('Month')
ax.set_ylabel('Rain, hundredths of inch')
ax.set_title(f'Average rain by month, {start_year} - {end_year}')
ax.set_xticks(months)