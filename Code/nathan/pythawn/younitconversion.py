unit_conversion = {'mm': 1000, 'cm': 100, 'm': 1, 'km': .001, 'in': 39.37, 'ft': 3.28, 'yd': 1.09}
while True:
    frum = input('pick a base unit of measurement \n >')
    start_ammount = input('how much of your chosen unit \n >')
    start_ammount = int(start_ammount)
    to = input('what unit of measurement do you want to convert to? \n >')
    try:
        end_ammount = (start_ammount/ unit_conversion[frum]) * unit_conversion[to]
        print(end_ammount, to)
        break
    except KeyError:
        print("bad unit")