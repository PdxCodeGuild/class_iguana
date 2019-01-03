import random

width = 9  # the width of the board
height = 9  # the height of the board
kill_count = 0
weapons_count = 1
health = 6

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 6
player_j = 6

# add 4 enemies in random locations
for i in range(6):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# loop until the user says 'done' or dies
weapons = ['1']
enemy_weapons = ['1', '2', '3']
weapons_display = ['[1]six shooter'] #'[2]ray gun', '[3]magnet gun'
coin = ['h', 't']
die = ['1', '2', '3', '4', '5', '6', '7']
while True:
    if kill_count == 1 and weapons_count == 1:
        weapons.append('2')
        weapons_display.append('[2]sword')
        weapons_count += 1
        print('you earned a sword')
    elif kill_count == 2 and weapons_count == 2:
        weapons.append('3')
        weapons_display.append('[3]ray gun')
        weapons_count += 1
        print('congrats, you got a ray gun')
    elif kill_count == 3 and weapons_count == 3:
        weapons.append('4')
        print('you have learned kindness')
        health += 1
        weapons_display.append('[4]kindness')
        weapons_count += 1

    print(f'health: {health}, kill count: {kill_count}')
    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'a':
        player_j -= 1  # move left
    elif command == 'd':
        player_j += 1  # move right
    elif command == 'w':
        player_i -= 1  # move up
    elif command == 's':
        player_i += 1  # move down
    elif command == 'ja':#jumping commands
        player_j -= 3
    elif command == 'jd':
        player_j += 3
    elif command == 'jw':
        player_i -= 3
    elif command == 'js':
        player_i += 3

    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        weapon_choice = input(f'choose a weapon {weapons_display}')
        enemy_weapon = random.choice(enemy_weapons)
        coin_flip = random.choice(coin)
        die_roll = random.choice(die)
        if weapon_choice == '1' and enemy_weapon == '1':
            if coin_flip == 't':
                board[player_i][player_j] = ' '  # remove the enemy from the board
                kill_count += 1
                print('you won the quick draw')
            else:
                if coin_flip == 'h':
                    print('you lost the quick draw')
                    health -= 1
        elif weapon_choice == '1' and enemy_weapon == '2':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('you shot the swordsman')
            else:
                if coin_flip == 'h':
                    print('you lost the quick draw')

            print('you were demolished by the enemies sword')
            health -= 1
        elif weapon_choice == '1' and enemy_weapon == '3':
            print('a six shooter is no match for a ray gun \n you were murked')
            health -= 1
        elif weapon_choice == '2' and enemy_weapon == '1':
            print('the enemy died from your swinging blade')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            kill_count += 1
        elif weapon_choice == '2' and enemy_weapon == '2':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('you won the quick draw')
            else:
                if coin_flip == 'h':
                    print('you lost the quick draw')
                    health -= 1

        elif weapon_choice == '2' and enemy_weapon == '3':
            print('a sword is no match for a ray gun \n you got owned')
            health -= 1
        elif weapon_choice == '3' and enemy_weapon == '1':
            print('the enemy died thanks to your speedy quick lazer')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            kill_count += 1
        elif weapon_choice == '3' and enemy_weapon == '2':
            print('nice')
            board[player_i][player_j] = ' '
            kill_count += 1
        elif weapon_choice == '3' and enemy_weapon == '3':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('you won the quick draw')
            else:
                if coin_flip == 'h':
                    print('you lost the quick draw')
                    health -= 1
        elif weapon_choice == '4' and enemy_weapon == '1':
            if die_roll == '3' or die_roll == '4':
                print('kindness did not win')
                health -= 1
            else:
                if die_roll != '3' or '4':
                    print('kindness killed the enemy')
                    board[player_i][player_j] = ' '
                    kill_count += 1
        elif weapon_choice == '4' and enemy_weapon == '2':
            if die_roll == '3' or die_roll == '4':
                print('kindness did not win')
                health -= 1
            else:
                if die_roll != '3' and die_roll != '4':
                    print('kindness killed the enemy')
                    board[player_i][player_j] = ' '
                    kill_count += 1
        elif weapon_choice == '4' and enemy_weapon == '3':
            if die_roll == '3' or die_roll == '4':
                print('kindness did not win')
                health -= 1
            else:
                if die_roll != '3' and die_roll != '4':
                    print('kindness killed the enemy')
                    board[player_i][player_j] = ' '
                    kill_count += 1

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
    if health <= 0:
        print('you have reached an untimely death')
        break
    if kill_count == 6:
        print('Enemies Cleared')
        break

