import re
import string

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
    return rain_fall_list[-1]


with open('rain_data.txt') as file:
    rain_data = file.read()

rain_data = re.findall('\d{2}-\w{3}-\d{4}\s+\d+', rain_data)

data = []
for row in rain_data:
    row = row.split()
    date = row[0] # todo: convert to datetime
    daily_total = row[1]
    daily_total = int(daily_total)*0.01

    data.append((date, daily_total))

print(data)
average = average_rainfall(data)
print(f'The average daily rainfall is {round(average, 4)} inches')
most_rain_fall = most_rain(data)
print(f'The most rainfall in one day is {most_rain_fall} inches')
