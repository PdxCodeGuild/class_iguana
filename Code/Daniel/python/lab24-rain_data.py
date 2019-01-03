import re
import datetime
import matplotlib.pyplot as plt


with open('hayden_island.txt', 'r') as file:
    data = file.read()#.split('\n')            

data2 = []
year_vals = {}

# # Removes non pertinent information and creates a list of tuples containing the date and daily total
# for line in data:
#     line = re.split('\s+', line)
#     try:
#         date = datetime.datetime.strptime(line[0], '%d-%b-%Y')
#         if str(date.year) in year_vals:                         # Gets a dict with the year as key and the total sum of daily vals as values
#             year_vals[str(date.year)] += int(line[1])
#         else:
#             year_vals[str(date.year)] = int(line[1])
#     except ValueError:
#         continue
#     data2.append((line[0], line[1]))
    

reg = '(\d{2}-\w+-\d{4})\s+(\d+)'
data2 = re.findall(reg, data)


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

# # max year
# sorted_years = sorted(year_vals, key=year_vals.__getitem__, reverse=True)
# max_year = sorted_years[0]

years = {}
for date in data2:
    year = date[0].split('-')[2]
    if year in years:
        years[year][0] += int(date[1])
        years[year][1] += 1
    else:
       years[year] = [int(date[1]), 1]

max_year = ('',0) 
for year in years:
    avg = years[year][0]/years[year][1]
    if avg > max_year[1]:
        max_year = (year, avg) 


print(f'\nMean: {mean}\nVariance: {var}')
print(f'The day with the most rain was {max_day[0]} with {max_day[1]}')
print(f'The year with the most rain on average was {max_year[0]} with {max_year[1]} recorded over {years[max_year[0]][1]} days\n')

# # get values for graph
# years_g = list(years.keys())
# vals_g = list(years.values())

years_g = []
vals_g = []
for year in years:
    years_g.append(str(year))
    vals_g.append(years[year][0])


# graph of total rainfall by year
plt.plot(years_g, vals_g)
plt.show()
plt.close()

