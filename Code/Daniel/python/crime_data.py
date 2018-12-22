import requests

data_list = [
    'https://raw.githubusercontent.com/PdxCodeGuild/class_ocelot/master/1%20Python/data/crime_incident_data_2011.csv',
    'https://raw.githubusercontent.com/PdxCodeGuild/class_ocelot/master/1%20Python/data/crime_incident_data_2012.csv',
    'https://raw.githubusercontent.com/PdxCodeGuild/class_ocelot/master/1%20Python/data/crime_incident_data_2013.csv',
    'https://raw.githubusercontent.com/PdxCodeGuild/class_ocelot/master/1%20Python/data/crime_incident_data_2014.csv'
]

data = []
for year in data_list:
    response = requests.get(year)
    lines = response.text.split('\n')
    
    del lines[0]

    for line in lines:
        data.append(line.split(','))

    
crime_dict = {}
crime_year = {}
for crime in data:
    if len(crime) > 3:
        year = crime[1].split('/')[2].strip('"')

        if crime[3] in crime_dict:
            crime_dict[crime[3]] +=1
        else:
            crime_dict[crime[3]] = 1
        
        if year in crime_year:
            crime_year[year] += 1
        else:
            crime_year[year] = 1

sorted_crimes = sorted(crime_dict, key=crime_dict.__getitem__)
sorted_years = sorted(crime_year, key=crime_year.__getitem__, reverse = True)

# rare_crime = [off.strip('"')for off in sorted_crimes]
num_off = [f'{off} with {crime_dict[off]} reports' for off in sorted_crimes]


print(f'\nThe most common crime is {sorted_crimes[-1]} with {crime_dict[sorted_crimes[-1]]} reports')
print('\nThe rarest crimes are:')
for off in num_off[:5]:
    print(off)

print(f'\nThe year with the most crime was {sorted_years[0]} with {crime_year[sorted_years[0]]} reports\n')
