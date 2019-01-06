#Rain Data
import string
import datetime

def load_file(file):
    with open(file, encoding="utf-8") as rain_data:
        contents = rain_data.read()
    lines = contents.split('\n') # split massive string into lines
    lines = lines[11:] # remove junk at the top of the file


    data = []
    for line in lines: #remember that lines are a bunch of strings, this is iterating down the lines(ie, down the rows)
        values = line.split() # this is splitting the lines(rows) into individual strings (like into columns)
        # print(values)
        if values[1] != '-':
            data_dict = {'date': values[0], 'daily total': values[1]} # while we are in the loop in order to split the lines we can also collect the keys and values of each dictionary (in this case the first two values in each line/row are the values
            data.append(data_dict) #adding each new dictionary to our data list
        else:
            continue
    return data


def parse_data(data):
    for data_dict in data:
        data_dict['date'] = datetime.datetime.strptime(data_dict['date'], '%d-%b-%Y')
        data_dict['daily total'] = int(data_dict['daily total'])

    return data

data = load_file('portland_fire.txt')
data = parse_data(data)

total_days = len(data)
total_rain = 0 # start the collection of the sum/total of the data from the data points
for data_dict in data:
    total_rain += data_dict['daily total'] #need the sum of all data points
rainfall_mean = 1/total_days * total_rain        # calculation for mean now that we have the sum of data points
rainfall_mean = round(rainfall_mean, 3)

print(f'the rainfall mean for this period is {rainfall_mean} tips')

for data_dict in data:
    v_sum = 0
    daily_rain_variance = (data_dict['daily total'] - rainfall_mean) ** 2 # per the formula we need (data point minus the mean) squared

    v_sum += daily_rain_variance
variance = round(v_sum/(total_days - 1), 3)
print(f'The variance in rainfall for this period is {variance} tips')

# day of highest rainfall. Need to find day with no days higher in 'daily total'
daily_inches = []
for data_dict in data:
    daily_inches.append(data_dict['daily total'])
daily_inches.sort()
highest_amount = daily_inches[-1]

for data_dict in data:
    if data_dict['daily total'] == highest_amount:
        print(f"The day with the highest amount of rainfall was {data_dict['date']} with {highest_amount} tips")
    else:
        continue

# for data_dict in data: # need to add days of the same month together and then average.
# make a list of the years and then sort
    #call the years from data and put them in a list
years = []
for item in data:
    if item['date'].year not in years:
        years.append(item['date'].year)

#the list of years is already sorted so I'm going to leave it.
#so now
year_data_points = {}

for data_dict in data:
    year = data_dict['date'].year
    if year in year_data_points:
        year_data_points[year] += 1
    else:
        year_data_points[year] = 1

print(f'year data points are {year_data_points}')

year_rain_totals = {}

for data_dict in data:
    year = data_dict['date'].year
    if year in year_rain_totals:
        year_rain_totals[year] += data_dict['daily total']
    else:
        year_rain_totals[year] = data_dict['daily total']

print(f'year rain totals are {year_rain_totals}')

# average_rainfall = []
year_average = []
for year in year_rain_totals:
    average = year_rain_totals[year]/year_data_points[year]
    year_average.append(average)
print(year_average)

averages = []
for i in range(len(years)):
    # yearly_average = (years[i], year_average[i])
    yearly_average = (year_average[i], years[i])
    averages.append(yearly_average)
print(averages)

averages.sort()
print(averages)

print(f'The year with the highest average rainfall was {averages[-1][1]} with {averages[-1][0]} tips')




# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# date = datetime.datetime.strptime()


