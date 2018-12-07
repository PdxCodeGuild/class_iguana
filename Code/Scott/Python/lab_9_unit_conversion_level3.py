#lab_9_unit_conversion_level_3

#receive units and ocnverst to float
input_distance = float(input('What is the distance?:\n'))
input_unit = input('Measured in what?:\n')
output_unit = input('Converted to?:\n')

#create associations for measurement types. convert them to meters
#round(length_in_meters, 4). Note: i can keep the same variable name after using round() to update the value. for some reason I thought I had to make a new one.
#convert to meters

# miles_in_meters = ''
# feet_in_meters = ''
# kilo_in_meters = ''
# meters = ''

if input_unit == 'mi':
    miles_in_meters = input_distance * 1609.34
    miles_in_meters = round(miles_in_meters, 4)
    #return miles
    # print(f'{input_distance} mi is {miles} m')
if input_unit == 'ft':
    feet_in_meters = input_distance * 0.3048
    feet_in_meters = round(feet_in_meters, 4)
    # return feet
    # print(f'{input_distance} ft is {feet} ft')
if input_unit == 'km':
    kilo_in_meters = input_distance * 1000
    kilo_in_meters = round(kilo_in_meters, 4)
    # return kilo
    # print(f'{input_distance} km is {kilo} m')
if input_unit == 'm':
    meters = round(meters, 4)
    # return meter

#print output unit based on meter conversion to said output unit type
# output_meter = ''
# output_mile = ''
# output_feet = ''
# output_kilo = ''

if output_unit == 'm':
    output_meter = meters
if output_unit == 'mi':
    output_mile = miles_in_meters / 1609.34
if output_unit == 'ft':
    output_feet = feet_in_meters_ / 0.3048
if output_unit == 'km':
    output_kilo = kilo_in_meters / 1000

if input_unit == 'm' and output_unit == 'mi':
    print(f'{input_distance} m is {output_mile} miles.')
if input_unit == 'm' and output_unit == 'ft':
    print(f'{input_distance} m is {output_feet} ft')
if input_unit == 'm' and output_unit == 'km':
    print(f'{input_distance} m is {output_kilo} km' )
if input_unit == 'mi' and output_unit == 'km':
    print(f'{input_distance} miles is {output_mile} km' )
if input_unit == 'mi' and output_unit == 'ft':
    print(f'{input_distance} miles is {output_feet} ft' )
if input_unit == 'mi' and output_unit == 'm':
    print(f'{input_distance} miles is {output_meter} m' )
if input_unit == 'km' and output_unit == 'mi':
    print(f'{input_distance} km is {output_mile} mi' )
if input_unit == 'km' and output_unit == 'm':
    print(f'{input_distance} km is {output_meter} m' )
if input_unit == 'km' and output_unit == 'ft':
    print(f'{input_distance} km is {output_feet} ft' )
if input_unit == 'ft' and output_unit == 'km':
    print(f'{input_distance} ft is {output_kilo} km' )
if input_unit == 'ft' and output_unit == 'mi':
    print(f'{input_distance} ft is {output_mile} mi' )
if input_unit == 'ft' and output_unit == 'm':
    print(f'{input_distance} ft is {output_meter} m' )



exit()