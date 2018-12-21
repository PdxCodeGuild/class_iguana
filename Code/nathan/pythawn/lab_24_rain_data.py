import re
import datetime

def average_rainfall(data):
    total = 0
    for tuple in data:
        total += tuple[1]
    return total / len(data)


def most_rain(data):
    rain_fall_list = []
    for tuple in data:
        rain_fall_list.append(tuple[1])
    rain_fall_list = sorted(rain_fall_list)
    rain_fall_list = rain_fall_list[-1]
    for tuple in data:
        if tuple[1] == rain_fall_list:
            return tuple[0].strftime('%d-%b-%Y'), rain_fall_list


def wettest_year(data):
    years = [2001, 2002, 2003, 2004, 2005, 2006]
    total_list = []
    for year in years:
        total = 0
        for tuple in data:
            if tuple[0].year == year:
                total += tuple[1]
        total_list.append(total)
    wet_year = sorted(total_list)[-1]
    for year in years:
        total = 0
        for tuple in data:
            if tuple[0].year == year:
                total += tuple[1]
        if wet_year == total:
            return f'the year that it rained most was {year}, and the annual total was {total} inches'


with open('rain_data.txt') as file:
    rain_data = file.read()

rain_data = re.findall('\d{2}-\w{3}-\d{4}\s+\d+', rain_data)

data = []
for row in rain_data:
    row = row.split()
    date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
    daily_total = row[1]
    daily_total = int(daily_total)*0.01

    data.append((date, daily_total))

average = average_rainfall(data)
print(f'The average daily rainfall is {round(average, 4)} inches')
most_rain_fall = most_rain(data)
print(f'The most rainfall in one day is {most_rain_fall} inches')
most_yearly_rain = wettest_year(data)
print(most_yearly_rain)


