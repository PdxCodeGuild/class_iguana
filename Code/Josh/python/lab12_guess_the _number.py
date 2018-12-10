import random
x = random.randint(1,100) #generating the random number for the computer
#print(x)
guess = 0 #setting guess (the counter) to 0
while True: #start of first user's guess while loop
    guess_left = abs(guess - 8)
    if guess == 1:
        break
    user_num = int(input(f'Guess my number from 1 to 100 \n{guess_left} attempt(s) left\n> '))
    guess += 1
    if user_num > x:
        print('That\'s to high')
    if user_num < x:
        print(f'That\'s to low')
    if user_num == x:
        print(f'Wow first guess, {x} is my number, How did you know?!!?')
        break
if user_num == x:
    quit()
while True:

    guess_left = abs(guess - 8)
    last_guess = user_num
    user_num = int(input(f'{guess_left} attempt(s) left\n> '))
    guess += 1
    #print(last_guess), print(user_num)
    if user_num == x:
        print(f'{x} is my number, How did you know?!')
        break
    if guess == 8:
        print(f'Sorry to many guesses the number was {x}')
        break
    if user_num > x and abs(last_guess - x) > abs(user_num - x):
        print(f'you\'re getting warmer {user_num} is to high')
    if user_num > x and abs(last_guess - x) < abs(user_num - x):
        print( f'you\'re getting colder {user_num} is to high')
    if user_num < x and abs(last_guess - x) > abs(user_num - x):
        print(f'you\'re getting warmer {user_num} is to low')
    if user_num < x and abs(last_guess - x) < abs(user_num - x):
        print(f'your\'re getting colder {user_num} is to low')
    if user_num < x and abs(last_guess - x) == abs(user_num - x):
        print(f'{user_num} is to low')
    if user_num > x and abs(last_guess - x) == abs(user_num - x):
        print(f'{user_num} is to high')