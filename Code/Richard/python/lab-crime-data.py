"""
author: Richard Sherman
2018-12-11
lab-crime-data.py, calculates frequencies of Portland crime data from July 1972 - October 2018
source is https://www.portlandoregon.gov/police/71978
requires minor pre-processing (the variable 'Sex Offences, Nonforcible' has a comma in its name
this was done outside of python)
"""


with open('crime_data.csv', 'r') as file:
    lines = file.read().split('\n')

# first line of file contains variable names (dict keys)
varnames = lines[0].split(',')
# print(f'varnames = {varnames}')

# split all lines into lists of values
for i in range(1, len(lines)):
    lines[i] = (lines[i].split(','))
# print(f'raw data = {lines}')
# print(f'first lines: {lines[0], lines[1]}')


# construct list of dicts with keys and values, removing all obs with missing values
data_list = []
for i in range(1, len(lines)):
    data_list.append(dict(zip(varnames, lines[i])))
data_list.pop(0)        # get rid of the first dict in data_list, which is just the varnames

# print(data_list)

# look at the data
# print(f'first obs: {data_list[0]}]')
# print(f'second obs: {data_list[1]}')
# print(f'next_last obs: {data_list[-2]}')
# print(f'last obs: {data_list[-1]}')     # last obs is empty

data_list = data_list[0:-1]             # remove last obs
# print(f'last obs: {data_list[-1]}')     # check to make sure it's ok


# separate month/day/year from e.g. 12/11/2018
for i in range(len(data_list)):
    data_list[i]['Occur Month'], data_list[i]['Occur Day'], data_list[i]['Occur Year'] = data_list[i]['Occur Date'].split('/')

# look at the data again
print(f'first obs: {data_list[0]}')
# print(f'last obs: {data_list[-1]}')
# print(f'1001th obs: {data_list[1001]}')
# print(f'-1001th obs: {data_list[-1001]}')


# count up crimes by a key, e.g. 'Offence Type' or 'Neighborhood'
def get_count(key):
    count_dict = {}
    for i in range(len(data_list)):
        val = data_list[i][key]
        count_dict[val] = count_dict.get(val, 0) + 1
#    print(count_dict)
    return count_dict

# get_count('Offense Type')
# get_count('Occur Year')

# sorts a dict by values, used here to sort the result of get_count(key)
def count_freq(dict):
    items = list(dict.items())
    items.sort(key=lambda tup: tup[1], reverse=True)
#    print(items)
    return items

print('\n')
print(f'The top ten crime types are: {count_freq(get_count("Offense Type"))[0:9]}')
print(f'The top ten crime years are: {count_freq(get_count("Occur Year"))[0:9]}')
print(f'The top ten crime neighborhoods are {count_freq(get_count("Neighborhood"))[0:9]}')
print(f'The top ten crime months are {count_freq(get_count("Occur Month"))[0:9]}')

# # alternatively:
# crime_type = get_count('Offence Type')
# crime_year = get_count('Offence Year')
# crime_hood = get_count('Neighborhood')
# crime_month = get_count('Occur Month')
#
# print(f'The top ten crime types are: {crime_type[0:9]}')
# print(f'The top ten crime years are: {crime_year[0:9]}')
# print(f'The top ten crime neighborhoods are: {crime_hood[0:9]}')
# print(f'The top ten crime months are: {crime_month[0:9]}')

# todo: get frequencies of e.g. Offence Type by Occur Year, etc.