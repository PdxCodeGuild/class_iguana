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


password_list = []

lc = input('How many lower-case alphabet characters do you need?:\n')
lc = int(lc)
lower_case_portion = ''
for l in range(lc):
    lower_case_portion += random.choice(list(string.ascii_lowercase))
    #password_list.append(random.choice(string.ascii_lowercase))


uc = input('How many upper-case alphabet characters do you need?:\n')
uc = int(uc)
upper_case_portion = ''
for u in range(uc):
    upper_case_portion = upper_case_portion + random.choice(list(string.ascii_uppercase))

num = input('How many numeric characters do you need?:\n')
num = int(num)
numeric_portion = ''
for n in range(num):
    numeric_portion = numeric_portion + random.choice(list(string.digits))

char = input('How many special characters do you need?:\n')
char = int(char)
character_portion = ''
for c in range(char):
    character_portion = character_portion + random.choice(list(string.punctuation))

password_list = list(lower_case_portion) + list(upper_case_portion) + list(numeric_portion) + list(character_portion)

print(password_list) #this will show the list of all of the collected characters in order of their collection; ie, 2 by 2 or 3 by 3
password = ''
for i in range(len(password_list)):
    random_index = random.randint(0, len(password_list)-1) # variable for a randomly selected element (by index). to establish the proper range, use -1 because indexing starts with 0
    print(password_list) #will show the same list as the one above first time through the loop, then each time missing a randomly selected element
    # print(random_index)
    random_element = password_list.pop(random_index) #this is removing whatever element was randomely seclected on line 47 via

    # print(random_element)
    #print()

    password += random_element # add random character to output

    print(password)#this print statement (located here in the loop) will show the password growing by one element at a time.
    print()

print(f'Your new password is {password}')

# random.shuffle(password)




