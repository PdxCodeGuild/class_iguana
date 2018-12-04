import random

eyes = [';', ':', 'B']
nose = ['<', '@', '~', '-']
mouth = ['p', ')', '(', '/', '\\']
emot = 0
while emot < 5:
# print(random.choice(eyes), random.choice(nose), random.choice(mouth), sep='')
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
    emot = emot + 1