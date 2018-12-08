card_list = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10}

first_card = input('what is your first card?')
print(card_list[first_card])

second_card = input('what is your second card?')
print(card_list[second_card])

third_card = input('what is your third card?')
print(card_list[third_card])

card_count = (card_list[first_card]) + (card_list[second_card]) + (card_list[third_card])

print(card_count)
if card_count < 17:
    print('hit')
elif card_count > 17 and card_count < 21:
    print('stay')
elif card_count == 21:
    print('black jack')
elif card_count > 21:
    print('bust')





