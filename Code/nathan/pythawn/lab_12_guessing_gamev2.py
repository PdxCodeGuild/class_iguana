flavors = ['vanilla', 'mint' , 'chocolate', 'coffee', 'pistachio', 'cookie dough', 'cotton candy', 'coffee', 'moose tracks', 'fudge']
input('I want you to guess my favorite flavor of ice cream, this will be fun! \n press enter to see options...')
print('Here are your choices::: ' + ', '.join(flavors))

my_favorite_flavor = 'moose tracks'

guess_counter = 0
while True:
    guess = input('guess an ice cream flavor: ')
    guess_counter += 1
    if guess == my_favorite_flavor:
        print('YOU GUESSED MY FAVORITE ICE CREAM FLAVOR')
        print(f'That took {guess_counter} tries')
        break
    else:
        print('thats not my favorite flavor...')


