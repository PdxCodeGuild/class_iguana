numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = numbers[0]
guess_count = 0

while True:
    guess = int(input('guess a number between 1 and 10 \n >'))
    if guess != numbers[0]:
        guess_count += 1
        print(' guess again ')
        print(guess_count)

    elif guess == numbers[0]:
        guess_count += 1
        print(' good job ')
        print(guess_count)
        break



