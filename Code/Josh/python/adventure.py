import random


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '§')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☺')


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, j):
        return self.board[j]

    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print(' ', end='')
            print()

def battle():
    player_weapon = input('choose a weapon\ntype k for katana\ntype s for sais\ntype b for bo staff\n>>')
    weapon = ['a katana', 'sais', 'nunchucks', 'no weapon']
    enemy_weapon = random.choice(weapon)

    if player_weapon in ['k', 'K', 'katana'] and enemy_weapon in ['a katana', 'no weapon', 'nunchucks']:
        print(f'Your enemy has {enemy_weapon}')
        print('Your katana skills out matched your enemy, nice job Leonardo')
        entities.remove(enemy)
        enemies.remove(enemy)
    elif player_weapon in ['s', 'S', 'sais'] and enemy_weapon in ['sais', 'no weapon', 'a katana']:
        print(f'Your enemy has {enemy_weapon}')
        print('Your sai skills out matched your enemy, nice job Raphael')
        entities.remove(enemy)
        enemies.remove(enemy)
    elif player_weapon in ['b', 'B', 'bo staff'] and enemy_weapon in ['nunchucks', 'no weapon', 'sais']:
        print(f'Your enemy has {enemy_weapon}')
        print('Your bo staff skills out matched your enemy, nice job Donatello')
        entities.remove(enemy)
        enemies.remove(enemy)
    elif player_weapon in ['b', 'B', 'bo staff'] and enemy_weapon == 'a katana':
        print(f'Your enemy has {enemy_weapon}')
        print('Your enemies katana skills decapitated you\nGAME_OVER')
        exit()
    elif player_weapon in ['s', 'S', 'sais'] and enemy_weapon == 'nunchucks':
        print(f'Your enemy has {enemy_weapon}')
        print('Your enemies nunchuck skills bashed your skull in\nGAME_OVER')
        exit()
    elif player_weapon in ['k', 'K', 'katana'] and enemy_weapon == 'sais':
        print(f'Your enemy has {enemy_weapon}')
        print('Your enemies sai skills have pierced you in the heart\nGAME_OVER')
        exit()
    else:
        print(f'{player_weapon} is not a valid choice')
        battle()




board = Board(10, 10)

pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
enemies = []

for i in range(5):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)

def run(game_counter):
    print(game_counter)
    game_counter += random.randint(0,5)
    if game_counter <= 10:
        print('you narrowly escaped the enemy')
        player.location_i -= 1
        return game_counter
    else:
        game_counter > 10
        print('The enemy shot you in the heart with an arrow\nGAME_OVER')
game_counter = 0
enemy_counter = 0
while True:
    if enemy_counter == 5:
        print('Congratulations you have slain all enemies!! you are a true hero')
        quit()
    board.print(entities)

    command = input('what is your command?')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down

    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            print('you\'ve encountered an enemy!')
            action = input('what will you do?\nattack or run?\n>>')
            # print(action)
            if action == 'attack':
                battle()
                enemy_counter += 1
                break
            if action == 'run':
                game_counter += 1
                game_counter = (run(game_counter))
                break
            else:
                print('you hesitated and were slain\nGAME_OVER')
                exit()

