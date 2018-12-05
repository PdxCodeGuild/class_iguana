import random

def generate_six():
    ticket = []
    
    for i in range(6):
        ticket.append(random.randint(1, 99))
    
    return ticket


balance = 0
earnings = 0
golden_ticket = generate_six()
num_matches = 0
num_tickets = 100000
expenses = num_tickets * 2

for i in range(num_tickets):
    num_matches = 0
    ticket = generate_six()

    num_matches += len([i for i, j in zip(golden_ticket, ticket) if i == j])

    if num_matches == 6:
        earnings += 25000000
    elif num_matches == 5:
        earnings += 1000000
    elif num_matches == 4:
        earnings += 50000
    elif num_matches == 3:
        earnings += 100
    elif num_matches == 2:
        earnings += 7
    elif num_matches == 1:
        earnings += 4
    else:
        continue
    

balance = earnings - expenses
roi = str(int(((earnings - expenses) / expenses) * 100)) + '%'
print('Earnings: ' + str(earnings) + '\nExpenses: ' + str(expenses) + '\nROI: ' + roi + '\nBalance: ' + str(balance))

