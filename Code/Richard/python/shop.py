"""
author: Richard Sherman
2018-12-20
shop.py, a.k.a. lab25-atm-v2.py, simulates a shop selling 4 items of clothing,
an exercise in classes and functions
"""

import random
import datetime

class Shop():
    def __init__(self, stock, price, cash):
        self.stock =  stock
        self.cash = cash
        self.price =  price
        self.transactions = []

    def restock(self):
        print(f'\nThe current inventory is {self.stock}.')
        stock_not_stock = input('Would you like to re-stock? y or n:  ')
        if 'y' in stock_not_stock:
            to_stock = input('\nWhat would you like to re-stock? shirts, pants, shoes, or socks:  ')
            qty_to_stock = int(input(f'\nHow many new {to_stock} do want?  '))
            if self.cash >= qty_to_stock * self.price[to_stock]:
                self.stock[to_stock] += qty_to_stock
                self.cash -= qty_to_stock * self.price[to_stock]
                self.transactions.append(f'Stocked {qty_to_stock} {to_stock}, {datetime.datetime.now()}, Cash on hand = {self.cash} ')
            else:
                print('We don\'t have enough cash on hand. We\'ll have to restock later.')

    def sell(self):
        item_to_sell = input('\nThere\'s a customer in the shop. What would you like to sell? shirts, pants, shoes, or socks:  ')
        offer = round(random.uniform(price[item_to_sell] - 1, price[item_to_sell] * 2), 2)
        sell_not_sell = input(f'The price they\'re offering is {offer}. Would you like to take that offer? y or n:  ')
        if 'y' in sell_not_sell:
            qty_to_sell = int(input('How many do you want to sell? 1, 2, 3 ...?  '))
            if stock[item_to_sell] < qty_to_sell:
                if stock[item_to_sell] == 0:
                    print('We don\'t have any in stock.')
                else:
                    print(f'We have {stock[item_to_sell]} on hand. We\'ll sell those now and then restock.')
            self.cash += offer * qty_to_sell
            self.stock[item_to_sell] -= qty_to_sell
            self.transactions.append(f'Sold {qty_to_sell} {item_to_sell}, {datetime.datetime.now()}, Cash on hand = {self.cash} ')

    def check_books(self):
        print(f'\n{self.transactions}')


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

print('\nThe shop\'s open!\n')
print('When it\'s time to close, just type q.\n')

while True:
    shop.sell()
    shop.restock()
    shop.check_books()