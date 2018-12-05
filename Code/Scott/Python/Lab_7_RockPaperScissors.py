#lab_7_RockPaperScissors
import random
options_list = ['rock', 'paper', 'scissors']
while True:
    response = random.choice(options_list)
    user_choice = input('Ok choose: rock, paper, or scissors? Or type "quit" if you want to end the game.')
    while user_choice not in ['rock', 'paper', 'scissors', 'quit']:
        user_choice = input('Come on: rock, paper, or scissors? Or type "quit" if you want to end the game.')

    if user_choice == options_list[0] and response == options_list[1]:
        print(f'{response}! Oops, you lost')
    elif user_choice == options_list[1] and response == options_list[2]:
        print(f'{response}! Oops, you lost')
    elif user_choice == options_list[2] and response == options_list[0]:
        print(f'{response}! Oops, you lost')
    elif user_choice == options_list[1] and response == options_list[0]:
        print(f'{response}.' + 'Wow, You win.')
    elif user_choice == options_list[2] and response == options_list[1]:
        print(f'{response}.' + 'Wow, You win.')
    elif user_choice == options_list[0] and response == options_list[2]:
        print(f'{response}.' + 'Wow, You win.')
    elif user_choice == response:
        print(f'{response}.' + 'Looks like we tied')
    elif user_choice == 'quit':
        break



#catch_not_cat.py
# while True:
#     cat_string = input("Please type cat >")
#     if cat_string == 'cat':
#         break

# dog_string = 5
# while dog_string != 'dog': #If the answer isn't correct, repeat with "True"
#     dog_string = input("Please type dog >")

# print(user_choice)
# print(response)
#'paper' > 'rock'
#'rock' > 'scissors'
#'scissors' > 'paper'
# if user_choice > response:
#     print(f'{response}.' +'Wow, You win.')
# if user_choice < response:
#     print(f'{response}.'+'Oops, You lost')
# if user_choice == response:
#     print(f'{response}.' +'Looks like we tied')
