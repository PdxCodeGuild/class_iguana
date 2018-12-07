#lab_9_unit_conversion_level_2

#receive units and ocnverst to float
input_distance = float(input('What is the distance?:\n'))
input_unit = input('Measured in what?:\n')

#create associations for measurement types.
#round(length_in_meters, 4). Note: i can keep the same variable name after using round() to update the value. for some reason I thought I had to make a new one.
if input_unit == 'mi':
    miles = input_distance * 1609.34
    miles = round(miles, 4)
    print(f'{input_distance} mi is {miles} m')
elif input_unit == 'ft':
    feet = input_distance * 0.3048
    feet = round(feet, 4)
    print(f'{input_distance} ft is {feet} ft')
elif input_unit == 'km':
    kilo = input_distance * 1000
    kilo = round(kilo, 4)
    print(f'{input_distance} km is {kilo} m')

exit()