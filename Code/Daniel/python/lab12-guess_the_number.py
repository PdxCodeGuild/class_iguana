import random

num_guess = 1
comp_num = random.randint(1, 10)

while True:
    try:
        guess = int(input('Guess the number: '))

        if guess == comp_num:
            print('That\'s right! Took you ' + str(num_guess) + ' guesses.')
            break
        elif guess < 1 or guess > 10:
            print('Not the brightest crayon in the box, huh? It\'s a number 1-10, genius.')
        elif guess > comp_num:
            print('Too high')
        elif guess < comp_num:
            print('Too low')
        else:
            print('Nope! Guess again!')

        num_guess += 1

    except ValueError:
        print('Not a proper guess. I\'m counting that though.')
        num_guess += 1