#lab_11_simple_calculator_version2.py
#lab_11_simple_calculator_lvl_1
#operator_dict = {'+': +,}


operator = input("What type of calculation would you like to do? Please enter '+', '-', '**', or '/' :")

operand_a = input('Please enter the first number:')
operand_b = input('Please enter the second number:')

operand_a = float(operand_a)
operand_b = float(operand_b)

if operator == '+':
    result = operand_a + operand_b
    print(f'Answer: {result}')
elif operator == '-':
    result = operand_a - operand_b
    print(f'Answer: {result}')
elif operator == '*':
    result = operand_a * operand_b
    print(f'Answer: {result}')
elif operator == '/':
    result = operand_a / operand_b
    print(f'Answer: {result}')

while True:
    operator = input("Please enter '+', '-', '**', or '/' or if you are finished, type 'done'")
    if operator == 'done':
        print('Goodbye.')
        break


