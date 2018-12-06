"""
author: Richard Sherman
2018-12-05
lab15-num-to-phrase.py, converts numbers to numerals (words)
also tries to convert to roman numerals
"""

# create a dict from numbers to numerals, in parts

numbers = list(range(0,100))
tens_list = []
digits_list = []
for i in numbers:
    tens = i // 10
    digits = i % 10
    tens_list.append(tens)
    digits_list.append(digits)
numerals = {
            0   : '',
            1   :   'one',
            2   :   'two',
            3   :   'three',
            4   :   'four',
            5   :   'five',
            6   :   'six',
            7   :   'seven',
            8   :   'eight',
            9   :   'nine',
            10  :   'ten',
            11  :   'eleven',
            12  :   'twelve',
            13  :   'thirteen',
            14  :   'fourteen',
            15  :   'fifteen',
            16  :   'sixteen',
            17  :   'seventeen',
            18  :   'eighteen',
            19  :   'nineteen'
            }

tens =      {
            2  :   'twenty',
            3  :   'thirty',
            4  :   'forty',
            5  :   'fifty',
            6  :   'sixty',
            7  :   'seventy',
            8  :   'eighty',
            9  :   'ninety'
            }


number = int(input('Please enter an integer between 0 and 99 (inclusive): '))
if number < 20:
    word = numerals[number]
if number > 19:
    word = tens[number // 10] + '-' + numerals[number % 10]
print(f'\n{number}\t:\t{word}')

if number > 99:
    if number % 100 < 20:
        word = numerals[number // 100] + ' hundred ' + numerals[number % 10]
    elif number % 100 > 19:
        word = numerals[number // 100] + ' hundred ' + tens[numerals[number $ 100]
