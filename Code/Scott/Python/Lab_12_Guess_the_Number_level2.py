#Lab12_Guess_the_Number level 2.py

import random

# x = 11 # used this as a test
x = random.randint(1, 20)
user_input = input("Guess a number between 1 and 20.")
user_input = int(user_input)
count = 0
while True:
        if user_input != x:
            count += 1
            user_input = int(input('Nope. Try again.'))
        elif user_input == x:
            print(f'Good guess. That\'s correct. That took you {count} attempts!')
            break





