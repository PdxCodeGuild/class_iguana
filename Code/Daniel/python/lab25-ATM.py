

class Atm:
    def __init__(self):
        self.balance = 0
        self.interest_rate = .001
        self.transactions = 'End of Transactions'

    def check_balance(self):
        return self.balance / 100


    def deposit(self, amount):
        amount = convert_to_cents(amount)
        if amount is not None:
            self.balance += amount
            self.transactions = f'User deposited ${amount/100}\n' + self.transactions  
            print('Deposit successful!')


    def check_withdrawal(self, amount):
        return self.balance - amount >= 0


    def withdraw(self, amount):
        amount = convert_to_cents(amount)
        if amount is not None:
            if self.check_withdrawal(amount) == True:
                self.balance -= amount
                self.transactions = f'User withdrew ${amount/100}\n' + self.transactions
                print(f'Withdrew ${amount/100}')
                return self.balance, amount / 100
            else:
                print('Not enough funds')
    


    def calc_interest(self):
        pass


    def print_transactions(self):
        return self.transactions


def check_command(command):
    command = command.replace(' ', '') 

    if command.isalpha() == True:
        command = command.lower()
        if command == 'd' or command == 'deposit':
            return 'd' 
        elif command == 'w' or command == 'withdraw':
            return 'w' 
        elif command == 'c' or command == 'checkbalance':
            return 'c' 
        elif command == 'h' or command == 'history':
            return 'h' 


def convert_to_cents(amount):
    amount = amount.replace('$', '')
    
    if amount.replace('.', '', 1).isdigit() == True:
        if '.' in amount:
            amount = '0' + amount + '00'
            # try:
            dollars, cents = amount.split('.')
            # except ValueError:
            #     amount += '0'
            #     dollars, cents = amount.split('.')
        else:
            dollars = amount
            cents = 0

        if int(cents) > 99: 
            cents = cents[:2]

        total = int(dollars) * 100 + int(cents)
        return total
    else:
        print('Not a valid amount')


    

user = Atm()



while True:
    command = check_command(input('\nWhat would you like to do? Options: (d)eposit, (w)ithdraw, (c)heck balance, (h)istory\t'))

    if command == 'd':
        user.deposit(input('Enter an amount to deposit: '))
    elif command == 'w':
        user.withdraw(input('Enter an amount to withdraw: '))
    elif command == 'c':
        print(f'Current Balance: ${user.check_balance()}')
    elif command == 'h':
        print(user.print_transactions())