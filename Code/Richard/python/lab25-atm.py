"""
author: Richard Sherman
2018-12-16
lab25-atm.py, an ATM simulator, an exercise in classes and functions
"""
import datetime

class ATM():
    def __init__(self, balance = 100, rate = 0.01):
        self.balance = balance
        self.rate = rate
        self.transactions = []

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        return True

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f'Withdrawal of {amount}, {datetime.datetime.now()}, Balance = {self.balance} ')
        else:
            print('Insufficient funds')


    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposit of {amount}, {datetime.datetime.now()}, Balance = {self.balance}')

    def check_balance(self):
        self.calc_interest(self.balance)
        self.transactions.append(f'Interest of {self.rate} added to balance, {datetime.datetime.now()}, Balance = {self.balance}')
        return self.balance

    def calc_interest(self, rate):
        self.balance += self.balance * self.rate
        return self.balance

    def print_transactions(self):
        print(self.transactions)

atm = ATM()
while True:
    command = input('what would you like to do (deposit, withdraw, check balance, history, exit)? ')
    if command == 'exit':
        print('Thank you for banking with us!')
        break
    elif command == 'deposit':
        amount = float(input('what is the amount you\'d like to deposit? '))
        atm.deposit(amount)
    elif command == 'withdraw':
        amount = float(input('what is the amount you\'d like to withdraw? '))
        atm.withdraw(amount)
    elif command == 'check balance':
        print(f'Your account balance is ${atm.check_balance()}')
    elif command == 'history':
        atm.print_transactions()
