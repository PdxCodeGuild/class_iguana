

tens_list = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ones_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def get_digits(number):
    digits = []
    digits.append(number // 100)
    if number > 99:
        number -= digits[0] * 100
    digits.append(number // 10)
    digits.append(number % 10)

    return digits

try:
    number = int(input('Enter a number from 1 to 999: '))

    if 0 < number < 1000:
        digits = get_digits(number)
        phrase = ''    

        if digits[0] != 0:
            phrase += str(ones_list[digits[0]]) + ' hundred '
        if digits[1] == 1: 
            phrase += str(teens_list[digits[2]])
        else:
            phrase += str(tens_list[digits[1]])
            if digits[1] != 0 and digits[2] != 0:
                phrase += '-'
            phrase += str(ones_list[digits[2]])
    
        print(phrase)

    else:
        print('Number out of range')

except ValueError:
    print('Not a valid number')
