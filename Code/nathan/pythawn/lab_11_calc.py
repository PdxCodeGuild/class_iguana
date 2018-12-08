op = input('what operation would you like to perform? \n >')

num1 = input('what is your first number?\n >')

num2 = input('what is your second number? \n >')

a = int(num1)
b = int(num2)

#def add(a, b):
    #return a + b

#def subtract(a, b):
    #return a - b

#def multiply(a, b):
    #return a * b

#def divide(a, b):
    #return a / b

if op == 'subtract':
    print(a - b)
elif op == 'add':
    print(a + b)
elif op == 'divide':
    print(a / b)
elif op == 'multiply':
    print(a * b)



