import re
import datetime
import matplotlib.pyplot as plt


with open('hayden_island.txt', 'r') as file:
    data = file.read().split('\n')            

data2 = []
year_vals = {}

# Removes non pertinent information and creates a list of tuples containing the date and daily total
for line in data:
    line = re.split('\s+', line)
    try:
        date = datetime.datetime.strptime(line[0], '%d-%b-%Y')
        if str(date.year) in year_vals:                         # Gets a dict with the year as key and the total sum of daily vals as values
            year_vals[str(date.year)] += int(line[1])
        else:
            year_vals[str(date.year)] = int(line[1])
    except ValueError:
        continue
    data2.append((line[0], line[1]))
        

# mean
mean = sum([int(pair[1]) for pair in data2 if pair[1].isdigit()]) / len(data2)

# variance
var = sum([(int(tup[1]) - mean)**2 for tup in data2 if tup[1].isdigit()]) / len(data2)

# max day
max_rain = 0
for tup in data2:
    if int(tup[1]) > max_rain:
        max_rain = int(tup[1])
        max_day = tup

# max year
sorted_years = sorted(year_vals, key=year_vals.__getitem__, reverse=True)
max_year = sorted_years[0]


print(f'Mean: {mean}\nVariance: {var}')
print(f'The day with the most rain was {max_day[0]} with {max_day[1]}')
print(f'The year with the most rain was {max_year} with {year_vals[max_year]}\n')

# get values for graph
years = list(year_vals.keys())
vals = list(year_vals.values())

# graph of total rainfall by year
plt.plot(years, vals)
plt.show()
plt.close()

