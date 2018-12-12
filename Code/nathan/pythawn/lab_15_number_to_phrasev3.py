def obtain1_digit(x):
    return x % 10


def obtain10_digit(y):
    return y // 10 % 10


def obtain100_digit(z):
    return z // 100


ones_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                  7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                  13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                  18: 'eighteen', 19: 'nineteen'}

tens_dict = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty',
             9: 'ninety'}

hundreds_dict = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred',
                 5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred',
                 9: 'nine hundred'}

number = int(input('give me a number\n'))



if number < 20:
    print(ones_dict[number])
elif number < 100:
    ones_digit = obtain1_digit(number)
    if ones_digit == 0:
        print(tens_dict[obtain10_digit(number)])
    else:
        tens_num = (tens_dict[obtain10_digit(number)]) + '-' + (ones_dict[obtain1_digit(number)])
        print(tens_num)
elif number < 1000:
    hundreds_num = obtain1_digit(number)
    if hundreds_num == 0:
        print(hundreds_dict[obtain100_digit(number)])
    else:
        hundreds_num = (hundreds_dict[obtain100_digit(number)]) + '-' + (tens_dict[obtain10_digit(number)]) + '-' + (ones_dict[obtain1_digit(number)])
        print(hundreds_num)
else:
    print('that\'s too high, sorry .-. im still learning how to read')





