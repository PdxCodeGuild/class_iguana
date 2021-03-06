"""
author: Richard Sherman
2018-12-12
lab23-contacts-list.py, manipulates data from .csv file and implements a CRUD
"""

# the 'contacts list' here is just some data from the World Bank

with open('world_data.csv', 'r') as file:
    lines = file.read().split('\n')

# first line of file contains variable names (dict keys)
varnames = lines[0].split(',')
print(f'varnames = {varnames}')

# split all lines into lists of values
for i in range(len(lines)):
    lines[i] = (lines[i].split(','))
print(f'raw data = {lines}')
print(f'first lines: {lines[0], lines[1]}')

# construct list of dicts with keys and values, removing all obs with missing values
data_list = []
for i in range(1, len(lines)):
    if '' in lines[i]:
        continue
    data_list.append(dict(zip(varnames, lines[i])))

print(f'whole data set: {data_list}')        # working ok, too big to see
print(f'first obs: {data_list[0]}]')     # working ok
print(f'second obs: {data_list[1]}')     # working ok
print(f'last obs: {data_list[-1]}')    # working ok
print(f'Maternal Mortality, first obs: {data_list[0]["Maternal Mortality Rate"]}')     # working ok

# destring and round all numerical values:
for i in range(len(data_list)):
    data_list[i]['Maternal Mortality Rate'] = int(data_list[i]['Maternal Mortality Rate'])
    data_list[i]['Urban Population %'] = round(float(data_list[i]['Urban Population %']), 2)
    data_list[i]['GDP Per Capita'] = round(float(data_list[i]['GDP Per Capita']), 2)
print(data_list)

# implement a CRUD
# I will ask for a region, so as not to over-write a country
print('\nNow, let\'s add a region to the data set.')
region = input('Please enter the region:  ')
region_code = input('Please enter the region code:  ')
mmr = int(input('Please enter the maternal mortality rate:  '))
urbpop = float(input('Please enter the % urban population:  '))
gdp = float(input('Please enter the GDP per capita:  '))

data_list.append({'Country Name' : region, 'Country Code' : region_code, 'Maternal Mortality Rate' : mmr, 'Urban Population %' : urbpop, 'GDP Per Capita' : gdp})
print(data_list[-1])  #working ok

country_query = input('\nPlease enter the name of the country you would like information on:  ')
for i in range(len(data_list)):
    if country_query == data_list[i]['Country Name']:
        print(data_list[i])

# update a field
country_to_update = input('\nPlease enter the name of country for which you would like to update information:  ')
update_field = input('Please tell me which variable you would like to update (Maternal Mortality Rate, Urban Population %, GDP Per Capita:  ')
update_value = int(input('Please tell me the new value:  '))
for i in range(len(data_list)):
    if country_to_update == data_list[i]['Country Name']:
        data_list[i].update({update_field : update_value})
        print(data_list[i])     # to check if update was made

# delete an entry
country_to_delete = input('\nPlease enter the name of country you would like to delete from the data set:  ')
for i in range(len(data_list)):
    if country_to_delete == data_list[i]['Country Name']:
        data_list.pop(i)
        print(data_list)    # to check if deletion was made
        break

# write updated data to file
with open('world_data_updated.csv', 'w+') as outfile:
    fieldnames = ['Country Name', 'Country Code', 'Maternal Mortality Rate', 'GDP Per Capita', 'Urban Population %']
    writer = csv.DictWriter(outfile, fieldnames = fieldnames)

    writer.writeheader()
    for i in range(len(data_list)):
        writer.writerow(data_list[i])

