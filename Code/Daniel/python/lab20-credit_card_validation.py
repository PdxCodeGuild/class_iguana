

try:
    card = (input('Enter your credit card number: ').replace(' ', ''))      # Gets an input for the card number, removing spaces.
    card_num = list(map(int, card))     # Takes that string and changes each digit to an int, storing the digits in a list

    if len(card) == 16:
        check_digit = card_num.pop(15)      # Removes last digit and stores for later verification
        card_num = card_num[::-1]       # Reverses list? Does not impact card verification due to odd number of digits
        for i in range(0, 15, 2):       # Doubles every other digit. Maybe do every third so list reversal has an effect?
            card_num[i] *= 2
        for i, j in enumerate(card_num):        # Subtracts 9 from every digit over 9
            if j > 9:
                card_num[i] -= 9
        sum_digits = sum(card_num)      # Sums of all digits

        if str(check_digit) == str(sum_digits)[1] :     # Compares the check digit to the second digit of the sum. Prints result
            print('Card is Valid.')
        else:
            print('Card is not valid.')

    else:
        print('Not a valid card number. Number should be 16 digits.')


except ValueError:
    print('Not a valid card number.')

