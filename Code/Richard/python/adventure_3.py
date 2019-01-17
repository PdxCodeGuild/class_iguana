"""
author: Richard Sherman
2019-01-09
adventure.py, a simple game played in the terminal
A player encounters some other beings and interacts with them, with towns and forests.
The player seeks food by searching towns and forests and/or stealing from other beings.
The other beings can be helpful in finding food, and can pose dangers of their own.

"""

import random

# set up classes for the game board and the things on it, including the player

class Thing:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

class Player(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '👤')
        self.qualities = qualities
    def __repr__(self):
        return f'Player at {self.location_i}, {self.location_j}'

class Dog(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🐕')
        self.qualities = qualities
    def __repr__(self):
        return f'Dog at {self.location_i}, {self.location_j}'

class Cat(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '😸')
        self.qualities = qualities
    def __repr__(self):
        return f'Cat at {self.location_i}, {self.location_j}'

class Scholar(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '📜')
        self.qualities = qualities
    def __repr__(self):
        return f'Scholar at {self.location_i}, {self.location_j}'

class Crocodile(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🐊')
        self.qualities = qualities
    def __repr__(self):
        return f'Crocodile at {self.location_i}, {self.location_j}'

class Thief(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🦹️')
        self.qualities = qualities
    def __repr__(self):
        return f'Thief at {self.location_i}, {self.location_j}'

class Forest(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🌲')
        self.qualities = qualities
    def __repr__(self):
        return f'Forest at {self.location_i}, {self.location_j}'

class Town(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🏠')
        self.qualities = qualities
    def __repr__(self):
        return f'Town at {self.location_i}, {self.location_j}'

class Companion(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '')
        self.qualities = qualities
    def __repr__(self):
        return 'No companion'


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def print(self, things):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(things)):
                    if things[k].location_i == i and things[k].location_j == j:
                        print(' ' + things[k].character, end='')
                        break
                else:
                    print('  ', end='')
            print()

# instantiate all the objects and give them qualities
            
board = Board(10, 10)

pi, pj = board.random_location()

companion = Companion(pi, pj, qualities = {'hunger' : 0,
                                       'loyalty' : 0,
                                       'cuteness' : 0,
                                       'courage' :  0,
                                       'smarts' : 0,
                                       'strength' : 0,
                                       'food' : 0,
                                        'viciousness' : 0
                                       })

player = Player(pi, pj, qualities = {'hunger' : random.randint(1, 10),
                                       'loyalty' : random.randint(0, 5) / 10,
                                       'cuteness' : 0,
                                       'courage' :  random.randint(0, 10),
                                       'smarts' : 10,
                                       'strength' : random.randint(0, 10),
                                       'food' : random.randint(1, 10),
                                       'companion' : companion,
                                        'viciousness' : 0
                                       })


things = [player]

# things are located at thing.location_i, thing.location_j
# collect them in dictionaries so that they can be referred to in play of the game

num = 7

dog_dict = {}
for i in range(num):
    dogi, dogj = board.random_location()
    dog = Dog(dogi, dogj, qualities = {'hunger': random.randint(1, 10),
                               'loyalty': 0.7,
                               'cuteness': random.randint(0,10),
                               'courage' : 10,
                               'smarts' : random.randint(0,10),
                               'strength' : random.randint(0,10),
                               'food' : random.randint(0, 10),
                                'viciousness': 0
                               })
    dog_dict[(dogi, dogj)] = dog
    things.append(dog)

cat_dict = {}
for i in range(num):
    cati, catj = board.random_location()
    cat = Cat(cati, catj, qualities = {'hunger' : random.randint(1, 10),
                                   'loyalty' : 0.3,
                                   'cuteness' :  random.randint(5, 10),
                                   'courage' : random.randint(0, 10),
                                   'smarts' : random.randint(0, 10),
                                   'strength' : random.randint(0, 10),
                                   'food' : random.randint(0, 10),
                                    'viciousness' : 0
                                   })
    cat_dict[(cati, catj)] = cat
    things.append(cat)

scholar_dict = {}
for i in range(num):
    scholari, scholarj = board.random_location()
    scholar = Scholar(scholari, scholarj, qualities = {'hunger' : random.randint(1, 10),
                                       'loyalty' : random.randint(0, 10) / 10,
                                       'cuteness' : 0,
                                       'courage' :  random.randint(0, 10),
                                       'smarts' : 10,
                                       'strength' : random.randint(0, 10),
                                       'food' : random.randint(0, 10),
                                        'viciousness' : 0
                                       })
    scholar_dict[(scholari, scholarj)] = scholar
    things.append(scholar)

croc_dict = {}
for i in range(num):
    croci, crocj = board.random_location()
    crocodile = Crocodile(croci, crocj, qualities = {'hunger' : random.randint(1, 10),
                                                 'loyalty' : 0.3,
                                                 'cuteness' : 0,
                                                 'courage' : 10,
                                                 'smarts' : random.randint(0, 10),
                                                 'strength' : random.randint(5, 10),
                                                 'food' : random.randint(0, 10),
                                                 'viciousness' : random.randint(0, 10)
                                                 })
    croc_dict[(croci, crocj)] = crocodile
    things.append(crocodile)

thief_dict = {}
for i in range(num):
    thiefi, thiefj = board.random_location()
    thief = Thief(thiefi, thiefj, qualities = {'hunger' : random.randint(0, 10),
                                   'loyalty' : 0.3,
                                    'cuteness' : 0,
                                    'courage' : 10,
                                    'smarts' : random.randint(0, 10),
                                    'strength' : random.randint(0, 10),
                                    'food' : random.randint(0, 10),
                                    'viciousness' : random.randint(0, 10)
                                    })
    thief_dict[(thiefi, thiefj)] = thief
    things.append(thief)

forest_dict = {}
for i in range(num):
    foresti, forestj = board.random_location()
    forest = Forest(foresti, forestj, qualities = {'danger' : random.randint(0, 10),
                                    'food' :  random.randint(0, 10),})
    forest_dict[(foresti, forestj)] = forest
    things.append(forest)

town_dict = {}
for i in range(num):
    towni, townj = board.random_location()
    town = Town(towni, townj, qualities = {'complexity' : random.randint(0, 10),
                                       'food' : random.randint(0, 10)})
    town_dict[(towni, townj)] = town
    things.append(town)


# Start play of the game

def move():
    command = input('You can choose to go left (l), right (r), up (u) or down (d): ')  
    if command == 'q':
        exit()  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down

def redraw_board():
    p_i, p_j = player.location_i, player.location_j
    board.print(things)
    player.location_i, player.location_j = p_i, p_j

intro_text = 'In this game, you will travel through a landscape dotted by towns and forests. Along the way you will look for food to sustain your strength. You will encounter others: dogs, cats, crocodiles, scholars, and thieves. Each of them can help you if you choose them as companions. All have special skills that might help add to your own. For example, crocodiles are strong and fearless, while scholars are smart and dogs loyal. A smart, cute cat might help you find food in a town, and even a thief or a crocodile might help you find food in a dangerous forest. But crocs and thieves can be risky companions; you never know when they might turn on you. If you\'re not feeling cooperative, you can try to steal food from a would-be companion--but if they\'re stronger, they\'ll steal food from you out of spite. \n\nFirst, take a moment to find yourself in the landscape. You\'re the blue head-and-shoulders figure. A scholar is represented by a scroll, and a thief is a scary-looking figure. Dogs, cats and crocs look like dogs, cats and crocs. And everyone knows what a town and a forest look like.'

print(intro_text, '\n')
print('You start out with the following qualities:\n')
print(f'{player.qualities.items()}.')


print('Let\'s play. Here\'s the playing board:')

while True:

    board.print(things)

    move()

# set up what happens when a player encounters a dog
        
    if (player.location_i, player.location_j) in dog_dict.keys():
        
        print('You have encountered a dog. The dog is loyal, so it will share food with you generously if you choose it as a companion.')
        print('But the dog is not very smart. You can:')
        print('\t Try to steal the dog\'s food (s)')
        print('\t Bring the dog with you and share its other qualities (b)') 
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 's':
            if dog_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print('The dog has no food! You need to look elsewhere.')
                # redraw_board()
                move()
            elif dog_dict[player.location_i, player.location_j].qualities['strength'] > max(player.qualities['strength'], player.qualities['companion'].qualities['strength']):
                print('The dog is stronger than you. Now you have a dog bite, and the dog stole your food.')
                print(f'Your hunger level is {player.qualities["hunger"]}. You should go find more food.')
                player.qualities['food'] = 0
                redraw_board()
                move()
            else:
                player.qualities['food'] += dog_dict[player.location_i, player.location_j].qualities['food']
                print(f'You stole {dog_dict[player.location_i, player.location_j].qualities["food"]} units of food from the dog. You should probably move on.')
                dog_dict[player.location_i, player.location_j].qualities['food'] = 0
                redraw_board()
                move()
        elif choice == 'b':
            player.qualities['companion'] = dog_dict[player.location_i, player.location_j]
            print('THe dog is now your companion on your journey. The dog has the following qualities:')
            print(f'{dog_dict[player.location_i, player.location_j].qualities.items()}')
            print('Your own qualities are:')
            print(f'{player.qualities.items()}.')
            print('While you travel with the dog, you can draw on whichever qualities are better, yours or the dog\'s.')
            things.remove(dog_dict[player.location_i, player.location_j])
            redraw_board()
            move()
        else:
            move()

# set up what happens when the player encounters a cat:
        
    if (player.location_i, player.location_j) in cat_dict.keys():
        print('You have encountered a cat. The cat is not very loyal, but it is smart and cute.')
        print('You can:')
        print('\t Try to steal the cat\'s food (s)')
        print('\t Bring the cat along with you and share its other qualities (b)')
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 's':
            if cat_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print('The cat has no food! You need to look elsewhere.')
                # redraw_board()
                move()
            elif cat_dict[player.location_i, player.location_j].qualities['strength'] + cat_dict[player.location_i, player.location_j].qualities['smarts'] > max((player.qualities['strength'] + player.qualities['smarts']), (player.qualities['companion'].qualities['strength'] + player.qualities['companion'].qualities['smarts'])):
                print('The cat\'s combination of strength and smarts has defeated you. Now, you are cat-scratched, and the cat stole your food.')
                print(f'Your hunger level is {player.qualities["hunger"]}. You should go find more food.')
                player.qualities['food'] = 0
                redraw_board()
                move()
            else:
                player.qualities['food'] += cat_dict[player.location_i, player.location_j].qualities['food']
                print(f'You stole {cat_dict[player.location_i, player.location_j].qualities["food"]} units of food from the cat. You should probably move on.')
                cat_dict[player.location_i, player.location_j].qualities['food'] = 0
                redraw_board()
                move()
        elif choice == 'b':
            player.qualities['companion'] = cat_dict[player.location_i, player.location_j]
            print('The cat is now your companion on your journey. The cat has the following qualities:')
            print(f'{cat_dict[player.location_i, player.location_j].qualities.items()}')
            print('Your own qualities are:')
            print(f'{player.qualities.items()}.')
            print('While you travel with the cat, you can draw on whichever qualities are better, yours or the cat\'s.')
            things.remove(cat_dict[player.location_i, player.location_j])
            redraw_board()
            move()
        else:
            move()

# set up what happens when the player encounters a scholar
        
    if (player.location_i, player.location_j) in scholar_dict.keys():
        print('You have encountered a scholar. The scholar is not very loyal, but it is very smart.')
        print('You can:')
        print('\t Try to steal the scholar\'s food (s)')
        print('\t Bring the scholar along with you and share its other qualities (b)')
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 's':
            if scholar_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print('The scholar has no food! You need to look elsewhere.')
                redraw_board()
                move()
            elif scholar_dict[player.location_i, player.location_j].qualities['strength'] + scholar_dict[player.location_i, player.location_j].qualities['smarts'] > max((player.qualities['strength'] + player.qualities['smarts']), (player.qualities['companion'].qualities['strength'] + player.qualities['companion'].qualities['smarts'])):
                print('The scholar\'s combination of strength and smarts has defeated you. Now, you are dumbstruck, and the scholar stole your food.')
                print(f'Your hunger level is {player.qualities["hunger"]}. You should go find more food.')
                player.qualities['food'] = 0
                redraw_board()
                move()
            else:
                player.qualities['food'] += scholar_dict[player.location_i, player.location_j].qualities['food']
                print(f'You stole {scholar_dict[player.location_i, player.location_j].qualities["food"]} units of food from the scholar. You should probably move on.')
                scholar_dict[player.location_i, player.location_j].qualities['food'] = 0
                redraw_board()
                move()
        elif choice == 'b':
            player.qualities['companion'] = scholar_dict[player.location_i, player.location_j]
            print('The scholar is now your companion on your journey. The scholar has the following qualities:')
            print(f'{scholar_dict[player.location_i, player.location_j].qualities.items()}')
            print('Your own qualities are:')
            print(f'{player.qualities.items()}.')
            print('While you travel with the scholar, you can draw on whichever qualities are better, yours or the scholar\'s.')
            things.remove(scholar_dict[player.location_i, player.location_j])
            redraw_board()
            move()
        else:
            move()

# set up what happens when a player encounters a crocodile

    if (player.location_i, player.location_j) in croc_dict.keys():
        print('You have encountered a crocodile. The crocodile is very strong, but it can be dangerous.')
        print('You can:')
        print('\t Try to steal the crocodile\'s food (s)')
        print('\t Bring the crocodile along with you and share its other qualities (b)')
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 's':
            if croc_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print('The crocodile has no food! You need to look elsewhere.')
                # redraw_board()
                move()
            elif croc_dict[player.location_i, player.location_j].qualities['strength'] > max(player.qualities['strength'], player.qualities['companion'].qualities['strength']):
                print('The crocidile\'s strength has defeated you. Now, you have crocodile scars, and the crocodile stole your food.')
                print(f'Your hunger level is {player.qualities["hunger"]}. You should go find more food.')
                player.qualities['food'] = 0
                redraw_board()
                move()
            else:
                player.qualities['food'] += croc_dict[player.location_i, player.location_j].qualities['food']
                print(f'You stole {croc_dict[player.location_i, player.location_j].qualities["food"]} units of food from the crocodile. You should probably move on.')
                croc_dict[player.location_i, player.location_j].qualities['food'] = 0
                redraw_board()
                move()
        elif choice == 'b':
            player.qualities['companion'] = croc_dict[player.location_i, player.location_j]
            print('The crocodile is now your companion on your journey. The crocodile has the following qualities:')
            print(f'{croc_dict[player.location_i, player.location_j].qualities.items()}')
            print('Your own qualities are:')
            print(f'{player.qualities.items()}.')
            print('While you travel with the crocodile, you can draw on whichever qualities are better, yours or the crocodile\'s.')
            things.remove(croc_dict[player.location_i, player.location_j])
            redraw_board()
            move()
        else:
            move()

# set up what happens when the player encounters a thief

    if (player.location_i, player.location_j) in thief_dict.keys():
        print('You have encountered a thief. The thief is fearless and strong, but he can be dangerous.')
        print('You can:')
        print('\t Try to steal the thief\'s food (s)')
        print('\t Bring the thief along with you and share its other qualities (b)')
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 's':
            if thief_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print('The thief has no food! You need to look elsewhere.')
                # redraw_board()
                move()
            elif thief_dict[player.location_i, player.location_j].qualities['strength'] > max(player.qualities['strength'], player.qualities['companion'].qualities['strength']):
                print(
                    'The thief\'s strength has defeated you. Now, you are known as an easy mark, and the thief stole your food.')
                print(f'Your hunger level is {player.qualities["hunger"]}. You should go find more food.')
                player.qualities['food'] = 0
                redraw_board()
                move()
            else:
                player.qualities['food'] += thief_dict[player.location_i, player.location_j].qualities['food']
                print(f'You stole {thief_dict[player.location_i, player.location_j].qualities["food"]} units of food from the thief. You should probably move on.')
                thief_dict[player.location_i, player.location_j].qualities['food'] = 0
                redraw_board()
                move()
        elif choice == 'b':
            player.qualities['companion'] = thief_dict[player.location_i, player.location_j]
            print('The thief is now your companion on your journey. The thief has the following qualities:')
            print(f'{thief_dict[player.location_i, player.location_j].qualities.items()}')
            print('Your own qualities are:')
            print(f'{player.qualities.items()}.')
            print('While you travel with the thief, you can draw on whichever qualities are better, yours or the thief\'s.')
            things.remove(thief_dict[player.location_i, player.location_j])
            redraw_board()
            move()
        else:
            move()

# set up what happens when the player enters a town

    if (player.location_i, player.location_j) in town_dict.keys():
        print('You have entered a town. You might find some food here, and your companion (if you have one) will help you. But towns can be complex to navigate; you\'ll need to use your smarts. And searching is hard, so it will cost you and your companion some of your strength.')
        print('You can:')
        print('\t Search around town for food, then eat (h)')
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 'h':
            if town_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print("There\'s no food in this town! You should move on.")
                move()
            elif town_dict[player.location_i, player.location_j].qualities['complexity'] > max(player.qualities['smarts'], player.qualities['companion'].qualities['smarts']) + player.qualities['companion'].qualities['cuteness']:
                print('Sorry, the town is too complex for you. You didn\'t find any food. You should probably move on.')
                move()
            else:
                if player.qualities['companion'].qualities['viciousness'] > 5:
                    print('Your companion ran off with all your food! I told you they might be dangerous! You\'d better move on.')
                    player.qualities['food'] = 0
                    move()
                else:
                    food = town_dict[player.location_i, player.location_j].qualities['food']
                    # player gets a share of food, after sharing with companion
                    player.qualities['food'] += food * (1 - player.qualities['loyalty'])
                    player.qualities['companion'].qualities['food'] += food * (player.qualities['loyalty'])
                    # player gets a share of food from companion
                    to_share = player.qualities['companion'].qualities['food'] * player.qualities['companion'].qualities['loyalty']
                    player.qualities['companion'].qualities['food'] -= to_share
                    # player and companion eat
                    player_to_eat = min(player.qualities['food'] * (1 / player.qualities['hunger'] + 0.1) , player.qualities['food'])
                    player.qualities['hunger'] -= player_to_eat
                    player.qualities['strength'] += player_to_eat - 1
                    companion_to_eat = min(player.qualities['companion'].qualities['food'] * (1 / (player.qualities['companion'].qualities['hunger'] + 0.1)), player.qualities['companion'].qualities['food'])
                    player.qualities['companion'].qualities['food'] -= companion_to_eat
                    player.qualities['companion'].qualities['strength'] += companion_to_eat - 1
                    print(f'You found {food} units of food in the town. After you and your companion shared it, you ate {player_to_eat} units of food.')
                    print('You now have the following qualities:')
                    print(f'{player.qualities.items()}')
                    print('Your companion has the following qualities:')
                    print(f'{player.qualities['companion'].qualities.items()}')
                    print('It\'s time to move on.')
                    move()


# set up what happens when the player enters a forest

    if (player.location_i, player.location_j) in forest_dict.keys():
        print('You have entered a forest. You might find some food here, and your companion (if you have one) will help you. But forests can be dnagerous; you\'ll need to use your courage. And searching is hard, so it will cost you and your companion some of your strength.')
        print('You can:')
        print('\t Search around the forest for food, then eat (h)')
        print('\t Or continue on (l, r, u, d).')
        choice = input('What would you like to do?  ')
        if choice == 'h':
            if forest_dict[player.location_i, player.location_j].qualities['food'] == 0:
                print("There\'s no food in this forest! You should move on.")
                move()
            elif forest_dict[player.location_i, player.location_j].qualities['danger'] > max(player.qualities['courage'], player.qualities['companion'].qualities['courage']):
                print('Sorry, the forest is too dangerous for you. You didn\'t find any food. You should probably move on.')
                move()
            else:
                if player.qualities['companion'].qualities['viciousness'] > 5:
                    print('Your companion ran off with all your food! I told you they might be dangerous! You\'d better move on.')
                    player.qualities['food'] = 0
                    move()
                else:
                    food = forest_dict[player.location_i, player.location_j].qualities['food']
                    # player gets a share of food, after sharing with companion
                    player.qualities['food'] += food * (1 - player.qualities['loyalty'])
                    player.qualities['companion'].qualities['food'] += food * (player.qualities['loyalty'])
                    # player gets a share of food from companion
                    to_share = player.qualities['companion'].qualities['food'] * player.qualities['companion'].qualities['loyalty']
                    player.qualities['companion'].qualities['food'] -= to_share
                    # player and companion eat
                    player_to_eat = min(player.qualities['food'] * (1 / player.qualities['hunger'] + 0.1), player.qualities['food'])
                    player.qualities['hunger'] -= player_to_eat
                    player.qualities['strength'] += player_to_eat - 1
                    companion_to_eat = min(player.qualities['companion'].qualities['food'] * (1 / (player.qualities['companion'].qualities['hunger'] + 0.1)), player.qualities['companion'].qualities['food'])
                    player.qualities['companion'].qualities['food'] -= companion_to_eat
                    player.qualities['companion'].qualities['strength'] += companion_to_eat - 1
                    print(f'You found {food} units of food in the forest. After you and your companion shared it, you ate {player_to_eat} units of food.')
                    print('You now have the following qualities:')
                    print(f'{player.qualities.items()}')
                    print('Your companion has the following qualities:')
                    print(f'{thief_dict[player.location_i, player.location_j].qualities.items()}')
                    print('It\'s time to move on.')
                    move()