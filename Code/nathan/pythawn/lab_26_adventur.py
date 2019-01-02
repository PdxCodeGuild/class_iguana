import random

width = 10  # the width of the board
height = 10  # the height of the board
kill_count = 0

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# loop until the user says 'done' or dies
weapons = ['six shooter', 'ray gun', 'magnet gun']
coin = ['h', 't']
while True:

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

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            weapon_choice = input('choose a weapon (six shooter, ray gun, magnet gun)')
            enemy_weapon = random.choice(weapons)
            coin_flip = random.choice(coin)
            if weapon_choice == 'six shooter' and enemy_weapon == 'six shooter':
                if coin_flip == 't':
                    board[player_i][player_j] = ' '  # remove the enemy from the board
                    kill_count += 1
                    print('you won the quick draw')
                else:
                    if coin_flip == 'h':
                        print('you lost the quick draw')
                        break
            elif weapon_choice == 'six shooter' and enemy_weapon == 'ray gun':
                print('you were demolished by the enemies ray gun')
                break
            elif weapon_choice == 'six shooter' and enemy_weapon == 'magnet gun':
                print('a six shooter is no match for a magnet gun')
                break
            elif weapon_choice == 'ray gun' and enemy_weapon == 'six shooter':
                print('the enemy died from your ray gun attack')
                board[player_i][player_j] = ' '  # remove the enemy from the board
                kill_count += 1
            elif weapon_choice == 'ray gun' and enemy_weapon == 'ray gun':
                if coin_flip == 't':
                    board[player_i][player_j] = ' '
                    kill_count += 1
                    print('you won the quick draw')
                else:
                    if coin_flip == 'h':
                        print('you lost the quick draw')
                        break

            elif weapon_choice == 'ray gun' and enemy_weapon == 'magnet gun':
                print('a ray gun is no match for a magnet gun')
                break
            elif weapon_choice == 'magnet gun' and enemy_weapon == 'six shooter':
                print('the enemy died')
                board[player_i][player_j] = ' '  # remove the enemy from the board
                kill_count += 1
            elif weapon_choice == 'magnet gun' and enemy_weapon == 'ray gun':
                print('nice')
                board[player_i][player_j] = ' '
                kill_count += 1
            elif weapon_choice == 'magnet gun' and enemy_weapon == 'magnet gun':
                if coin_flip == 't':
                    board[player_i][player_j] = ' '
                    kill_count += 1
                    print('you won the quick draw')
                    break
                else:
                    if coin_flip == 'h':
                        print('you lost the quick draw')
                        break

            else:
                print('you hestitated and were slain')
                break

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
    if kill_count == 4:
        print('Enemies Cleared')
        break
