

def convert_penny():
    try:
        pennies = int(input('How many pennies do you have? '))
        dollar = pennies // 100
        extra = pennies % 100
        if extra < 10:
            extra = "0" + str(extra)
        total = '$' + str(dollar) + '.' + str(extra) 

        print('\nYou have ' + total + '.')
        return pennies

    except ValueError:
        print('Penny amount does not compute... Shutting down\n')
        quit()

def convert_dollar():

    try:
        total = input('How much money do you have? ')
        total = total.replace('$','')
        dollar = int(total.split('.')[0])

        try:
            extra = int(total.split('.')[1])
        except:
            extra = 0

        pennies = dollar * 100 + extra

        print('\nYou have ' + str(pennies) + ' pennies.')
        return pennies
    
    except ValueError:
        print('Dollar amount does not compute... Shutting down\n')
        quit()

def make_change():

    while True:
        amount = input('\nWould you like to convert a penny amount or dollar amount? (p/d) ')

        if amount == 'p':
            pennies = convert_penny()
            break
        elif amount == 'd':
            pennies = convert_dollar()
            break
        else:
            print('-' * 50 + '\nNot a valid choice. Please enter "p" for penny or "d" for dollar\n' + '-' * 50)


    quarters = pennies // 25
    pennies -= quarters * 25
    dimes = pennies // 10
    pennies -= dimes * 10
    nickels = pennies // 5
    pennies -= nickels * 5

    print('That equals ' + str(quarters) + ' quarters, ' + str(dimes) + ' dimes, ' + str(nickels) + ' nickels, and ' + str(pennies) + ' pennies.\n')

make_change()