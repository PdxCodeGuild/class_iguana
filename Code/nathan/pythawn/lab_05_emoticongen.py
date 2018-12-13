import random
#allows program to know what random is
start = input('PRESS ENTER TO CREATE AN EMOTICON AT RANDOM')
#pointless intro text to allow user to know what program is going to do
mouths = ['D', ')', '(', 'p', '/']
noses = ['^', 'c', '<', '*']
eyes = [':', 'X', ';', 'B']
#list of emoticon face pieces
outstring = '' #outstring starts as blank string
outstring += random.choice(eyes)
outstring += random.choice(noses)
outstring += random.choice(mouths)
#combines randomly picked face pieces to blank string
print(outstring)
#prints now not blank string
