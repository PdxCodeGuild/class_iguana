def contact_add(contacts, key_list):
    new_contact_dict = {}
    new_contact = []
    for key in key_list:
        value = input('what is new contacts ' + key + '?')
        new_contact.append(value)
    for i in range(len(key_list)):
            new_contact_dict[key_list[i]] = new_contact[i]
    contacts.append(new_contact_dict)
    return new_contact_dict


def name_search(contacts):
    name_search = input('who are you looking for?\n')
    for i in range(len(contacts)):
        for j in contacts[i]:
            if j == 'name' and (contacts[i]['name']) == name_search:
                return contacts[i]


def contact_delete(contacts):
    contact_delete = input('who are you sick of?\n')
    for i in range(len(contacts)):
        for j in contacts[i]:
            if j == 'name' and (contacts[i]['name']) == contact_delete:
                contacts.pop(i)
    return contacts


def update_info(contacts, key_list):
    update = input('who would you like to edit?\n')
    key_select = input(f' what would you like to change {key_list}')
    changed_key = input('what is the new information')
    for i in range(len(contacts)):
        for j in contacts[i]:
            if j == 'name' and (contacts[i]['name']) == update:
                contacts[i][key_select] = changed_key
            if key_select not in key_list:
                print('not a valid key')
    return contacts


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

while True:
    contact_command = input('would you like to: (add contact, view contact, edit contact, delete contact) **type done when done**\n>').lower()
    if contact_command == 'add contact':
        print(contact_add(contacts, key_list))
    elif contact_command == 'view contact':
        print(name_search(contacts))
    elif contact_command == 'edit contact':
        print(update_info(contacts, key_list))
    elif contact_command == 'delete contact':
        print(contact_delete(contacts))
    elif contact_command == 'done':
        break

