import random

eyes = [':', '8', '=', 'X', ';']
noses = ['^', '-', '', 'o']
mouths = [')', '(', ']', '[', 'O', 'D', 'P', '/', '|']

i = 0
while i <=5:
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    print(eye + nose + mouth)
    i += 1