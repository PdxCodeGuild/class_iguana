import msvcrt
import copy
import levels

class Game_State:
    

    def __init__(self):
        self.player_position = {'x':4, 'y':9}
        self.last_position = {'x':0, 'y':0}
        self.player_direction = 'up'
        self.current_level = 0
        self.grid = levels.level_list[self.current_level]
        self.player = ' O '
        self.obstructions = ['   ','_|_','| |','ΞΞΞ','__|','|__','|  ','  |','¯¯|','|¯¯','']

    def check_intersection(self):
        player_pos_tup = (self.player_position['x'],self.player_position['y'])
        if state.grid[self.player_position['y']][self.player_position['x']] not in self.obstructions:
            if player_pos_tup in levels.level_objects[state.current_level]['doors']:
                if self.current_level == 0:
                    if player_pos_tup == levels.level_objects[state.current_level]['doors'][1]:
                        self.player_position = {'x':6, 'y':10}
                        self.current_level += 1
                        state.grid = copy.deepcopy(levels.level_list[state.current_level])
                elif player_pos_tup == (6,0) and self.player_direction == 'up':
                    self.player_position = {'x':6, 'y':11}
                    self.current_level += 1
                    state.grid = copy.deepcopy(levels.level_list[state.current_level])
                return False
            elif player_pos_tup == (6,11) and self.player_direction == 'down':
                print('adsfsff')
                self.player_position = {'x':6, 'y':1}
                self.current_level -= 1
                state.grid = copy.deepcopy(levels.level_list[state.current_level])
                return False
            return True 
        else:
            return False        


    def update_direction(self, player_direction):
        if player_direction == 'up':
            self.grid[2][13] = '\t△\n'
        elif player_direction == 'down':
            self.grid[2][13] = '\t▽\n'
        elif player_direction == 'left':
            self.grid[2][13] = '\t◁\n'
        elif player_direction == 'right':
            self.grid[2][13] = '\t▷\n'
        self.player_direction = player_direction


    def interact(self):
        check_space = ()

        if self.grid[2][13] == '\t△\n':
            check_space = (self.player_position['x'], self.player_position['y'] - 1)
        elif self.grid[2][13] == '\t▽\n':
            check_space = (self.player_position['x'], self.player_position['y'] + 1)
        elif self.grid[2][13] == '\t◁\n':
            check_space = (self.player_position['x'] - 1, self.player_position['y'])
        elif self.grid[2][13] == '\t▷\n':
            check_space = (self.player_position['x'] + 1, self.player_position['y'])

        print(check_space)
        try:
            obj = [item for item in levels.level_objects[state.current_level]['special'] if item.coord == check_space][0]
            print(obj.text_list)
        except IndexError:
            pass
            

def update_position(state):
    print(state.player_position, state.current_level)
    state.grid = copy.deepcopy(state.grid)     # state.grid = copy.deepcopy(levels.level_list[state.current_level])
    for i, row in enumerate(state.grid):
        if state.player_position['y'] == i: 
            for j in range(len(row)):
                if state.player_position['x'] == j:
                    on_platform(state)
                    row[j] = state.player 
    if state.last_position != state.player_position:
        state.grid[state.last_position['y']][state.last_position['x']] = levels.level_list[state.current_level][state.last_position['y']][state.last_position['x']]
                    
    grid_string = ''
    for row in state.grid:
        grid_string += ''.join(row)
    print(grid_string)

def on_platform(state):
    tile = levels.level_list[state.current_level][state.player_position['y']][state.player_position['x']]
    if state.current_level == 1:
        if tile == '| |' or tile == '|_|':
            state.player = '|O|' 
        elif tile == 'ΞΞΞ':
            state.player = 'Ξ፬Ξ'
        elif tile[0] == '|':
            state.player = '|O '
        elif tile[2] == '|':
            state.player = ' O|'    
        else:
            state.player = ' O '
    else:
        state.player = ' O '


    


state = Game_State()
update_position(state)


# Uses wasd for movement. q for quit. Prevents player from going out of bounds. Checks for intersections and
# prevents moving into occupied space. Updates player position and refreshes scene on move
while True:                         
    command = msvcrt.getch()
    if command == b'q':
        break

    if command == b' ':
        state.interact()

    if command == b'w':
        if state.player_position['y'] != 0:
            state.last_position = copy.deepcopy(state.player_position)
            state.player_position['y'] -= 1
            
            if state.check_intersection() == True:
                state.player_position['y'] += 1
        state.update_direction('up')

    elif command == b's':
        if state.player_position['y'] != 12: 
            state.last_position = copy.deepcopy(state.player_position)
            state.player_position['y'] += 1
            
            if state.check_intersection() == True:
                state.player_position['y'] -= 1
        state.update_direction('down')

    elif command == b'a':
        if state.player_position['x'] != 1:
            state.last_position = copy.deepcopy(state.player_position)
            state.player_position['x'] -= 1
            
            if state.check_intersection() == True:
                state.player_position['x'] += 1
        state.update_direction('left')

    elif command == b'd':
        if state.player_position['x'] != 12:
            state.last_position = copy.deepcopy(state.player_position)
            state.player_position['x'] += 1
            
            if state.check_intersection() == True:
                state.player_position['x'] -= 1
        state.update_direction('right')

    update_position(state)


