import levels
# import importlib
# lab26 = importlib.import_module('lab26-adventure')

class Inventory:
    def __init__(self):
        self.inventory = []

    def view_inventory(self):
        print('\n'*25) 
        for item in self.inventory:
            print(item)
    
    def place_item(self):
        pass

    def item_grabber(self, obj, item_pos, lvl):
        answer = input('Add to inventory? y/n ')
        if answer == 'y':
            self.inventory.append(obj)
            levels.level_list[lvl][item_pos[1]][item_pos[0]] = '   '
            # print('\n'*25)