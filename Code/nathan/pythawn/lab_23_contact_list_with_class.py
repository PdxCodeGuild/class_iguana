class Contacter:

    def __init__(self, contacts, key_list):
        self.contacts = contacts
        self.key_list = key_list


    def contact_add(self, contacts, key_list):
        new_contact_dict = {}
        new_contact = []
        for key in self.key_list:
            value = input('what is new contacts ' + key + '?')
            new_contact.append(value)
        for i in range(len(self.key_list)):
                new_contact_dict[key_list[i]] = new_contact[i]
        self.contacts.append(new_contact_dict)
        return self.contacts


    def name_search(self, contacts):
        name_search = input('who are you looking for?\n')
        for i in range(len(self.contacts)):
            for j in self.contacts[i]:
                if j == 'name' and (self.contacts[i]['name']) == name_search:
                    return self.contacts[i]


    def contact_delete(self, contacts):
        contact_delete = input('who are you sick of?\n')
        for i in range(len(self.contacts)):
            for j in self.contacts[i]:
                if j == 'name' and (self.contacts[i]['name']) == contact_delete:
                    self.contacts.pop(i)
        return self.contacts


    def update_info(self, contacts, key_list):
        update = input('who would you like to edit?\n')
        key_select = input(f' what would you like to change {self.key_list}')
        changed_key = input('what is the new information')
        for i in range(len(self.contacts)):
            for j in self.contacts[i]:
                if j == 'name' and (self.contacts[i]['name']) == update:
                    self.contacts[i][key_select] = changed_key
                if key_select not in self.key_list:
                    print('not a valid key')
        return self.contacts


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

contacter = Contacter(contacts, key_list)
while True:
    contact_command = input('would you like to: (add contact, view contact, edit contact, delete contact) **type done when done**\n>').lower()
    if contact_command == 'add contact':
        print(contacter.contact_add(contacts, key_list))
    elif contact_command == 'view contact':
        print(contacter.name_search(contacts))
    elif contact_command == 'edit contact':
        print(contacter.update_info(contacts, key_list))
    elif contact_command == 'delete contact':
        print(contacter.contact_delete(contacts))
    elif contact_command == 'done':
        break
