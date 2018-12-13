#Lab_15_number_to_phrase.py
#version 1 = 1 - 99
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
#
# Hint: you can use modulus to extract the ones and tens digit.
#
# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings.

num = int(input('Please enter a number from 0 - 99: \n'))

ones_dict = {0 : 'zero',
              1 : 'one',
              2 : 'two',
              3 : 'three',
              4 : 'four',
              5 : 'five',
              6 : 'six',
              7 : 'seven',
              8 : 'eight',
              9 : 'nine',
              10 : 'tem',
              11 : 'eleven',
              12 : 'twelve',
              13 : 'thirteen',
              14 : 'fourteen',
              15 : 'fifteen',
              16 : 'sixteen',
              17 : 'seventeen',
              18 : 'eighteen',
              19 : 'nineteen'}

tens_dict = {2 : 'twenty',
             3 : 'thirty',
             4 : 'fourty',
             5 : 'fifty',
             6 : 'sixty',
             7 : 'seventy',
             8 : 'eighty',
             9 : 'ninety'}

hundreds_dict = {1 : 'one-hundred',
              2 : 'two-hundred',
              3 : 'three-hundred',
              4 : 'four-hundred',
              5 : 'five-hundred',
              6 : 'six-hundred',
              7 : 'seven-hundred',
              8 : 'eight-hundred',
              9 : 'nine-hundred'}

if num <= 19:
    phrase = ones_dict[num]

elif num <= 99 and num > 19:
    tens_digit = num // 10
    ones_digit = num % 10
    phrase = tens_dict[tens_digit] + '-' + ones_dict[ones_digit]

elif num > 99:
    hundreds_digit = num // 100
    num = num - (hundreds_digit * 100)
    tens_digit = num // 10
    ones_digit = num % 10
    phrase = hundreds_dict[hundreds_digit] + '-' + tens_dict[tens_digit] + '-' + ones_dict[ones_digit]

print(phrase)

# *************************************************************************************
# elif num > 99:
#     hundreds_digit = num // 100
#     tens_digit = num // 10
#     ones_digit = num % 10
#
#
#
#
# hundreds_dict[hundreds_digit] + '-' +
# hundreds_digit = num // 100
# import string
# tens_list = list(string.digits)
# print(tens_list)
# def calc_payout(ticket, winners):
#
#     n_matches = 0
#     for i in range(6):
#         if ticket[i] == winners[i]:
#             n_matches += 1
#
#     payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
#         return payout[n_matches]
