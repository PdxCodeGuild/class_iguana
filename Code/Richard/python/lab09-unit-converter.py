
"""Author: Richard Sherman
2018-12-04
lab09-unit-converter.py, converts units of distance"""

#note: problems with float arithmetic. Various solutions (integer division, rounding) have undesirable effects.
#better, for purposes of an example, to cast the input as an int, but this works for people who
#understand problems with float arithmetic and those who don't mind very close approximations
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

meters = dist * conv[unit_in]
inches = meters / conv['inch']
feet = meters / conv['foot']
yards = meters / conv['yard']
miles = meters / conv['mile']
# meters = meters / conv['meter']
kilometers = meters / conv['kilometer']

print(f'\n{inches} \t inches \n{feet} \t feet \n{yards} \t yards \n{miles} \t miles \n{meters} \t meters \n{kilometers} \t kilometers')

result = meters / conv[unit_out]
print(f'\n {dist} {unit_in} is {result} {unit_out}')