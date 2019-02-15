# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:
#
# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

class ATM:
    def __init__(self, balance=0, interest_rate=.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def __repr__(self):
        return f'balance: {self.balance}'

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'user deposited ${amount}')

    def check_withdraw(self, amount):
        if self.balance - amount > 0:
            print(f'You will have enough to cover this withdraw')
        else:
            print(f'You do not have enough to cover this withdraw.')

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'user withdrew {amount}')
        return amount

    def calculate_int(self, balance, interest_rate):
        self.balance += self.balance * self.interest_rate
        self.transactions.append(f'user earned ')
        return self.balance

atm = ATM()

while True:
    request = input(
        'What would you like to do? Check your balance? (type \'balance\') Make a deposit? (type \'deposit \') Make a withdraw? (type \'withdraw\')  View your accrued interest?'
        '(type \'interest\'),  Or enter \'done\':  ')

    if request == 'done':
            break

    if request == 'balance':
        print(f'Your account balance is {atm.check_balance()}')
    elif request == 'deposit':
        amount = float(input('What is the amount you would like to deposit?'))
        atm.deposit(amount)
    elif request == 'withdraw':
        amount = float(input('What amount would you like to withdraw?'))
        atm.withdraw(amount)
    elif request == 'interest':
        atm.calculate_int()
    elif request == 'check withdraw':
        ask_amount = float(input("How much do you need to withdraw?"))
        if ask_amount <
        atm.check_withdraw(amount)








