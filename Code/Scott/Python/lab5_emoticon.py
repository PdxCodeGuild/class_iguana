#lab5 emoticon generator
import random

#Define lists of eyes, noses, mouths
eyes_list = [':', '=', ';']
noses_list = ['-', '>', 'o']
mouth_list = ['(', ')', '0']

i = 0
while i < 5:
    face = random.choice(eyes_list) + random.choice(noses_list) + random.choice(mouth_list)
    print(face)
    i = i + 1





