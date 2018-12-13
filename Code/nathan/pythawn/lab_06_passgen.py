import random
#allows program to understand random

import string
#allows program to give strings
leng = int(input('how long do you want your password?\n>'))
#user input that turns string into integer to determine password length
characters = string.ascii_letters + string.digits
#defines variable characters as pre made list of strings and numbers
password = ''
#defines password variable as the input string
number = 0 #number starts at zero because program does not know password length to start
while number < leng:
    number += 1
    password += random.choice(characters)
#while number is less than length (0 always less than) turns number into input value and assigns it to random charcters
print(password)
#prints random characters based on given length (random password)


