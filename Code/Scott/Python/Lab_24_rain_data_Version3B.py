#Rain Data
import string
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
import requests
import datetime

#for a cool x,y axis: matt suggests taking the average rainfall for each day/year, IOW, find the average rainfall for
#all the january 1st for each year and make that a datapoint...

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

# print(data)

#collect all of the same month/days and their daily totals into 2 different lists. a list of dicts i think. month/day:total
#365 dates and 365 averages

#unique set of days

days = set()     #this is just like starting a list with  = list(),
for row in data:
    dt = datetime.datetime(year=2000, month=row['date'].month, day=row['date'].day) #datetime dates are immutable. Cant drop the year, but we can just make all years the same and therefor irrelevant while collecting uniique days
    days.add(dt)
days = list(days)
days.sort()
# print(days)

data_points = []
daily_totals = []
daily_average = []
for i in range(len(days)):   #outer loop: using i in range because we need to associate indeces between lists. IOW, matche up data_points[0] with daily_totals[0] etc
    day = days[i]
    data_points.append(0)   #ok, this is a little tricky. Because (see comment above) we need to associate indeces, we need to have those actual indeces, otherwise wher would data_points[4] be?
    daily_totals.append(0)     # so we are creating a list of 366 0's because we need the indeces.
    for row in data:
        if day.day == row['date'].day and day.month == row['date'].month: #checking if day and month as represented by datetime parsing is == between days list and the dictionaries in the data set
            data_points[i] += 1     #adding each time a match up happens
            daily_totals[i] += row['daily total']  #adding the relevent total amount from the data dict each time a match happens
    avg_total = daily_totals[i]/data_points[i]  #in the outer loop, calculating the average of each set.
    daily_average.append(avg_total)      #collecting these averages in a list
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
fig = plt.figure()
ax = fig.add_subplot(111)
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''


ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
plt.plot(days,daily_average)
plt.ylabel('rain totals')
plt.xlabel('day of the year')
labels = months
plt.xticks(days, labels, rotation='vertical')
plt.show()


#plt.set_xticks(months)
# print(data_points)
# print(daily_totals)
# print(daily_average)
# print(len(data_points))
# print(len(daily_totals))
# print(len(daily_average))
# avg_daily_total = []
# for row in data:
#
# year_rain_totals = {}

# plt.plot(years,year_average)
# plt.show()

# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# date = datetime.datetime.strptime()


