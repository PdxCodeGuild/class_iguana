import random


import string

leng = int(input('how long do you want your password?\n>'))

characters = string.ascii_letters + string.digits

password = ''

number = 0
while number < leng:
    number += 1
    password += random.choice(characters)

print(password)

