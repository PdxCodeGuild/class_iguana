#Lab12_Guess_the_Number.py

import random

x = 11
#x = random.randint(1, 20)
user_input = input("Guess a number between 1 and 20.")
user_input = int(user_input)
count = 0
while True:
    if count != 10:
        if user_input != x:
            count += 1
            user_input = int(input('Nope. Try again.'))
        elif user_input == x:
            print('Good guess. That\'s correct.')
            break
    else:
        print('I\'m sorry. You took too long.')
        break





