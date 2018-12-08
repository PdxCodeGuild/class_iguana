"""
author: Richard Sherman
2018-12-08
lab-lcr-simulator.py, simulates lcr game of dice
"""

# This is slightly different than the game described in the lab (it is simpler).
# For example: when any L is rolled, the player hands one chip to the player on the left (likewise right).
# Of two or three L's are rolled, the player still hands only one chip to the left (likewise right).
# This should be fixed in a revision.
# The player with the dice and the outcome of the roll are shown in each iteration to check
# that the game is programmed correctly.

import random

# players = 1, 2, 3
# dice = d1, d2, d3
# order of players is left-to-right 1, 2, 3, 1

def chips_zero(chips):
    count = 0
    i = 0
    while i < 3:
        if chips[i] == 0:
            count += 1
        i += 1
    if count > 1:
        return True


chips = [10, 10, 10]

while chips_zero != 1:
    player = 0
    while player < 3:
        roll = [random.choice('LRC...'), random.choice('LRC...'), random.choice('LRC...')]
        print(player)
        print(roll)
        for die in roll:
            if die == 'L':
                if chips[player] != 0:
                    chips[player] -= 1
                    chips[(player - 1) % 3 ] += 1
            if die == 'R':
                if chips[player] != 0:
                    chips[player] -= 1
                    chips[(player + 1) % 3] += 1
            if die == 'C':
                if chips[player] != 0:
                    chips[player] -= 1
        print(chips)
        player += 1

    if chips_zero(chips):
        break
maximum = max(chips)
print(f'Player {chips.index(maximum)} won!')



