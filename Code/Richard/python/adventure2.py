import random
import string

class Thing:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

class Player(Thing):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👤')

class Dog(Thing):
    def __init__(self, location_i, location_j, qualities):
        self.location_i = location_i
        super().__init__(location_i, location_j, '🐕')
        self.qualities = qualities

class Cat(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '😸')
        self.qualities = qualities

class Scholar(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '📜')
        self.qualities = qualities

class Crocodile(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🐊')
        self.qualities = qualities

class Thief(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🦹️')
        self.qualities = qualities

class Forest(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🌲')
        self.qualities = qualities

class Town(Thing):
    def __init__(self, location_i, location_j, qualities):
        super().__init__(location_i, location_j, '🏠')
        self.qualities = qualities

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

board = Board(20, 20)

pi, pj = board.random_location()
player = Player(pi, pj)

things = [player]

num = 7

dog_dict = {}
for i in range(num):
    dogi, dogj = board.random_location()
    dog = Dog(dogi, dogj, qualities = {'hunger': random.randint(0, 10),
                               'loyalty': random.randint(0, 10),
                               'cuteness': random.randint(0,10),
                               'fear' : 0,
                               'smarts' : random.randint(0,10),
                               'strength' : random.randint(0,10),
                               'food' : random.randint(0, 10)
                               })
    dog_dict[(dogi, dogj)] = dog
    things.append(dog)

cat_dict = {}
for i in range(num):
    cati, catj = board.random_location()
    cat = Cat(cati, catj, qualities = {'hunger' : random.randint(0, 10),
                                   'loyalty' : 0,
                                   'cuteness' :  random.randint(0, 10),
                                   'fear' : random.randint(0, 10),
                                   'smarts' : random.randint(0, 10),
                                   'strength' : random.randint(0, 10),
                                   'food' : random.randint(0, 10)
                                   })
    cat_dict[(cati, catj)] = cat
    things.append(cat)

scholar_dict = {}
for i in range(num):
    scholari, scholarj = board.random_location()
    scholar = Scholar(scholari, scholarj, qualities = {'hunger' : random.randint(0, 10),
                                       'loyalty' : random.randint(0, 10),
                                       'cuteness' : 0,
                                       'fear' :  random.randint(0, 10),
                                       'smarts' : 10,
                                       'strength' : random.randint(0, 10),
                                       'food' : random.randint(0, 10)
                                       })
    scholar_dict[(scholari, scholarj)] = scholar
    things.append(scholar)

croc_dict = {}
for i in range(num):
    croci, crocj = board.random_location()
    crocodile = Crocodile(croci, crocj, qualities = {'hunger' : random.randint(0, 10),
                                                 'loyalty' : 0,
                                                 'cuteness' : 0,
                                                 'fear' : 0,
                                                 'smarts' : random.randint(0, 10),
                                                 'strength' : random.randint(0, 10),
                                                 'food' : random.randint(0, 10)
                                                 })
    croc_dict[(croci, crocj)] = crocodile
    things.append(crocodile)

thief_dict = {}
for i in range(num):
    thiefi, thiefj = board.random_location()
    thief = Thief(thiefi, thiefj, qualities = {'hunger' : random.randint(0, 10),
                                   'loyalty' : 0,
                                    'cuteness' : 0,
                                    'fear' : 0,
                                    'smarts' : random.randint(0, 10),
                                    'strength' : random.randint(0, 10),
                                    'food' : random.randint(0, 10)
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


# for thing in (dog, cat, scholar, crocodile, thief, forest, town):
#     things.append(thing)

board.print(things)

