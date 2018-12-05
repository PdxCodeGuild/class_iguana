"""author: Richard Sherman
2018-12-04
lab11-calculator.py, a simple calculator"""

#simple version
op = input('Which operation would you like to perform (+ - * /)?  ')
num_1 = input('What is the first number?  ')
num_2 = input('What is the second number?  ')
expr = (num_1, op, num_2)
expr = ' '.join(expr)
result = eval(expr)
print(f'{num_1} {op} {num_2} = {result}.')

#with while loop
op = input('Which operation would you like to perform (+ - * /)?  ')
while True:
    num_1 = input('What is the first number?  ')
    num_2 = input('What is the second number?  ')
    expr = (num_1, op, num_2)
    expr = ' '.join(expr)
    result = eval(expr)
    print(f'{num_1} {op} {num_2} = {result}.')
    op = input('Choose another operation or type done to quit:  ')
    if op == 'done':
        print('Goodbye!')
        break

#hoping that the user enters a valid expression
expr = input('Enter an expression using + - * or / to be evaluated:  ')
while True:
    result = eval(expr)
    print(f'{expr} = {result}')
    expr = input('Enter another expression or type done to quit:  ')
    if expr == 'done':
        print('Goodbye!')
        break