def cc_validation(a):
    a = list(a)   #turn input into list
    for i in range(len(a)):
        a[i] = int(a[i])   #turn list into integers
    check_digit = a[len(a)-1]  # remove last index of list and store in check digit
    a = a[:-1]
    a = a[::-1]   #reverse list
    for i in range(0, len(a), 2):
        a[i] *= 2 #multiply every other index by 2
    for i in range(len(a)):
        if a[i] > 9:
            a[i] -= 9   #subtract nine from every index greater than nine
    a = sum(a)   #sum of list
    a = str(a)   #make sum into string so it can convert back to list
    a = list(a)  #list sum
    for i in range(len(a)):
        a[i] = int(a[i])  #make sum list into integer
    a = a[:-1]   #take off second digit of sum list
    a = sum(a)  #make sum list back into integer
    if a == check_digit:  #check if single digit is equal to stored check digit
        print('valid')
    else:
        print(' not valid ')
    return a


number = input('okay, I have your social security, can i have your credit card number now?\n')
print(cc_validation(number))

