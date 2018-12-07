number = input('pick a number between 1 and 100 \n >')
name = input('what is your name? \n >')
ski = input('do you ski or snowboard? \n >')
cereal_type = input('what is your favorite type of cereal? \n >')
insult = input('type in an insult that is a verb \n >')
weather = input('how is the weather today? \n >')
home = input('where do you live\n >')
animal = input('type an animal \n>')

skiiers = 1000
chair_lift = 4
chairs = 200

number_people_in_line = skiiers / chair_lift - chairs

print(f'SO, {name}, we are going on a skiing trip :)))).')
print(f'You are having {cereal_type} for breakfast???\n Thats kind of gross, are you still in first grade? \nMy truck is full of {animal} so you can sit in the truck bed.\n I dont really like riding with {ski}ers, you better keep up.\nThere is {skiiers} people here today, {chairs} chairs on the lift, and {chair_lift} people per chair.so, there should be {number_people_in_line} people in line for the lift.\n The weather is {weather}, and you {insult} at {ski}ing.You have fallen {number} times,, I cant wait to get back to {home} !!!')