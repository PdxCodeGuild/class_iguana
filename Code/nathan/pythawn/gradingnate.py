grade = input('what was your grade? \n>')
grade = int(grade)
if grade >= 90 and grade <=94:
    print('A-')
elif grade >= 80 and grade <=84:
    print('B-')
elif grade >= 70 and grade <=74:
    print('C-')
elif grade >= 60 and grade <=64:
    print('D-')
elif grade >= 50 and grade <=54:
    print('F- oh no')
elif grade <= 96 and grade >=100:
    print('A+ wow')
elif grade <= 86 and grade >=89:
    print('B+')
elif grade <= 76 and grade >=79:
    print('C+')
elif grade <= 66 and grade >=69:
    print('D+')
elif grade <= 56 and grade >=59:
    print('F+')
elif grade == 95:
    print('A')
elif grade == 85:
    print('B')
elif grade == 75:
    print('C')
elif grade == 65:
    print('D')
elif grade == 55:
    print('F')