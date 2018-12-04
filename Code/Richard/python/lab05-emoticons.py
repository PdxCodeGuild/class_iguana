"""Author: Richard Sherman
2018-12-03
lab05-emoticons.py, generates random emoticons"""

import random

eyes = [':', ';', '!', '*']
noses = ['v', '^', '>', '-']
mouths = [')', '(', '|', '\\']

i = 1
while i < 11:
    print(f'face {i}:  {random.choice(eyes)} + {random.choice(noses)} + {random.choice(mouths)}')
    i += 1
