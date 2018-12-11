"""Author: Richard Sherman
2018-12-03
lab05-emoticons.py, generates random emoticons"""

import random

eyes = [':', ';', '!', '*']
noses = ['v', '^', '>', '-']
mouths = [')', '(', '|', '\\']

for i in range(0, 11):
    face = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    print(face)
    