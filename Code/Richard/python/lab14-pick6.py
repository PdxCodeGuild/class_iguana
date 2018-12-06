"""
author: Richard Sherman
2018-12-05
lab14-pick6.py, a lottery-style game
repeats a two-dollar lottery with payoffs based on number of matched numbers between ticket and winning number
version 1 calculates ending payoff - ticket costs, and ROI =  (payoff - ticket costs) / ticket costs
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

winning_number = random.sample(list(range(0, 100)), 6)
balance =  0
for i in range(1, 100001):
    number_of_matches = 0
    balance = balance - 2
    ticket_number = random.sample(list(range(0, 100)), 6)
    for j in range(len(ticket_number)):
        if ticket_number[j] == winning_number[j]:
            number_of_matches += 1
    balance = payoff[number_of_matches] + balance
earnings = balance + 200000
expenses = 200000
ROI = (earnings - expenses) / expenses
print(f'\nYour final balance is {balance}')
print(f'Earnings:\t{earnings}')
print(f'Expenses:\t{expenses}')
print(f'ROI:\t{ROI}')

