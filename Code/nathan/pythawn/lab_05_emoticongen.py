import random

start = input('PRESS ENTER TO CREATE AN EMOTICON AT RANDOM')

mouths = ['D', ')', '(', 'p', '/']
noses = ['^', 'c', '<', '*']
eyes = [':', 'X', ';', 'B']

outstring = ''
outstring += random.choice(eyes)
outstring += random.choice(noses)
outstring += random.choice(mouths)
print(outstring)
