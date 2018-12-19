data = [] #blank list
lines = open('contacts.csv').read().split('\n')
while '' in lines:
    lines.remove('')
for line in lines:
    data.append(line.split(',')) #filling list with csv file information

key_list = data.pop(0) #seperating keys from data

contacts = []
for in_list in data:

    contact = {}
    for i in range(len(key_list)):
        contact[key_list[i]] = in_list[i]
    contacts.append(contact)

#adding a contact
new_contact_dict = {}
new_contact = []
for key in key_list:
    value = input('what is new contacts '+key+'?')
    new_contact.append(value)
for i in range(len(key_list)):
    new_contact_dict[key_list[i]] = new_contact[i]
contacts.append(new_contact_dict)

print(new_contact)

print(contacts)

#finding a contact

name_search = input('who are you looking for?\n')

for i in range(len(contacts)):
    for j in contacts[i]:
        if j == 'name' and (contacts[i]['name']) == name_search:
            print(contacts[i])

#deleting a contact

contact_delete = input('who are you sick of?\n')

for i in range(len(contacts)):
    for j in contacts[i]:
        if j == 'name' and (contacts[i]['name']) == contact_delete:
            contacts.pop(i)
print(contacts)

#update a contacts info
# update = input('who would you like to input?\n')
# update_which_key = ''
# for i in range(len(contacts)):
#     for j in contacts[i]:
#         if j == 'name' and (contacts[i]['name']) == update:
#             update_which_key = input('would you like to change name, fav_food, fav_color, or animal?\n')
#             if update_which_key == 'name':
#
#             else:
#                 if update_which_key == 'fav_food':
#
#             else:
#                 if update_which_key == 'fav_color':
#
#             else:
#                 if update_which_key == 'animal':