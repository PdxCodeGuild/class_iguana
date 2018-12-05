#lab6_password_generatory.py
#1. acquire all possible characters
import random
import string
# n = input('How many characters would you like your password to have?:\n')
# n = int(n)
# character_list = list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)
# password = ''
# for c in range(0, n):
#     password = password + random.choice(character_list)
# print(f'Your new password is {password}')


#2. get from user quantities of character types


password_list = []

lc = input('How many lower-case alphabet characters do you need?:\n')
lc = int(lc)
lower_case_portion = ''
for l in range(lc):
    lower_case_portion += random.choice(list(string.ascii_lowercase))
    password_list.append(random.choice(string.ascii_lowercase))


uc = input('How many upper-case alphabet characters do you need?:\n')
uc = int(uc)
upper_case_portion = ''
for u in range(0, uc):
    upper_case_portion = upper_case_portion + random.choice(list(string.ascii_uppercase))

num = input('How many numeric characters do you need?:\n')
num = int(num)
numeric_portion = ''
for n in range(0, num):
    numeric_portion = numeric_portion + random.choice(list(string.digits))

char = input('How many special characters do you need?:\n')
char = int(char)
character_portion = ''
for c in range(0, char):
    character_portion = character_portion + random.choice(list(string.punctuation))

# pull said quantities into a common list and combine with random.choice

password_list = list(lower_case_portion) + list(upper_case_portion) + list(numeric_portion) + list(character_portion)
# password_digits = list(lower_case_portion + upper_case_portion + numeric_portion + character_portion)


# random.shuffle(password)

#    0          1           2
# ['apples', 'bananas', 'pears']


# print(', '.join(['apples', 'bananas', 'pears']))
#
# print(''.join(password))

#print(password_list)
password = ''
for i in range(len(password_list)):
    random_index = random.randint(0, len(password_list)-1)
    #print(password_list)
    #print(random_index)
    random_element = password_list.pop(random_index)

    #print(random_element)
    #print()

    password += random_element

print(f'Your new password is {password}')
#




