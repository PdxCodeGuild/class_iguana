import requests
import re
import datetime

rain = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain').content
print(rain)
data = re.findall('(\d{2}-\w{3}-\d{4}) +(\d+)', rain)
data = [(parse_date(data[i][0]), int(data[i][1]) * 0.01 * 2.54) for i in range(len(data))]
print(data[0])

