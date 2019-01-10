import random

width = 9  # the width of the board
height = 9  # the height of the board
kill_count = 0
health = 3



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
    board[enemy_i][enemy_j] = '♿'

# loop until the user says 'done' or dies
weapons = [('1', '[1]six shooter')]
enemy_weapons = ['1', '2', '3']
coin = ['h', 't']
die = ['1', '2', '3', '4']

while True:
    #check kill counter and weapons counter to decide whether to add an upgraded weapon
    if kill_count == 1 and len(weapons) == 1:
        weapons.append(('2', '[2]sword'))
        print('you earned a sword')
    if kill_count == 2 and len(weapons) == 2:
        weapons.append(('3', '[3]ray gun'))
        print('congrats, you got a ray gun')
    if kill_count == 3 and len(weapons) == 3:
        weapons.append(('4', '[4]kindness'))
        print('you have learned kindness')
        health += 1

    #print health level and kill count everytime a command is made
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

    if board[player_i][player_j] == '♿':
        print('you\'ve encountered an enemy!')
        weapon_choice = input('choose a weapon:' + '\n\t'.join([weapon[1] for weapon in weapons]))
        enemy_weapon = random.choice(enemy_weapons)
        coin_flip = random.choice(coin)
        die_roll = random.choice(die)
        if weapon_choice == '1' and enemy_weapon == '1':
            if coin_flip == 't':
                board[player_i][player_j] = ' '  # remove the enemy from the board
                kill_count += 1
                print('a revolver always does the trick')
            else:
                if coin_flip == 'h':
                    health -= 1
                    print('oh no')
        elif weapon_choice == '1' and enemy_weapon == '2':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('sweet style')
            else:
                if coin_flip == 'h':
                    health -= 1
                    print('oh no')
        elif weapon_choice == '1' and enemy_weapon == '3':
            health -= 1
            print('oh no')
        elif weapon_choice == '2' and enemy_weapon == '1':
            board[player_i][player_j] = ' '  # remove the enemy from the board
            kill_count += 1
            print('sweet style')
        elif weapon_choice == '2' and enemy_weapon == '2':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('awesome swordsmanship')
            else:
                if coin_flip == 'h':
                    health -= 1
                    print('oh no')

        elif weapon_choice == '2' and enemy_weapon == '3':
            health -= 1
            print('oh no')
        elif weapon_choice == '3' and enemy_weapon == '1':
            board[player_i][player_j] = ' '  # remove the enemy from the board
            kill_count += 1
            print('sweet style')
        elif weapon_choice == '3' and enemy_weapon == '2':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('sweet style, ray gun does the trick')
            else:
                if coin_flip == 'h':
                    health -= 1
                    print('oh no')
        elif weapon_choice == '3' and enemy_weapon == '3':
            if coin_flip == 't':
                board[player_i][player_j] = ' '
                kill_count += 1
                print('sweet style')
            else:
                if coin_flip == 'h':
                    health -= 1
                    print('oh no')
        elif weapon_choice == '4' and enemy_weapon == '1':
            if die_roll == '4':
                health -= 1
                print('oh no')
            else:
                if die_roll != '4':
                    board[player_i][player_j] = ' '
                    kill_count += 1
                    print('sweet style')
        elif weapon_choice == '4' and enemy_weapon == '2':
            if die_roll == '4':
                health -= 1
                print('oh no')
            else:
                if die_roll != '4':
                    board[player_i][player_j] = ' '
                    kill_count += 1
                    print('hell yea')
        elif weapon_choice == '4' and enemy_weapon == '3':
            if die_roll == '4':
                health -= 1
                print('oh no')
            else:
                if die_roll != '4':
                    board[player_i][player_j] = ' '
                    kill_count += 1
                    print('hell yea')



            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('⛄', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
    if health <= 0:
        print('you have reached an untimely death')
        print('''                               ,-'   ,"",
                                     / / ,-'.-'
                           _,..-----+-".".-'_,..
                   ,...,."'             `--.---'
                 /,..,'                     `.
               ,'  .'                         `.
              j   /                             `.
              |  /,----._           ,.----.       .
             ,  j    _   \        .'  .,   `.     |
           ,'   |        |  ____  |         | ."--+,^.
          /     |`-....-',-'    `._`--....-' _/      |
         /      |     _,'          `--..__  `        '
        j       | ,-"'    `    .'         `. `        `.
        |        .\                        /  |         \
        |         `\                     ,'   |          \
        |          |                    |   ,-|           `.
        .         ,'                    |-"'  |             \
         \       /                      `.    |              .
          ` /  ,'                        |    `              |
           /  /                          |     \             |
          /  |                           |      \           /
         /   |                           |       `.       _,
        .     .                         .'         `.__,.',.----,
        |      `.                     ,'             .-""      /
        |        `._               _.'               |        /
        |           `---.......,--"                  |      ,'
        '                                            '    ,'
         \                                          /   ,'
          \                                        /  ,'
           \                                      / ,'
            `.                                   ,+'
              >.                               ,'
          _.-'  `-.._                      _,-'-._
        ,__          `",-............,.---"       `.
           \..---. _,-'            ,'               `.
                  "                '..,--.___,-"""---' mh''')

        break
    if kill_count == 6:
        print('Enemies Cleared')
        break

