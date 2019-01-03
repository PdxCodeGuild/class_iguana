def check_balance(account):
    return account


def check_interest(account, interest):
    return account * interest


def deposit(account, amount):
    return account + amount


def withdrawal(account, amount, history):
    if account - amount < 0:
        print('sorry you don\'t have that much money')
        history.append('<<failed')
        return account
    else:
        return account - amount


def transaction_history(history):
    return history


account = 0
interest = 0.1
amount = 0
history = []
while True:
    transaction = input('would you like to (check balance, check interest, check history, deposit, withdrawal)\n**type \'goodbye\' if finished**\n')
    if transaction == 'check balance':
        print(check_balance(account))
    if transaction == 'deposit':
        amount = int(input('how much would you like to deposit?\n'))
        history.append('deposit')
        history.append(amount)
        account = (deposit(account, amount))
        print(account)
    if transaction == 'withdrawal':
        amount = int(input('how much money would you like to take out?\n'))
        history.append('withdrawal')
        history.append(amount)
        account = withdrawal(account, amount, history)
        print(account)
    if transaction == 'check interest':
        print(check_interest(account, interest))
    if transaction == 'check history':
        print(transaction_history(history))
    if transaction == 'goodbye':
        break







