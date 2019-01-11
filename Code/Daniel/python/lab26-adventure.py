import msvcrt
import copy
import levels
import time
import importlib
import lab26_inv as inv
rps = importlib.import_module('lab07-rock_paper_scissors')
guess = importlib.import_module('lab12-guess_the_number')


class Player:

    def __init__(self):
        self.player_position = {'x':4, 'y':9}
        self.last_position = {'x':0, 'y':0}
        self.player_direction = 'up'
        self.won_games = [False, False]
        self.fall_position = {'x':0, 'y':0} 


    def update_direction(self, player_direction):
        if player_direction == 'up':
            state.grid[2][13] = '\t△\n'
        elif player_direction == 'down':
            state.grid[2][13] = '\t▽\n'
        elif player_direction == 'left':
            state.grid[2][13] = '\t◁\n'
        elif player_direction == 'right':
            state.grid[2][13] = '\t▷\n'
        self.player_direction = player_direction


    def lvl_2_interact(self, obj):
        if state.current_level == 2:
            if obj.text_list == 'Hello' and self.won_games[0] == False:
                self.won_games[0] = rps.get_winner()
            elif obj.text_list == 'Yellow' and self.won_games[1] == False:
                self.won_games[1] = guess.guess()
            elif obj.text_list == 'Cello' and self.won_games[0] == False:
                print('I can\'t beat that guy at Rock, Paper, Scissors. He\'s pretty good. I\'m pretty sure he mainly chooses rock' +
                ' but he always knows when to switch off!')
            elif obj.text_list == 'Cello' and self.won_games[0] == True:
                print('You beat him! Wow. You\'re so cool.')
            else:
                print('Are you here to gloat? You\'ve already won. Leave me be.')
        else:
            print(obj.text_list)

        if self.won_games == [True, True] and 'This is an item' not in inv.inventory:       # Item dup possible by placing on table and interacting with npc again 
            inv.inventory.append('This is an item')


    def interact(self, state):
        check_space = ()

        if state.grid[2][13] == '\t△\n':
            check_space = (self.player_position['x'], self.player_position['y'] - 1)
        elif state.grid[2][13] == '\t▽\n':
            check_space = (self.player_position['x'], self.player_position['y'] + 1)
        elif state.grid[2][13] == '\t◁\n':
            check_space = (self.player_position['x'] - 1, self.player_position['y'])
        elif state.grid[2][13] == '\t▷\n':
            check_space = (self.player_position['x'] + 1, self.player_position['y'])

        # print(check_space)                  # Remove me!! Troubleshooting only
        try:
            obj = [item for item in levels.level_objects[state.current_level]['special'] if item.coord == check_space][0]
            self.lvl_2_interact(obj)
            if obj.is_item == True:
                inv.item_grabber([obj.text_list, obj.symbol], check_space, state.current_level)
                state.grid = copy.deepcopy(levels.level_list[state.current_level])
                if state.current_level == 1:
                    state.grid = dark_view((player.player_position['x'], player.player_position['y']), levels.level_list[state.current_level])
                update_position(state, player)
        except IndexError:
            pass




class Game_State:

    def __init__(self):
        self.current_level = 0
        self.previous_lvl = 0
        self.grid = levels.level_list[self.current_level]
        self.player_icon = ' O '
        self.obstructions = ['   ','_|_','| |','ΞΞΞ','__|','|__','|  ','  |','¯¯|','|¯¯','¯ ¯','|¯|',' X ']         # misnomer: change, 'X' for testing only

    def check_intersection(self):
        player_pos_tup = (player.player_position['x'],player.player_position['y'])
        if state.grid[player.player_position['y']][player.player_position['x']] not in self.obstructions:
            if player_pos_tup in levels.level_objects[state.current_level]['doors']:
                if self.current_level == 0:
                    if player_pos_tup == levels.level_objects[state.current_level]['doors'][1]:
                        player.player_position = {'x':6, 'y':10}
                        self.current_level += 1
                        state.grid = copy.deepcopy(levels.level_list[state.current_level])
                elif player_pos_tup == (6,0) and player.player_direction == 'up':
                    player.player_position = {'x':6, 'y':10}
                    self.current_level += 1
                    state.grid = copy.deepcopy(levels.level_list[state.current_level])
                self.previous_lvl = self.current_level - 1
                return False
            elif player_pos_tup == (6,11) and player.player_direction == 'down':
                self.previous_lvl = self.current_level

                if self.current_level == 1:
                    player.player_position = {'x':6, 'y':6}
                else:
                    player.player_position = {'x':6, 'y':2}

                self.current_level -= 1
                state.grid = copy.deepcopy(levels.level_list[state.current_level])
                return False
            return True 
        else:
            state.previous_lvl = state.current_level
            return False        

            

def update_position(state, player):
    print(player.player_position, player.last_position, player.fall_position, state.current_level, state.previous_lvl)      # Remove me! Troubleshooting only
    state.grid = copy.deepcopy(state.grid)  
    for i, row in enumerate(state.grid):
        if player.player_position['y'] == i: 
            for j in range(len(row)):
                if player.player_position['x'] == j:
                    row[j] = state.player_icon 
    if player.last_position != player.player_position:
        if state.previous_lvl != state.current_level and state.current_level == 1 and player.player_position['y'] > 9:  # player enters room from bottom 
            state.grid[player.last_position['y']][player.last_position['x']] = '   '
        elif state.previous_lvl != state.current_level and state.current_level == 1 and 3 > player.player_position['y']: # player enters room from top
            state.grid[player.last_position['y']][player.last_position['x']] = '   '
        elif (player.last_position['x'] < 5 or player.last_position['x'] > 7):
            state.grid[player.last_position['y']][player.last_position['x']] = '   '
        elif (player.last_position['y'] < 9 or player.last_position['y'] > 2):
            state.grid[player.last_position['y']][player.last_position['x']] = '   '
        else:
            state.grid[player.last_position['y']][player.last_position['x']] = levels.level_list[state.current_level][player.last_position['y']][player.last_position['x']]
    
                    
    grid_string = ''
    for row in state.grid:
        grid_string += ''.join(row)
    print(grid_string)

def on_platform(state, player):
    tile = levels.level_list[state.current_level][player.player_position['y']][player.player_position['x']]


    if player.player_position['y'] < 9:
        state.previous_lvl = 0

    if state.current_level == 1:
        if tile == '| |' or tile == '|_|' or tile == '|¯|':
            state.player_icon = '|O|' 
        elif tile == 'ΞΞΞ':
            state.player_icon = 'Ξ፬Ξ'
        elif tile[0] == '|':
            state.player_icon = '|O '
        elif tile[2] == '|':
            state.player_icon = ' O|'  
        elif tile == '   ':                         # issue with buffered inputs creating looong repeat fall animation
            player.fall_position = player.last_position
            fall_anim = [' o ',' · ','   ']

            for anim in fall_anim:
                state.player_icon = anim
                print('\n'*25)
                update_position(state, player)
                time.sleep(.5)
           
            player.player_position = {'x':6, 'y':10}
            on_platform(state, player)
            update_position(state, player)
            

        else:
            state.player_icon = ' O '
    else:
        state.player_icon = ' O '
    

def dark_view(player_pos, lvl1):
    x, y = player_pos 
    room_state = copy.deepcopy(lvl1)

    for i, row in enumerate(room_state):
        for j in range(len(row)):
            if j == len(row)-1:
                continue
            elif i not in range(y-1, y+2):
                room_state[i][j] = '   '
            else:
                if j not in range(x-1, x+2):
                    room_state[i][j] = '   '
                 
    return room_state



player = Player()
state = Game_State()
update_position(state, player)
inv = inv.Inventory()


# Uses wasd for movement, q for quit, and spacebar to interact. Prevents player from going out of bounds. Checks for intersections and
# prevents moving into occupied space. Updates player position and refreshes scene on move
while True:        

    command = msvcrt.getch()
    if command == b'q':
        break

    if command == b'w':
        if player.player_position['y'] != 0:
            player.last_position = copy.deepcopy(player.player_position)
            player.player_position['y'] -= 1
            
            if state.check_intersection() == True:
                player.player_position['y'] += 1
            on_platform(state, player)
        player.update_direction('up')

    elif command == b's':
        if player.player_position['y'] != 11: 
            player.last_position = copy.deepcopy(player.player_position)
            player.player_position['y'] += 1
            
            if state.check_intersection() == True:
                player.player_position['y'] -= 1
            on_platform(state, player)
        player.update_direction('down')

    elif command == b'a':
        if player.player_position['x'] != 1:
            player.last_position = copy.deepcopy(player.player_position)
            player.player_position['x'] -= 1
            
            if state.check_intersection() == True:
                player.player_position['x'] += 1
            on_platform(state, player) 
        player.update_direction('left')

    elif command == b'd':
        if player.player_position['x'] != 12:
            player.last_position = copy.deepcopy(player.player_position)
            player.player_position['x'] += 1
            
            if state.check_intersection() == True:
                player.player_position['x'] -= 1
            on_platform(state, player)
        player.update_direction('right')

    if state.current_level == 1:
        state.grid = dark_view((player.player_position['x'], player.player_position['y']), levels.level_list[state.current_level])
        player.update_direction(player.player_direction)

    print('\n'*25)
    update_position(state, player)

    if command == b' ':
        player.interact(state)

    if command == b'i':
        inv.view_inventory()


