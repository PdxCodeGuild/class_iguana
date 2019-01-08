steps_left = 10
steps_from_home = 35
burgers_eaten = 0
print(f'wow you have had a long day, you are {steps_from_home} steps away from home!')
print(f'you only have {steps_left} steps left in you, a hamburger will give you more energy though( + 15 steps )!')

while True:
    first_move = input('walk to burger store? (-5 steps), yes or no? (if no, you are heading home)\n')

    if first_move == 'yes':
        steps_left -= 5
        steps_left += 15
        steps_from_home += 5
        print(f' that burger was delicious, you have {steps_left} steps left. You are {steps_from_home} steps from home')
        burgers_eaten += 1
        print(f'you have eaten {burgers_eaten} burger(s)')

    elif first_move == 'no':
            steps_from_home -= steps_left
            if steps_from_home <= 0:
                print('yay, you made it home')
                break
            elif steps_from_home > 0:
                print('you ran out of energy and could not make it home')
                break

