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

    def _check_balance_(self, balance):
        self.balance = balance
        print(f'Your current balance is {balance}')

    def _deposit_(self, amount, balance):
        self.amount = amount
        ATM.balance = balance
        balance += amount
        return balance

    def _check_withdraw_(self, amount, balance):
        self.amount = amount
        ATM.balance = balance
        balance -= amount
        if balance > 0:
            print(f'You will have enough to cover this withdraw')
        else:
            print(f'You do not have enough to cover this withdraw.')

    def _withdraw_(self, amount, balance):
        self.amount = amount
        ATM.balance = balance
        balance -= amount
        return balance

    def _calculate_int_(self, balance, interest_rate):
        ATM.interest_rate = interest_rate
        ATM.balance = balance
        amount_interest = interest_rate * balance
        return amount_interest


request = input('What would you like to do? Check your balance? (type \'balance\') Make a deposit? (type \'deposit \') Make a withdraw? (type \'withdraw\' View your accrued interest?'
                '(type \'interest\'):  ')
if request == 'balance':
    ATM.check_balance()
elif request == 'deposit':
    ATM.deposit()
elif request == 'withdraw':
    ATM.withdraw()
elif request == 'interest':
    ATM.calculate_int()








