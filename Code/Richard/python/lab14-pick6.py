"""
author: Richard Sherman
2018-12-05
lab14-pick6.py, a lottery-style game
"""

import random

payoff = {
            0   :   0,
            1   :   4,
            2   :   7,
            3   :   100,
            4   :   50000,
            5   :   1000000,
            6   :   25000000
            }

winning = random.sample(list(range(0, 100)), 6)
balance =  0
for i in range(1, 100001):
    n_match = 0
    balance = balance - 2
    ticket = random.sample(list(range(0, 100)), 6)
    print(ticket)
    print(winning)
    for j in range(len(ticket)):
        if winning[j] == ticket[j]:
            n_match += 1
            balance += payoff[n_match]
    balance = payoff[n_match] + balance
print(f'\nYour final balance is {balance}')


