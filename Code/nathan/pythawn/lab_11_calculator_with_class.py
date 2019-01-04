class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


math_operation = input('which math operation would you like to perform?(+, -, x, /) \n >')
num1 = int(input('what is your first number?\n >'))
num2 = int(input('what is your second number? \n >'))

calc = Calc(num1, num2)

if math_operation == '+':
    sum = calc.add()
    print(sum)
elif math_operation == '-':
    sum = calc.subtract()
    print(sum)
elif math_operation == '/':
    sum = calc.divide()
    print(sum)
elif math_operation == 'x':
    sum = calc.multiply()
    print(sum)
