# ^_^  , ;-; , ^-^ , .-. , (>^-^)>
import random

start_text = input('PRESS ENTER TO RANDOMLY CREATE A KIRBY')

side = ['(']
hand = ['>']
face = ['^_^', ';-;', '^-^', '.-.', '.-,']
side2 = [')']
hand2 = ['>']
string = ''
string = string + random.choice(side)
string = string + random.choice(hand)
string = string + random.choice(face)
string = string + random.choice(side2)
string = string + random.choice(hand2)
print(string)