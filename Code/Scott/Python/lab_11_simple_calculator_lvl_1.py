#lab_11_simple_calculator_lvl_1
#operator_dict = {'+': +,}
operator = input("What type of calculation would you like to do? Please enter '+', '-', '**', or '/' :")
operand_a = input('Please enter the first number:')
operand_b = input('Please enter the second number:')

operand_a = float(operand_a)
operand_b = float(operand_b)

while True:
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
    break





