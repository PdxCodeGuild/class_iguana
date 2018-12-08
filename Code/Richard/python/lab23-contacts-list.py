"""
author: Richard Sherman
2018-12-07
lab23-contacts-list.py, manipulates data from .csv file and implements a CRUD
"""

# the 'contacts list' here is just some data from the World Bank

import csv
import pandas as pd

with open('world_data.csv', 'r') as file:
    lines = file.read().split('\n')

# first line of file contains variable names (dict keys)
varnames = (lines[0].split(','))
print(varnames)

# split all lines into lists of values
for i in range(len(lines)):
    lines[i] = (lines[i].split(','))
# print(lines)
# print(lines[0], lines[1])


# construct list of dicts with keys and values
data_list = []
for i in range(1, len(lines)):
    data_list.append(dict(zip(varnames, lines[i])))
print(data_list)        # working ok, too big to see
print(data_list[0])     # working ok
print(data_list[1])     # working ok
print(data_list[2])     # working ok
print(data_list[-1])    # working ok

# how to access elements of dicts?
print(data_list[1]['Urban Population'])     # working ok

# want to destring and round numerical figures:
# single example looks like this:
data_list[1]['Maternal Mortality Rate'] = int(data_list[1]['Maternal Mortality Rate'])
print(data_list[1])     # working ok

# # now destring and round all numerical values:  # not working
# for i in range(len(data_list)):
#     data_list[i]['Maternal Mortality Rate'] = int(data_list[i]['Maternal Mortality Rate'])
#     data_list[i]['Urban Population'] = float(data_list[i]['Urban Population'])
#     data_list[i]['GDP Per Capita'] = round(float(data_list[i]['GDP Per Capita']), 2)

# alternative method using csv module
# not working yet
with open('world_data.csv', 'r', newline='\n') as file:
    fieldnames = ['Country Name', 'Country Code', 'Maternal Mortality Rate', 'Urban Population', 'GDP Per Capita']
    world_data = csv.DictReader(file, fieldnames=fieldnames)
    dict_list = []
    for row in world_data:
        dict_list.append(row)
print(dict_list)

# alternative method using pandas
world_data = pd.read_csv('world_data.csv')

# implement a CRUD
