"""
author: Richard Sherman
2018-12-08
lab-lcr-simulator.py, simulates lcr game of dice
"""
import random

# players = 1, 2, 3
# dice = d1, d2, d3
# order of players is left-to-right 1, 2, 3, 1

def chips_zero(chips):
    count = 0
    for i in chips:
        if chips[i] == 0:
            count += 1
    if count > 1:
        return True


chips = [10, 10, 10]
player = 1
while chips_zero != 1:
    roll = [random.choice('LRC...'), random.choice('LRC...'), random.choice('LRC...')]
    for die in roll:
        if die == 'L':
            if chips[player] != 0:
                chips[player] -= 1
                chips[player % 3 - 1] += 1
        if die == 'R':
            if chips[player] != 0:
                chips[player] -= 1
                chips[player % 3 + 1] += 1
        if die == 'C':
            if chips[player] != 0:
                chips[player] -= 1
    player += 1

    if chips_zero(chips):
        break
    maximum = max(chips)
    print(chips.index(maximum))



