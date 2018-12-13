# Lab_14_Pick_6

import random

winning_ticket = [random.randint(0, 99) for i in range(6)]          # Generate a list of 6 random numbers representing the winning tickets
print(winning_ticket)

balance = 0 # Start your balance at 0
winnings = 0

# Loop 100,000 times, for each loop:
for round in range(100000): # <---- when using 'in range' use upper bound inclusive. This is not referencing indexes.
    ticket = [random.randint(0, 99) for i in range(6)]
    print(ticket)

    balance -= 2                    # Subtract 2 from your balance (you bought a ticket)
    match_count = 0                   # Find how many numbers match
    for i in range(6):
        if ticket[i] == winning_ticket[i]:
            match_count += 1
            # print(f'you had {match_count} matches!')

# if 1 number matches, you win $4,# if 2 numbers match, you win $7,# if 3 numbers match, you win $100,# if 4 numbers match, you win $50,000,# if 5 numbers match, you win $1,000,000,# if 6 numbers match, you win $25,000,000

    if match_count == 1:                         # Add to your balance the winnings from your matches
        balance += 4
        winnings += 4
    if match_count == 2:
        balance += 7
        winnings += 7
    if match_count == 3:
        balance += 100
        winnings += 100
    if match_count == 4:
        balance += 50000
        winnings += 50000
    if match_count == 5:
        balance += 1000000
        winnings += 1000000
    if match_count == 6:
        balance += 25000000
        winnings =+ 25000000

print(f' your total winnings was ${float(winnings)}')
print(f' final balance = ${float(balance)}')              # After the loop, print the final balance


#you had {   } winning tickets for a total of {  }