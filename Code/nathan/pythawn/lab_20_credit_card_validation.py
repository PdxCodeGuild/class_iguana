def cc_validation(a):
    a = list(a)
    for i in range(len(a)):
        a[i] = int(a[i])
    check_digit = a[len(a)-1]
    a = a[:-1]
    a = a[::-1]
    for i in range(0, len(a), 2):
        a[i] *= 2
    for i in range(len(a)):
        if a[i] > 9:
            a[i] -= 9
    a = sum(a)
    a = str(a)
    a = list(a)
    for i in range(len(a)):
        a[i] = int(a[i])
    a = a[:-1]
    a = sum(a)
    if a == check_digit:
        print('valid')
    else:
        print(' not valid ')
    return a


number = input('okay, I have your social security, can i have your credit card number now?\n')
print(cc_validation(number))

