"""
author: Richard Sherman
2018-12-07
lab23-contacts-list.py, manipulates data from .csv file and implements a CRUD
"""

# the 'contacts list' here is just some data from the World Bank

import csv

with open('world_data.csv', 'r') as file:
    lines = file.read().split('\n')
#    print(lines)
 #   print(lines[0])
varnames = (lines[0].split(','))
print(varnames)
data = []
for line in lines[1:]:
    data.append(line.split(','))
print(data)

