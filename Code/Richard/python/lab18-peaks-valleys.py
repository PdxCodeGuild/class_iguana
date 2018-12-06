"""
author: Richard Sherman
2018-12-06
lab10-peaks-valleys.py, takes a list of ints and identifies elements greater than their immediate neighbors ('peaks')
and elements less than their immediate neighbors ('valleys'). Tries to extend this logic beyond immediate neighbors to find
the 'volume' of 'valleys' and the 'height' of 'peaks'
"""

import random

print('We\'ll generate a list of integers, then identify the \'peaks\' (those greater than their immediate neighbors\
      and the \'valleys\' (those less than their immediate neighbors. Here is the randomly generated list:')
terrain = []
size = range(7)
for i in size:
    terrain.append(random.randint(0, 10))
print(terrain)

print('First we identify the peaks:')
# there must be a way to do this using slicing only, but the while loop seems easier to read and easier to type
peaks = []
#if terrain[0] > terrain[1]:  # don't need this
 #   peaks.append(0)
i = 0
while i < len(terrain) - 1:
    if terrain[i] > terrain[i - 1] and terrain[i] > terrain[i + 1]:
        peaks.append(i)
    i += 1
print(peaks)

print('\nThen we identify the valleys:')
valleys = []
#if terrain[0] > terrain[1]:    # don't need this
 #   valleys.append(0)
i = 0
while i < len(terrain) - 1:
    if terrain[i] < terrain[i - 1] and terrain[i] < terrain[i + 1]:
        valleys.append(i)
    i += 1
print(valleys)

print('\nNow we want to know the volume of the valleys:')

index_value = []
for i in range(len(terrain) - 1) :
    index_value.append((i, terrain[i]))
print(index_value)
