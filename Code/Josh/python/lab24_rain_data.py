import datetime


with open('rain_data.txt', 'r') as file: #opens file
    data = file.read().split('\n') #splits the file into a list w/ each element being the next line of the file or each element represents each day.
data = data[2:]#removing headers from text
data2 = []
for line in data: #going through each line in data
    values = line.split() #taking each line of data and setting it to the variable values
    my_dict = {'date':values[0], 'daily total':values[1]} #creating a dict with the key values date, & daily total taking each element from values and removing the first element (the date) and second value (the daily total) and setting each to my_dict
    data2.append(my_dict)#taking my_dict everytime it grabs the values from line 10 and adding it to the list data2 to create a list of dictionaries
rain_total = 0
days = len(data2)#getting total number of days for data
for dict in data2:#going through the list of dicts
    dict['date'] = datetime.datetime.strptime(dict['date'], '%d-%b-%Y')#converting the date from the dicts and converting the day, month and year into ints and a more human readable format
    dict['daily total'] = int(dict['daily total'])#converting the the daily total to intigers
    rain_total += dict['daily total']#adding each daily total together
mean = round(rain_total / days, 3) #getting mean
variance_sum = 0
print(mean)
for dict in data2:
    rain_variance = (dict['daily total'] - mean) ** 2  #  formula for variance (data point minus the mean) squared
    variance_sum += rain_variance
print(variance_sum)
print(data2[10]['date'].year)


# import datetime
# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016