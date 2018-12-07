cards = ['a', '2', 'a']
for card in range(len(cards)):
...     if cards[card] == 'a':
...             if card_dict[cards[0]] + card_dict[cards[1]] + card_dict[cards[2]] <= 11:
...                     cards[card] = 'aa'
...
>>> cards = ['aa', '2', 'a']