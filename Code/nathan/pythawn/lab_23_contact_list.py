data = [] #blank list
lines = open('contacts.csv').read().split('\n')
while '' in lines:
    lines.remove('')
for line in lines:
    data.append(line.split(',')) #filling list with csv file information


key_list = data.pop(0) #seperating keys from data

contacts = []
for in_list in data:

    # contact = {'name': in_list[0], 'fav_color': in_list[1], ...}
    # contact = {key_list[0]: in_list[0], key_list[1]: in_list[1], ...}

    contact = {}
    for i in range(len(key_list)):
        contact[key_list[i]] = in_list[i]
    contacts.append(contact)

print(contacts)