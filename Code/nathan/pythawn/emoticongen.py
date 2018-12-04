import random

start = input('PRESS ENTER TO CREATE AN EMOTICON AT RANDOM')

mouths = ['D', ')', '(', 'p', '/']
noses = ['^', 'c', '<', '*']
eyes = [':', 'X', ';', 'B']
outstring = ''

outstring = outstring + random.choice(eyes)
outstring = outstring + random.choice(noses)
outstring = outstring + random.choice(mouths)
print(outstring)
