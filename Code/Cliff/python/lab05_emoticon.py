import random
eyes = [':', ';', ]
noses = [' >', '#', '*', '-']
mouths = ['0', 'o', '0']
eyes = random.choice(eyes)
noses = random.choice(noses)
mouths = random.choice(mouths)
count = 0
while count < 5:
     print(eyes + noses + mouths), count
     count = count + 1

