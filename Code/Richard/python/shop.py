import random

class Shop():
    def __init__(self, stock, cash, price):
        self.stock =  stock
        self.cash = cash
        self.price =  price
        self.transactions = []

    def restock(self):
        print(self.stock)
        qn = input('Would you like to re-stock? y or n:  ')
        if 'y' in qn:
            to_stock = input('What would you like to re-stock? shirts, pants, shoes, or socks:  ')
            qty_to_stock = int(input(f'How many new {to_stock} do want?'  ))
            self.stock[to_stock] += qty_to_stock
            self.cash -= qty_to_stock * self.price[to_stock]

    def sell(self):
        item_to_sell = input('There\'s a customer in the shop. What would you like to sell? shirts, pants, shoes, or socks:  ')
        offer = random.uniform(0, price[item_to_sell] * 2)
        sell_not_sell = input(f'The price they\'re offering is {offer}. Would you like to take that offer? y or n:  ')
        qty_to_sell = input('How many do you want to sell? 1, 2, 3 ...?  ')
        if 'y' in qty_to_sell:
            self.cash += offer * qty_to_sell
            self.stock[qn] -= qty_to_sell

    def check_books(self):
        print(transactions)


stock = {'shirts': 10,
         'pants': 10,
         'shoes': 10,
         'socks': 10
         }
price = {'shirts': 3,
         'pants':  5,
         'shoes':  10,
         'socks':  1}

shop = Shop(stock, price, 100)
shop.sell()
shop.restock()