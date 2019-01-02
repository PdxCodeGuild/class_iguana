#Lab 23 version 3. Contact List
#When REPL loop finishes, write the updated contact info to the CSV file to be saved.
# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.

def add_contact(data_dict_list):
    added_person = []
    added_data = input('So you would like to join this club, huh? Let\'s see, what is your first and last name?\n ')
    added_person.append(added_data)
    added_data = input('Favorite fruit? \n')
    added_person.append(added_data)
    added_data = input('Favorite color: \n')
    added_person.append(added_data)
    added_data = input('What kind of dog do you have? If you don\'t have one you cannot be in this club. \n')
    added_person.append(added_data)
    added_data = input('In what city do you reside? \n')
    added_person.append(added_data)
    added_data = input('State: \n')
    added_person.append(added_data)
    added_data = input('Car \n')
    added_person.append(added_data)

    add_person_dict = {}
    for i in range(len(headers)): # iterate over the columns (again)
        add_person_dict[headers[i]] = added_person[i]
    data_dict_list.append(add_person_dict)

# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

def retreive_record(data_dict_list):
    lookup_name = input('Provide the first and last name of the person you would like to look up. \n')
    response = None
    for i in range(len(data_dict_list)):
        if lookup_name == data_dict_list[i]['Name']:
            response = data_dict_list[i]
            break
    if response is None:
        print(f'Sorry, {lookup_name} is not on the list.')
    else:
        for piece in data_dict_list[i].values():
            print(piece)
        quit()   #quitting here, otherwise the fileIO piece will run without anything updated

# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

def update_record(data_dict_list):
    lookup_name = input('Provide the first and last name of the person you would like to look up. \n')
    update_this = input('What info would you like to update? \n')
    update_info = input('What should it be updated to? \n')

    for i in range(len(data_dict_list)):
        if lookup_name == data_dict_list[i]['Name']:
            data_dict_list[i][update_this] = update_info

# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

def del_record(data_dict_list):
    remove_name = input('Please enter the first and last name of the person who should be removed from this club. \n ')
    for i in range(len(data_dict_list)):
        if remove_name == data_dict_list[i]['Name']:
            del data_dict_list[i]

    # print(data_dict_list)

with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
# print(lines)

# list of dictionaries

data_list = []
for line in lines:
    if line == '':
        continue
    line = line.split(',')
    data_list.append(line)

headers = data_list.pop(0)
data_dict_list = []
for row in data_list:  # iterate over the rows
    data_dict = {}
    for i in range(len(headers)):  # iterate over the columns
        data_dict[headers[i]] = row[i]
    data_dict_list.append(data_dict)

# print(data_dict_list)

selection = input('What would you like to do with this contact list(type the appropriate letter)?'
                  ' Add a contact? (type a), retrieve a record (type b), update a contact (type c), or delete a contact (type d)')

if selection == 'a':
    add_contact(data_dict_list)
elif selection == 'b':
    retreive_record(data_dict_list)
elif selection == 'c':
    update_record(data_dict_list)
elif selection == 'd':
    del_record(data_dict_list)



# output_line =''+','.join(headers)
# output_line += '\n'

lines = ','.join(headers) + '\n'
for row in data_dict_list:
    output_line = ''
    for item in row:
        output_line += row[item] + ','
    lines += output_line + '\n'
    # print(output_line)
        # output_strings.append(output)
print(lines)

# print(output_line)
with open('contact_list.csv', 'w') as contacts_file:
    contacts_file.write(lines)

