# while True:
#     operation = input('What opperation would you like to perform? type \'+\' for addition \'-\' for subtraction \'*\' for multiplication or \'/\' for division.\n If you would like to exit type \'done\'\n>')
#     if operation == 'done':
#         break
#     first_num = input('What is the first number?\n>')
#     second_num = input('What is the second number?\n>')
#     if operation == '+':
#         print(f'{first_num} + {second_num} =', int(first_num) + int(second_num))
#     if operation == '-':
#         print(f'{first_num} - {second_num} =', int(first_num) - int(second_num))
#     if operation == "*":
#         print(f'{first_num} * {second_num} =', int(first_num) * int(second_num))
#     if operation == '/':
#         print(f'{first_num} / {second_num} =', int(first_num) / int(second_num))
while True:
    problem = input('What\'s your math problem?\n if finished type \'done\'>')
    if problem == 'done':
        break
    print(eval(problem))