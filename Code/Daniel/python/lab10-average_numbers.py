# Typo when mode occurances is 1. Add if/else statement 

def calculate(numbers):

# average
    sum_numbers = 0

    for i in numbers:
        sum_numbers += i
    avg = sum_numbers / len(numbers) 
    print('\nThe average is: ' + str(avg))

# median 
    numbers.sort()
    length = len(numbers)

    if length % 2 == 0:
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        median = numbers[length // 2]

    print('The median is ' + str(median))

# mode
    mode_dict = dict()

    for i in numbers:
        if i in mode_dict:
            mode_dict[i] += 1
        else:
            mode_dict[i] = 1
    
    occurance = sorted(mode_dict.values(), reverse = True)[0]
    mode = [number for number, occur in mode_dict.items() if occur == occurance]

    print('The mode is ' + str(mode) + ' with ' + str(occurance) + ' occurances\n')

i = 0
numbers = []

print('\nType "done" to calculate\n')

while True:

    try:
        numbers.append(input('Enter a number: '))
        if numbers[i] == 'done':
            numbers.remove('done')
            calculate(numbers)
            break
        else:
            numbers[i] = int(numbers[i])
            i += 1

    except ValueError:
        print('Not a valid number')
        numbers.remove(numbers[i])
        
    

