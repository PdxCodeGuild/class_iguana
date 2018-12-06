"""
author: Richard Sherman
2018-12-06
lab19-blackjack.py, advises to hit or stay given a blackjack hand
"""
import random

print('I\'ll deal you a blackjack hand. Then you can decide to hit or stay. But I\'ll help you by giving you advice.')
print('To make it interesting, I\'ll play too. I won\'t look at my hand until you\'re finished, and I will always take exactly three cards.')
print('We\'ll start with the simple case, where an ace is always worth 1.')
z = input('If you\'re ready, hit the Enter (Return) key and I\'ll deal your first two cards.')

deck = [str(x) for x in range(2, 11)] + list('JQKA')
values = list(range(2, 11)) + [10, 10, 10, 1]  #there must be a better way to generate [10, 10, 10, 1]
values_dict = dict(zip(deck, values))
# advice_dict = {range(3, 17): 'Hit.', range(17, 21): 'Stay.', 21: 'Blackjack!', range(22, 32): "Sorry, you\'re busted."}
# print(deck)
# print(values_dict)
# print(advice_dict)
hand = random.sample(deck, 2)
# print(hand)
hand_sum = values_dict[hand[0]] + values_dict[hand[1]]
if 'A' in hand and hand_sum > 16:
    hand_sum += 10
print(f'\nYour hand is a {hand[0]} and a {hand[1]}. That makes {hand_sum}.')
player_decision = input('What do you want to do? Hit h for hit or s for stay:  ')
# advice = advice_dict[hand_sum]

while True:
    if hand_sum < 17:
        advice = 'Hit.'
        advice_code = 'h'
    elif hand_sum > 16 and hand_sum < 21:
        advice = 'Stay.'
        advice_code = 's'
    elif hand_sum == 21:
        print('You\'ve got blackjack!')
        break
    else:
        print('Sorry, you\'re busted.')
        break
    if player_decision == advice_code:
        print(\,That\'s my advice, too.')
    else:
        player_decision = input(f'\nWhat I would say is {advice} Would you like to hit (h) or stay (s)?  ')
    if player_decision == 's':
        break
    elif player decision == 'h':

