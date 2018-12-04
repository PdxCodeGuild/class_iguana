grade = int(input('What percentage did you get on your test? \n'))

if grade >= 96:
    print('Amazing you got an A+')
elif grade == 95:
    print('Pretty good you got an A')
elif grade >= 90:
    print('Nice you got an A-')
elif grade >= 86:
    print('doing good B+')
elif grade == 85:
    print('Good job that\'s a B')
elif grade >= 80:
    print('B- still above average')
elif grade >= 76:
    print('C+')
elif grade >= 75:
    print('Got a C that\'s average')
elif grade >= 70:
    print('C-')
elif grade >= 60:
    print('You got a D you need to apply yourself more')
elif grade <= 59:
    print('You failed your test study harder next time')