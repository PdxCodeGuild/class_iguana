# cards_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# suits_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#
# card_deck = []
# for suit in suits_list:
#     for card in cards_list:
#         suit_card = [(card, suit)]
#         card_deck += suit_card
#         # random.shuffle(card_deck)
# print(card_deck)
    # return card_deck

card_deck = [('A', 'Hearts'), ('2', 'Hearts'), ('3', 'Hearts'), ('4', 'Hearts'), ('5', 'Hearts'), ('6', 'Hearts'), ('7', 'Hearts'), ('8', 'Hearts'), ('9', 'Hearts'), ('10', 'Hearts'), ('J', 'Hearts'), ('Q', 'Hearts'), ('K', 'Hearts'), ('A', 'Diamonds'), ('2', 'Diamonds'), ('3', 'Diamonds'), ('4', 'Diamonds'), ('5', 'Diamonds'), ('6', 'Diamonds'), ('7', 'Diamonds'), ('8', 'Diamonds'), ('9', 'Diamonds'), ('10', 'Diamonds'), ('J', 'Diamonds'), ('Q', 'Diamonds'), ('K', 'Diamonds'), ('A', 'Clubs'), ('2', 'Clubs'), ('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs'), ('7', 'Clubs'), ('8', 'Clubs'), ('9', 'Clubs'), ('10', 'Clubs'), ('J', 'Clubs'), ('Q', 'Clubs'), ('K', 'Clubs'), ('A', 'Spades'), ('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'), ('5', 'Spades'), ('6', 'Spades'), ('7', 'Spades'), ('8', 'Spades'), ('9', 'Spades'), ('10', 'Spades'), ('J', 'Spades'), ('Q', 'Spades'), ('K', 'Spades')]
card_dict = {}
for card in card_deck:
    if card[0] == 'A':
        card_dict.update({card : 11})
    if card[0] == '2':
        card_dict.update({card: 2})
    if card[0] == '3':
        card_dict.update({card: 3})
    if card[0] == '4':
        card_dict.update({card: 4})
    if card[0] == '5':
        card_dict.update({card: 5})
    if card[0] == '6':
        card_dict.update({card: 6})
    if card[0] == '7':
        card_dict.update({card: 7})
    if card[0] == '8':
        card_dict.update({card: 8})
    if card[0] == '9':
        card_dict.update({card: 9})
    if card[0] == '10':
        card_dict.update({card: 10})
    if card[0] == 'J':
        card_dict.update({card: 10})
    if card[0] == 'Q':
        card_dict.update({card: 10})
    if card[0] == 'K':
        card_dict.update({card: 10})

print(card_dict)

