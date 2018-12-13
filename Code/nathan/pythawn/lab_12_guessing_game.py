#list of number 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = numbers[0]
#card needed to guess
guess_count = 0 #guess count variable starts at zero
#while loop making user continue guessing until they pick the right number
while True:
    guess = int(input('guess a number between 1 and 10 \n >'))
    if guess != numbers[0]:
        guess_count += 1   #guess count adds one if answer is not correct
        print(' guess again ')
        print(guess_count)

    elif guess == numbers[0]:
        guess_count += 1
        print(' good job ')
        print(guess_count)
        break
#loop breaks if guess is equal to answer


