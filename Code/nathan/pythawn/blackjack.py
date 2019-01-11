import random


class Black_jack:

    def __init__(self, score, card, cards_drawn):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.suits = ['♤', '♧', '♡', '♢']
        self.deck = []
        self.card_values = []
        self.score = score
        self.card = card
        self.cards_drawn = cards_drawn

    def build_deck(self):
        for i in self.suits:
            for j in self.values:
                self.deck.append((i, j))
        return self.deck

    def find_score(self):
        self.card_values = [sum(self.card_values)]
        self.score = self.card_values
        if self.score > [21]:
            return f' Bust!, Your score is at {self.score}'
        else:
            return f'Your score is at {self.score}'

    def draw_card(self):
        self.cards_drawn += 1
        self.card = random.choice(self.deck)
        if self.card[1] == 1 and self.score <= [10]:
            self.card_values.append(11)
        elif self.card[1] == 'J':
            self.card_values.append(10)
        elif self.card[1] == 'Q':
            self.card_values.append(10)
        elif self.card[1] == 'K':
            self.card_values.append(10)
        else:
            self.card_values.append(self.card[1])
        return f'{self.card}\n{self.cards_drawn}'

    def win_or_loose(self):
        if self.score == [21]:
            return 'TwEnTy OnE!'
        if self.score > [21]:
            return 'loose'
        elif self.score <= [21]:
            return 'not loose'


#♤ ♧ ♡ ♢
# 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾
# 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮
# 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎
# 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞
black_jack = Black_jack(0, 0, 0)

while True:
    black_jack.build_deck()
    start = input('would you like a hit?\ntype \'stay\' if done\n>')
    if start == 'yes':
        print(black_jack.draw_card())
        print(black_jack.find_score())
    if black_jack.win_or_loose() == 'TwEnTy OnE!':
        print('TwEnTy OnE!\nCheers!')
        break
    if black_jack.win_or_loose() == 'loose':
        break
    elif start == 'stay':
        print(black_jack.win_or_loose())
        break




