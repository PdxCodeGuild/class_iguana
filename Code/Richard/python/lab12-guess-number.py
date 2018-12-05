"""author: Richard Sherman
2018-12-4
lab12-guess-number.py, an interactive guessing game involving random numbers"""

import random

print('Let\'s play a game. I\'ll choose a number between 1 and 10 (inclusive), and you try to guess what it is.\nI\'ll give you ten chances!')
number = random.randint(1, 10)
i = 1
guess = int(input('Try to guess the number I chose:  '))
while i < 11:
    if guess == number:
        print(f'Right! you got it in {i} try(ies)!')
        break
    else:
        if i == 10:
            print('Sorry, you didn\'t guess the number.')
            break
        else:
            guess = int(input('That\'s not the number. Try again:  '))
            i += 1

#version 2, unlimited tries
print('\nLet\'s play a game. I\'ll choose a number between 1 and 10 (inclusive), and you try to guess what it is.\nI\'ll give you as many chances as you need!')
number = random.randint(1, 10)
guess = int(input('Try to guess the number I chose.'))
i = 1
while True:
    if guess == number:
        print(f'Right! you got it in {i} try(ies)!')
        break
    else:
        guess = int(input(f'You\'ve guessed {i} time(s). Try again!  '))
        i += 1

#version 3, too high/too low
print('\nLet\'s play a game. I\'ll choose a number between 1 and 10 (inclusive), and you try to guess what it is.\nI\'ll tell you if you\'re too high or too low.')
number = random.randint(1, 10)
guess = int(input('Try to guess the number I chose.'))
i = 1
while True:
    if guess == number:
        print(f'Right! you got it in {i} try(ies)!')
        break
    else:
        if guess > number:
            guess = int(input('That\'s too high. Try again.  '))
        elif guess < number:
            guess = int(input('That\'s too low. Try again.  '))
        i += 1

#version 4, getting closer/getting farther
print('\nLet\'s play a game. I\'ll choose a number between 1 and 10 (inclusive), and you try to guess what it is.\nI\'ll tell you if you\'re too high or too low.')
number = random.randint(1, 10)
i = 1
guess = int(input('Try to guess the number I chose.  '))
guess_list = [guess]
while True:
    dist = abs(guess_list[i] - number)
    if guess_1 == number:
        print(f'Right! you got it in {i} try(ies)!')
        break
    elif i == 1:
        guess = int(input('That\'s not it. Try again.  '))
        guess_list.append(guess)
        i = i + 1
    else:
        if abs(guess_list[i] - number) > abs(guess_list[i - 1] - number):
            guess = int(input('You\'re getting farther away. Try again.  '))
            guess_list.append(guess)
        elif abs(guess_list[i] - number) < abs(guess_list[i - 1] - number):
            guess = int(input('You\'re getting closer. Try again.  '))
            guess_list.append(guess)
        i += 1
