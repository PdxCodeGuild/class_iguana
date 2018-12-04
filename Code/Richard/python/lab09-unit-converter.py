
"""Author: Richard Sherman
2018-12-04
lab09-unit-converter.py, converts units of distance"""

#note: problems with float arithmetic. Rounding to two digits (x.xx) is a kludge
conv =  {
        'inch'    :   0.0254,
        'foot'    :   0.3048,
        'yard'    :   0.9144,
        'mile'    :   1609.34,
        'meter'   :   1,
        'kilometer' : 1000
        }

dist = float(input('What is the distance? '))
unit_in = input('What is the original unit?\n\tPlease choose between:\tinch\tfoot\tyard\tmile\tmeter\tkilometer -----------> ?  ')
unit_out = input('What is the desired unit?\n\tPlease choose between:\tinch\tfoot\tyard\tmile\tmeter\tkilometer -----------> ?  ')

meters = round(dist * conv[unit_in], 2)
inches = round(meters / conv['inch'], 2)
feet = round(meters / conv['foot'], 2)
yards = round(meters / conv['yard'], 2)
miles = round(meters / conv['mile'], 2)
# meters = meters / conv['meter']
kilometers = round(meters / conv['kilometer'], 2)

print(f'\n{inches} \t inches \n{feet} \t feet \n{yards} \t yards \n{miles} \t miles \n{meters} \t meters \n{kilometers} \t kilometers')

result = round(meters / conv[unit_out], 2)
print(f'\n {dist} {unit_in} is {result} {unit_out}')