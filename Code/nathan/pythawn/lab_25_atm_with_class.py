class Atm:

    def __init__(self, balance, interest):
        self.balance = balance
        self.history = []
        self.interest = interest

    def check_balance(self):
        return self.balance

    def check_interest(self):
        return self.balance * self.interest

    def deposit(self, amount):
        self.history.append(f'User deposited ${amount}')
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.history.append(f'User withdrew ${amount}')
            self.balance -= amount
            return self.balance

        else:
            if self.balance - amount < 0:
                print('sorry you don\'t have that much money')
                return self.balance

    def transaction_history(self):
        return self.history


atm = Atm(0, 0.01)

while True:
    transaction = input('would you like to (check balance, check interest, check history, deposit, withdrawal)\n**type \'goodbye\' if finished**\n')
    if transaction == 'check balance':
        print(f'Your account has ${atm.check_balance()}')
    if transaction == 'deposit':
        amount = int(input('how much would you like to deposit?\n'))
        account = atm.deposit(amount)
    if transaction == 'withdrawal':
        amount = int(input('how much money would you like to take out?\n'))
        account = atm.withdrawal(amount)
    if transaction == 'check interest':
        print(f' Your current acumulated interst is ${atm.check_interest()}')
    if transaction == 'check history':
        print(atm.transaction_history())

    if transaction == 'goodbye':
        print('Have a nice day')
        break