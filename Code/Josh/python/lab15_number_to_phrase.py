



def num_converter(user_num):
    converted_nums_1_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                      'twenty']
    cn20plus = ['','one','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty',]
    cn100 = ['0','onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
    user_num = int(user_num)
    ones_digit = user_num % 10
    tens_digit = (user_num % 100) // 10
    hundreths_digit = user_num // 100
    ones_printed = converted_nums_1_20[ones_digit]
    tens_printed = cn20plus[tens_digit]
    hundreths_printed = cn100[hundreths_digit]
    if (user_num) <= 20:
        return converted_nums_1_20[user_num]
    elif user_num > 20 and user_num < 100:
        if ones_digit == 0:
            return tens_printed
        return tens_printed + ones_printed
    elif user_num >= 100:
        if ones_digit == 0 and tens_digit == 0:
            return cn100[hundreths_digit]
        if tens_digit == 1:
            teenage_number = int(str(tens_digit) + str(ones_digit))
            return cn100[hundreths_digit] + converted_nums_1_20[teenage_number]
        if ones_digit == 0 and tens_digit != 0:
            return hundreths_printed + tens_printed
        return hundreths_printed + tens_printed + ones_printed
user_num = input('What\'s your number?\n>>')
print(num_converter(user_num))