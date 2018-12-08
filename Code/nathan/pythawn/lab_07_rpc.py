import random

intro_txt = input('WE ARE PLAYING ROCK PAPER SCISSORS\n your choices are >r >p or >s\n Press ENTER to continue ')
choices = ['r', 'p', 's']

player_choice = ''
computer_choice = random.choice(choices)
player_choice = input('name your weapon\n >')
if player_choice == 'r' and computer_choice == 'r':
    print('r v r = TIE')
if player_choice == 'r' and computer_choice == 'p':
    print('r v p = LOSE')
if player_choice == 'r' and computer_choice == 's':
    print('r v s = WIN')
if player_choice == 's' and computer_choice == 'p':
    print('s v p = WIN')
if player_choice == 's' and computer_choice == 'r':
    print('s v r = LOSE')
if player_choice == 's' and computer_choice == 's':
    print('s v s = TIE')
if player_choice == 'p' and computer_choice == 'p':
    print('p v p = TIE')
if player_choice == 'p' and computer_choice == 's':
    print('p v s = LOSE')
if player_choice == 'p' and computer_choice == 'r':
    print('p v r = WIN')

