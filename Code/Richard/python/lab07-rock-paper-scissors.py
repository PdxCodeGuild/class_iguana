"""Author: Richard Sherman
2018-12-03
lab07-rock-paper-scissors.py, plays an interactive rock-paper-scissors game"""

import random

print('Let\'s play a game of rock-paper-scissors. Remember:\n\t - paper beats rock\n\t - rock beats scissors\n]\t - scissors beats paper')
play_again = 'y'
choices = ['r', 'p', 's']
while play_again == 'y':
    choice = input('Please make a choice of r, p, or s: ')
    computer_choice = random.choice(choices)
    if choice == 'r':
        if computer_choice == 'r':
            print('I chose rock, too. We tied!')
        elif computer_choice == 's':
            print('I chose scissors. You win!')
        elif computer_choice == 'p':
            print('I chose paper. I win!')
    elif choice == 'p':
        if computer_choice == '=r':
            print('I chose rock. You win!')
        elif computer_choice == 's':
            print('I chose scissors. I win!')
        elif computer_choice == 'p':
            print('I chose paper, too. We tied!')
    elif choice == 's':
        if computer_choice == 'r':
            print('I chose rock. I win!')
        elif computer_choice == 's':
            print('I chose scissors. We tied!')
        elif computer_choice == 'p':
            print('I chose paper. You win!')

    play_again = input('Do you want to play again? Please type y or n: ')

if play_again == 'n':
    print('OK, thanks for playing!')