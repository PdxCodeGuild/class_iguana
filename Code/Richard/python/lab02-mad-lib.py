"""Author: Richard Sherman
2018-12-03
gets input from user and generates a mad lib from the input"""

import random
#create lists for random inclusion in mad lib
jobs = ['laborer', 'physician', 'grocer', 'astronaut']
tasks = ['dig', 'market', 'disassemble', 'reproduce']
teams = ['team', 'assembly', 'mob', 'corps']
objects = ['products', 'miracles', 'irrelevancies', 'constructs']

ant = input('Give me an antonym for "functional": ')
handed = input('Are you left-handed, right-handed, or ambidextrous? Please choose one: ')
adj = input('Give me an adjective: ')
others = input("Name a job/occupation, in the plural: ")
bldg = input("Name a part of a building: ")
buzz = input("Tell me a buzzword that you occasionally find annoying: ")
tech = input("Name a piece of technology: ")
comp = input("Tell me an aspect of your computer that you don't like: ")

print(f'{ant} Expert Job Description:')
print(f'Seeking {(adj)} {random.choice(jobs)}, able to {random.choice(tasks)} {buzz} {random.choice(objects)} with a {random.choice(teams)} of {others}. Must be {handed}.')
print('Key responsibilities:')
print(f' - Engage in profound study of all things {ant}.')
print(f' - Reconfigure {bldg}.')
print(f' - Explore applications of {tech} to {comp}s.')
print('Application deadline: January 1, 2019.')