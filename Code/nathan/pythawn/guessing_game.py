import random

flavors = ['vanilla', 'mint' , 'chocolate', 'coffee', 'pistachio', 'cookie dough', 'cotton candy', 'coffee', 'moose tracks']
intro_text = input('I want you to guess my favorite flavor of ice cream, this will be fun! \n press enter to see options...')
guess = ''
while guess not in flavors:
    guess = input(' here are your choices::: vanilla, mint , chocolate, coffee, pistachio, cookie dough, cotton candy, coffee, moose tracks \n > ')
print(guess)
my_favorite_flavor = random.choice(flavors)
print(my_favorite_flavor)

if my_favorite_flavor == guess:
    print('YOU GUESSED MY FAVORITE ICE CREAM FLAVOR')
elif my_favorite_flavor != guess:
    print('thats not my favorite flavor...')