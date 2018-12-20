data = [] #blank list
lines = open('contacts.csv').read().split('\n')
while '' in lines:
    lines.remove('')
for line in lines:
    data.append(line.split(',')) #filling data list with csv file values(info)


key_list = data.pop(0) #seperating keys from data list

contacts = [] #blank list
for in_list in data:
    contact = {} #blank dictionary
    for i in range(len(key_list)): #matching i number of keys to i number of information
        contact[key_list[i]] = in_list[i]
    contacts.append(contact) #adding dictionaries to list

print(contacts)





