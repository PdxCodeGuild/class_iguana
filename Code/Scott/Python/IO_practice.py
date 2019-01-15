#for practice with fil IO

#create a list and print it to a csv file

import csv

# animal_list = ['dogs', 'cats', 'llamas', 'bulls', 'giraffes', 'lions', 'bears']



with open('animals.csv') as file:
    lines = file.read().split('\n')
    for line in lines:
        if line == '':
            continue
    # print('\n'.join(lines))
# print('\n'.join(animal_list))

added_animals = ['cheetah', 'boxer', 'viper', 'goldfish', 'crane', 'bull']
added_animals = ','.join(added_animals)
lines.append(added_animals)

print(lines)
# print(added_animals)

with open('animals2.csv', 'w') as animal_file:
	animal_file.write('\n'.join(lines))


