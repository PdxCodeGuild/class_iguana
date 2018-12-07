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
print('\nLet\'s play a game. I\'ll choose a number between 1 and 10 (inclusive), and you try to guess what it is.\nI\'ll tell you if you\'re getting closer or getting farther.')
number = random.randint(1, 10)
print(number)
i = 1
guess = int(input('Try to guess the number I chose.  '))
dist = abs(guess - number)
dist_list = [dist]
while True:
    dist = abs(guess - number)
    dist_list.append(dist)
    if guess == number:
        print(f'Right! you got it in {i} try(ies)!')
        break
    elif i == 1:
        guess = int(input('That\'s not it. Try again.  '))
        i = i + 1
    else:
        if dist_list[i] > dist_list[i-1]:
            guess = int(input('You\'re getting farther. Try again.  '))
        elif dist_list[i] <= dist_list[i-1]:
            guess = int(input('You\'re getting closer. Try again.  '))
        i += 1

#version 5, computer does the guessing
print('\nLet\'s play a game. Choose a number between 1 and 10 (inclusive), I\'ll try to guess what it is.')
guess_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(guess_list)
number = int(input('Please choose a number between 1 and 10, inclusive.  '))
i = 0
while i < 10:
    guess = guess_list[i]
    confirm = input(f'Is {guess} the right number? Please answer y or n:  ')
    if confirm == 'y':
        print('Wow, I got it right!')
        exit()
    elif confirm == 'n':
        i += 1



#version 5, person chooses, computer guesses
print('\nLet\'s play a game. You choose a number between 1 and 10 (inclusive), and I\'ll try to guess what it is.')
number = int(input('Think of a number between one and ten. You can type it in here; I won\'t see it.  '))
print('I think I can get it in fewer than ten tries.')
guess_list = list(range(1, 11))
random.shuffle(guess_list)
i = 0
while i <= 10:
    guess = guess_list[i]
    confirm = input(f'Is {guess} the number? Please type y or n:  ')
    if confirm == 'y':
        print('Great! I got it right!')
        break
    else:
        print('Let me try again.')
        i += 1
