import random

class Shop():
    def __init__(self, stock, cash, price):
        self.stock =  stock
        self.cash = cash
        self.price =  price


    def restock(self):
        print(self.stock)
        qn = input('Would you like to re-stock? y or n:  ')
        if 'y' in qn:
            to_stock = input('What would you like to re-stock? shirts, pants, shoes, or socks:  ')
            qty_to_stock = int(input(f'How many new {to_stock} do want?'  ))
            self.stock[to_stock] += qty_to_stock
            self.cash -= qty_to_stock * self.price[to_stock]

    def sell(self):
        qn = input('There\'s a customer in the shop. What would you like to sell? shirts, pants, shoes, or socks:  ')
        offer = price[qn] * (1 + random.uniform(0, price[qn]))
        print(f'The price they\'re offering is {offer}.')
        answer = input('How many do you want to sell? 1, 2, 3 ...?  ')
        if 'y' in answer:
            self.cash += offer * answer
            self.stock[qn] -= answer


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