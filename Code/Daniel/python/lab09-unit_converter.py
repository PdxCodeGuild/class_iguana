

units = ['in', 'ft', 'y', 'mi', 'm', 'km']


def to_feet(distance, from_unit, to_unit):
    if from_unit == units[1]:
        feet = distance
    elif from_unit == units[0]:
        feet = distance / 12
    elif from_unit == units[2]:
        feet = distance * 3
    elif from_unit == units[3]:
        feet = distance * 5280
    elif from_unit == units[4]:
        feet = distance / 0.3048
    elif from_unit == units[5]:
        feet = distance / .0003048
    
    print(feet)
    from_feet(feet, to_unit)

# Metric to metric has rounding errors do to converting to feet first. Implement rounding for metric

def from_feet(feet, to_unit):
    converted = 0

    if to_unit == units[0]:
        converted = feet * 12
    elif to_unit == units[1]:
        converted = feet
    elif to_unit == units[2]:
        converted = feet * 3
    elif to_unit == units[3]:
        converted = feet / 5280
    elif to_unit == units[4]:
        converted = feet * 0.3048
    elif to_unit == units[5]:
        converted = feet * .0003048

    print('Your distance is: ' + str(converted) + ' ' + str(to_unit))
    quit()


while True:
    try:
        distance = int(input('\nEnter a distance: '))
        from_unit = input('Enter the unit you are converting -from- : [in, ft, y, mi, m, km]: ')
        to_unit = input('Enter the unit you are converting -to- : [in, ft, y, mi, m, km]: ')
        valid_from = False
        valid_to = False

        for i in range(len(units)):
            if from_unit == units[i]:
                valid_from = True
            if to_unit == units[i]:
                valid_to = True

        if valid_from == False or valid_to == False:
           print('\nUnit type error. Enter unit as [in, ft, y, mi, m, km]\n') 
        
        if from_unit == to_unit:
            print('-' * 50)
            print('No conversion necessary! Your distance is ' + str(distance) + ' ' + str(from_unit) + '!\n')
            quit()

        to_feet(distance, from_unit, to_unit)

    except ValueError:
        print('Input error. Enter distance as a number. Try 123.\n')

