#Blackjack Advice

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

#use random.choice with a full list of cards
# use a for loop to generate the list

import random

card_dict = {'A': 11,
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
             'K': 10}

def get_card_deck(shuffle=False):
    cards_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_deck = []
    for suit in suits_list:
        for card in cards_list:
            card_deck.append((card, suit))
    if shuffle:
        random.shuffle(card_deck)
    return card_deck


def main():
    card_deck = get_card_deck(shuffle=True)

    #what is the score of the card?
    user_start = input('Would you like to see your first two cards? (y/n) \n ')
    if user_start == 'yes' or user_start == 'y':
        card_one = card_deck.pop(0)
        card_two = card_deck.pop(0)
        card_one_score = card_dict[card_one[0]]
        card_two_score = card_dict[card_two[0]]
        print(card_one, card_two)
        # print(card_one_score, card_two_score)
        if card_one_score + card_two_score == 21:
            print('Blackjack!')
        elif card_one_score + card_two_score >= 17:
            print('Advise: Stay')
        elif card_one_score + card_two_score < 17:
            print('Advise: Hit')
            card_three = card_deck.pop(0)
            print(card_three)
            card_three_score = card_dict[card_three[0]]
            if card_one_score + card_two_score + card_three_score == 21:
                print('Blackjack!')
            elif card_one_score + card_two_score + card_three_score < 17:
                print('Advise: hit')
            elif card_one_score + card_two_score + card_three_score >= 17:
                print('Advise: Stay')

    else:
        print('Bye')


main()




