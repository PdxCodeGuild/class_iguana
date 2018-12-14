

def create_contact():
    new_contact = {}
    for i, item in enumerate(headers):
        new_contact[headers[i]] = input(f'Enter the {headers[i]}: ')
    contacts.append(new_contact)
    print(f'\nNew Contact created for {new_contact["first_name"]} {new_contact["last_name"]}!\n')

def no_contact_found():
    choice = input('Contact does not exist. Would you like to create one? y/n: ')
    if choice == 'y':
        create_contact()

def get_contact_by_last():
    last_name = input('Enter the last name of the contact: ')
    for i, contact in enumerate(contacts):
        if contact['last_name'] == last_name:
            return i 
        else:
            continue
    no_contact_found()


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

headers = lines[0].split(',')       # Get the headers from the csv file
contacts = []

for i in range(1, len(lines)):      # Split up the file into a list of dicts containing the contact info for each person
    contact = {}
    line = lines[i].split(',')
    for j, field in enumerate(line):
        contact[headers[j]] = field 
    
    contacts.append(contact)

while True:
    response = (input('\nWhat would you like to do with your contacts list?\nEnter "C" to create a new contact, "V" to view a contact,' +
                    '"U" to update a contact, or "D" to delete a contact: ')).lower()
# Create
    if response == 'c':
        create_contact()
# Delete
    elif response == 'd':
        index = get_contact_by_last()
        if index is not None:
            contacts.pop(index)
            print('Contact deleted!')
# Update
    elif response == 'u':
        index = get_contact_by_last()
        if index is not None:
            try:
                edit_field = int(input('\n0: First Name\n1: Last Name\n2: Address\n3: City\n4: County\n5: State\n' +
                            '6: Zip Code\n7: Phone Number\n8: Email\n\nEnter a number for the field to edit: '))
            except ValueError:
                print('Not a valid option')
                quit()
            update_contact = contacts[index]
            update = input(f'What would you like to change the {headers[edit_field]} to? ')
            update_contact[headers[edit_field]] = update
            print(f'{headers[edit_field]} updated to {update_contact[headers[edit_field]]}')
# View
    elif response == 'v':
        index = get_contact_by_last()
        if index is not None:
            print(contacts[index])

    else:
        print('Not a valid input')

    run = input('Would you like to perform another operation? Enter q to quit, any other to continue: ').lower()

    if run == 'q':
        break

# Create the 'save' string by joining back the headers and all contacts
save = ''+','.join(headers) 
save += '\n'
for i, people in enumerate(contacts):
    for j in range(len(people)):
        save += people[headers[j]]  
        if j != len(people) - 1:
            save += ','
    if i != len(contacts) - 1:
        save +='\n'

with open('contacts.csv', 'w') as file:
    file.write(save)

print('Contacts saved! Goodbye.')