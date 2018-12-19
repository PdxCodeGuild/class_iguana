def check_balance(account):
    return account


def check_interest(account, interest):
    return account * interest


def deposit(account, amount):
    return account + amount


def withdrawl(account, amount):
    if account - amount > -1:
        x = account - amount
    else:
        if account - amount < 0:
            print('sorry you dont have that much money')
    return x


def transaction_history(history):
    return history


account = 0
interest = 0.1
amount = 0
history = []
while True:
    transaction = input('would you like to (check balance, check interest, check history, deposit, withdrawl)\n**type finish if finished**\n')
    if transaction == 'check balance':
        print(check_balance(account))
    if transaction == 'deposit':
        amount = int(input('how much would you like to deposit?\n'))
        history.append('deposit')
        history.append(amount)
        account = (deposit(account, amount))
        print(account)
    if transaction == 'withdrawl':
        amount = int(input('how much money do you want to take out?\n'))
        history.append('withdrawl')
        history.append(amount)
        account = (withdrawl(account, amount))
        print(account)
    if transaction == 'check interest':
        print(check_interest(account, interest))
    if transaction == 'check history':
        print(transaction_history(history))
    if transaction == 'finish':
        break







