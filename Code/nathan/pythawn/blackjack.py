import random


class Black_jack:

    def __init__(self, score, card):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.suits = ['♤', '♧', '♡', '♢']
        self.deck = []
        self.card_values = []
        self.score = score
        self.card = card


    def build_deck(self):
        for i in self.suits:
            for j in self.values:
                self.deck.append((i, j))
        return self.deck

    def find_score(self):
        self.card_values = [sum(self.card_values)]
        self.score = self.card_values
        if self.score > [21]:
            print('bust')
        return f' Your score is at {self.score}'

    def draw_card(self):
        self.card = random.choice(self.deck)
        self.card_values.append(self.card[1])
        return self.card


#♤ ♧ ♡ ♢
# 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾
# 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮
# 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎
# 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞
black_jack = Black_jack(0, 0,)

while True:
    black_jack.build_deck()
    start = input('would you like a hit?\ntype \'stay\' if done')
    print(black_jack.draw_card())
    print(black_jack.find_score())





