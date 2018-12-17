import random

def pick6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))
    return nums

winning_numbers = pick6()
balance = 0
for i in range(100000):
    ticket_number = pick6()
    balance -= 2
    # print(winning_numbers)
    # print(ticket_number)

    # find the number of matches
    n_matches = 0
    for j in range(6):
        if ticket_number[j] == winning_numbers[j]:
            n_matches += 1

    # calculate payout
    if n_matches == 1:
        balance += 4
    if n_matches == 2:
        balance += 7
    if n_matches == 3:
        balance += 100
    if n_matches == 4:
        balance += 50000
    if n_matches == 1000000:
        balance += 4
    if n_matches == 6:
        balance += 25000000
print('wow you gambled 100 thousand times, your balance is')
print(balance)
earnings = 0
expenses = 0
if balance > 0:
    earnings = balance
    expenses = expenses + balance
elif balance < 0:
    expenses = balance
    earnings = earnings + balance
ROI = (earnings - expenses)/expenses
print('ROI')
print(ROI)




    #The ROI (return on investment) is defined as (earnings - expenses)/expenses.
    #Calculate your ROI, print it out along with your earnings and expenses.



