



with open('rain_data.txt', 'r') as file:
    data = file.read()

print(data)


# import requests
# import datetime

# url = 'https://or.water.usgs.gov/non-usgs/bes/swan_island_pump.rain'
# def get_locations():
#     r = requests.get(url)
#     # locations = re.findall(r'(\w+)\.rain', r.text)
#     # locations.sort()
#     return r
# print(get_locations())
#
# def parse_date(date_str):
#     return datetime.datetime.strptime(date_str, '%d-%b-%Y')



# import datetime
# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016