"""
steps for LCR:

get players' names, center (call it center)
each player has: (position in list), number of chips, name
list of dicts { name : chips }
list of lists [name, chips]

loop: start with three chips each

player rolls dice (how many?)
move chips left / right / center / not at all depending on roll of dice
next player rolls dice
etc.

stopping condition: only one player has chips

{'name': 'matthew', 'chips': 3}


"""
import random


player_names = ['Jose', 'Joseph', 'Josephine', 'Josip', 'Joe', 'Joanna']
# get the number of players and the player's names
num_players = int(input('How many players are there?  '))

players = [{'name': random.choice(player_names) + str(i), 'chips': 3} for i in range(num_players)]

# players = []
# for i in range(num_players):
#     player_name = input('What is the player\'s name? ')
#     player_chips = 3
#     player = {'name': player_name, 'chips': player_chips}
#     players.append(player)
print(players)

# set up variables for the rest of the game
center = 0
dice_choices = ['L', 'C', 'R', '.', '.', '.' ]
current_player_index = 0
while True:
    # find the number of die rolled for this player
    n_dice = 3 if players[current_player_index]['chips'] >= 3 else players[current_player_index]['chips']
    for i in range(n_dice):
        # roll the die
        roll = random.choice(dice_choices)

        # move the chips
        if roll == 'L':
            players[current_player_index]['chips'] -= 1
            players[current_player_index - 1]['chips'] += 1
        elif roll == 'C':
            players[current_player_index]['chips'] -= 1
            center += 1
        elif roll == 'R':
            players[current_player_index]['chips'] -= 1
            # loop back to the first player if we've gone past the end
            right_player_index = current_player_index + 1
            if right_player_index == len(players):
                right_player_index = 0
            players[right_player_index]['chips'] += 1
            # players[(current_player_index + 1)%len(players)] += 1
    
    # update the current player
    current_player_index += 1
    if current_player_index == len(players):
        current_player_index = 0
    
    # check if somebody won
    counter = 0
    for i in range(len(players)):
        if players[i]['chips'] > 0:
            counter += 1
    if counter == 1:
        break


winner = None
for player in players:
    if player['chips'] > 0:
        winner = player
        break
winner['chips'] += center
print(f'{winner["name"]} won with {winner["chips"]} chips')
