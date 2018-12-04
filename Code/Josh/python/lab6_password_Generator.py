import random
import string
length = int(input('how long would you like your password to be?\n'))
character = string.ascii_letters + string.digits
password = 0
new_pass = ''
while password < length:
    new_pass += random.choice(character)
    password += 1
print(f'{new_pass}')
