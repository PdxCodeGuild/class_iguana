import random
print('let\'s play Rock, Paper, Scissors')
pick = input('What\'s your choice Rock type "r", Paper type "p" or Scissors type "s"\n')
z = ['Rock', 'Paper', 'Scissors']
pc = random.choice(z)
print(f'computer picks {pc}')
if pick == 'r' and pc == 'Rock':
    print('it\'s a tie')
elif pick == 'p' and pc == 'Paper':
    print('it\'s a tie')
elif pick == 's' and pc == 'Scissors':
    print('it\'s a tie')
elif pick == 'r' and pc == 'Paper':
    print('You lose, Paper covers Rock.')
elif pick == 'r' and pc == 'Scissors':
    print('You win!! Rock smashes Scissors')
elif pick == 'p' and pc == 'Rock':
    print('You win!! Paper covers Rock')
elif pick == 'p' and pc == 'Scissors':
    print('You lose Scissors cuts paper')
elif pick == 's' and pc == 'Rock':
    print('You lose Rock smashes Scissors')
elif pick == 's' and pc == 'Paper':
    print('You win!! Scissors cut paper')
