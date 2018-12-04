import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
special = '!@#$%^&*()_+><.'
numbers = '0123456789'
password = [] 

print('-' * 50 + '\nPassword Generator\n' + '-' * 50 )

j = True
while j == True:
    try:
        num_lower = int(input('\nHow many lower case letters do you want? '))
        num_upper = int(input('How many upper case letters do you want? '))
        num_special = int(input('How many special characters do you want? '))
        num_numbers =  int(input('How many numbers do you want? '))
        j = False

    except ValueError:
        print('\n---\nPlease enter all numbers\n---\n')
        continue

for i in range(0, num_lower):
    password.append(random.choice(lower))
for i in range(0, num_upper):
    password.append(random.choice(upper))
for i in range(0, num_special):
    password.append(random.choice(special))
for i in range(0, num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
mixed = ''.join(password)

print('Your new password is: ' + mixed)