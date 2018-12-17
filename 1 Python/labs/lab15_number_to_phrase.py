



def num_converter(user_num):
    converted_nums_1_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                      'twenty']
    cn20plus = ['zero','one','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty',]
    user_num = int(user_num)
    if (user_num) <= 20:
        return converted_nums_1_20[user_num]
    elif user_num > 20:
        ones_digit = user_num % 10
        tens_digit = user_num // 10
        ones_printed = converted_nums_1_20[ones_digit]
        tens_printed = cn20plus[tens_digit]
        user_num = tens_printed + ones_printed

        return user_num







user_num = input('What\'s your number?')
print(num_converter(user_num))