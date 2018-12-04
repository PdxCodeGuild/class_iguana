#lab02 version 2 madlib with list
import random
person = input('Please provide or make up a first and last name:\n')
nouns = input('Please input 5 nouns separated by a comma - you know, person, place, or thing:\n')
noun_list = nouns.split(', ')  # 'apples, bananas, pears'.split(', ') -> ['apples', 'bananas', 'pears']
#print(noun_list)

verbs = input('Please provide 5 past tense verbs separated by a comma:\n')
verb_list = verbs.split(', ')
adjectives = ('Pleae provide 4 adjectives separated by a comma:\n')
adjective_list = adjectives.split(', ')

print(f'Incident Report #1209.4\n At approximately 10 am, {person} {random.choice(verb_list)} a {random.choice(noun_list)} onto the {random.choice(noun_list)}. This caused the {random.choice(noun_list)}  to  {random.choice(verb_list)} it\'s {random.choice(noun_list)}. As a result, {person} has been put on suspension.')

