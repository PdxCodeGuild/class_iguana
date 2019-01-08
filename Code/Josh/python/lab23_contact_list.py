
def load_contacts():
    with open('lab23_contacts.csv', 'r') as file:
        lines = file.read().split('\n') # taking the open file splitting it into a list and making each new line each element of the list
    key_list = lines.pop(0).split(',')#taking the header of the list and removing it from the variable lines and setting it to it's own variable
    key_list = [key.strip() for key in key_list] # remove whitespace
    contacts = []
    while len(lines) > 0: #running while loop to go through lines
        value_list = lines.pop(0).split(',')#removing the frist element of lines and spliting it into it's own list called value_list spliting each element of the list at commas (should be 3 elements for each new list created)
        name_dict = {}
        for i in range(len(value_list)): # looping though each index of value_list created on line 9
            name_dict[key_list[i]] = value_list[i]#adding to dictionary (name_dict) with the key being from the header list and the value coming from the newly created value_list from line 9
        contacts.append(name_dict)#adding the newly created dictionary to the list contacts
    return contacts

contacts = load_contacts()
print(contacts)


# fancy version - have load_contacts return the headers as well as the contacts
# when creating a new contact, loop over the headers, prompt user


# headers = ['name', 'favorite fruit', 'favorite color']
# person = {}
# for header in headers:
#     input('what is their ' + header + '? ')
#     person.append({header: input})
# print(person)

# asking the user for input to add a new contact or dictionary to the list of contacts that has already been created
def add_contact():
    name = input('What\'s the name to add?\n>>')
    fav_fruit = input('What\'s their favorite fruit to add?\n>>')
    fav_color = input('What\'s their favorite color to add?\n>>')
    contacts.append({'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color})

# add_contact()
# print(contacts)

def get_contact():
    name = input('What name are looking for?\n>>').capitalize()
    for contact in contacts:
        if contact['name'] == name:
            return contact
# print(get_contact())

def update_contact():
    print("\nI'm going to edit your contact for you.")
    edit_contact = (get_contact())
    key_list = list(edit_contact.keys())
    print('What would you like to edit?')
    print(edit_contact)
    for i in range(len(key_list)):
        print(f'For {key_list[i]} enter {i + 1}')
    selection = int(input('>>'))-1
    for i in range(len(contacts)):
        if (contacts[i]['name']) == edit_contact['name']:
            contacts.pop(i)
            break
    edit_contact[key_list[selection]] = input(f'What would you like to change {key_list[selection]} to?\n>>')
    contacts.append(edit_contact)
    print(contacts)








update_contact()

# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of `name`, `favorite fruit`, `favorite color`. Open the CSV, convert the lines of text into a **list of dictionaries**, one dictionary for each user. The text in the header represents the **keys**, the text in the other lines represent the **values**.
#
# Once you've processed the file, your list of contacts will look something like this...
# ```python
# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]
# ```

# my_dict = {}
# my_dict = lines
# print(my_dict)