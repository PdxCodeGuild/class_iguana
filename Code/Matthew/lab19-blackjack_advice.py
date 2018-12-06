

suits = ['diamonds', 'hearts', 'spades', 'clubs']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# [('Diamond', 'King'), ('Diamond', 'Queen')]
# [{'suit': 'Diamond', 'value': 'King'}, {}]

# O(n^2)
cards = []
for suit in suits:
    for value in values:
        print(f'{suit} {value}')
        cards.append({'suit': suit, 'value': value})

print(cards)
print(len(cards))


import random

card = cards.pop(random.randint(0, len(cards)-1))

print(card)


# value = 5
# for v in [1, 2, 3, 4, 5, 6, 7, 8]:
#     if v == value:
#         print('found')








card_1 = input('Please tell me your first card:  ')
card_2 = input('Please tell me your second card:  ')
card_3 = input('Please tell me your third card:  ')



def get_value(card):
    card = card.lower()
    if card in 'jqk':
        return 10
    if card == 'a':
        return 1
    return int(card)






def get_value(card):
    values = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    return values.get(card)


hand = get_value(card_1) + get_value(card_2) + get_value(card_3)
print(hand)

def give_advice(hand):
    if hand < 17:
        print('Hit!')
    elif hand >= 17 and hand < 21:
        print('Stay!')
    elif hand == 21:
        print('Blackjack!')
    elif hand > 21:
        print('Already Busted :(')
give_advice(hand)

if 'A' in [card_1, card_2, card_3] and hand <= 10:
    hand += 10
    print(hand)
    give_advice(hand)

