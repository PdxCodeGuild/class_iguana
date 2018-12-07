#lab_9_unit_conversion

#Receive amount measured in feet via user input as a float

length_in_feet = float(input('Give a length in measured in feet:\n'))

#convert feet to meters: x 0.3048

length_in_meters = length_in_feet * 0.3048

#round the result using the 'round(value, dec) function. Note. need to create a new variable as 'round' function does not modify the value.
length_in_meters_rounded = round(length_in_meters, 4)

print(f'{length_in_feet} feet is {length_in_meters_rounded} meters.')
