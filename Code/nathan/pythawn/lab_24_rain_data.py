

import re
import string


def average_rainfall(data):
    total = 0
    for tuple in data:
        total += tuple[1]
    return total / len(data)





with open('rain_data.txt') as file:
    rain_data = file.read()

rain_data = re.findall('\d{2}-\w{3}-\d{4}\s+\d+', rain_data)

data = []
for row in rain_data:
    row = row.split()
    date = row[0] # todo: convert to datetime
    daily_total = row[1] # todo: convert to int
    daily_total = int(daily_total)*0.01

    data.append((date, daily_total))

average = average_rainfall(data)
print(f'The average rainfall is {round(average, 4)} inches')

