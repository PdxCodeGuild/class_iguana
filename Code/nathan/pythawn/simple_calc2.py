#overly complex simple calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


math_operation = input('which math operation would you like to perform? \n >')
num1 = input('what is your first number?\n >')
num2 = input('what is your second number? \n >')

a = int(num1)
b = int(num2)

if math_operation == '+':
    sum = add(a, b)
    print(sum)
elif math_operation == '-':
    sum = subtract(a, b)
    print(sum)
elif math_operation == '/':
    sum = divide(a, b)
    print(sum)
elif math_operation == '*':
    sum = multiply(a, b)
    print(sum)


