from math import * 

print('-' * 50 + '\nType "done" to quit\n' + '-' * 50 )

while True:
    try:
        expression = input('\nEnter a math expression using [+, -, *, /] operators: ') 
        if expression == 'done':
                    break
        answer = eval(expression, {'__builtins__': None})
        print(answer)
        
    except:
        print('\nInvalid expression\n')