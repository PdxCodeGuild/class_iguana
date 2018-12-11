"""Author: Richard Sherman
2018-12-03
grades.py, turns numerical grades into letter grades"""

grade = 'not recorded yet. Your numerical score has to be between 0 and 100.'
while grade == 'not recorded yet. Your numerical score has to be between 0 and 100.':
    score = int(input('Please tell me your numerical score: '))
    if score == 100:
        print('Your grade is A+')
        exit()
    elif score > 89 and score < 100:
        grade = 'A'
    elif score > 79 and score < 90:
        grade = 'B'
    elif score > 69 and score < 80:
        grade = 'C'
    elif score > 59 and score < 70:
        grade = 'D'
    elif score < 60:
        grade = 'F'
    else:
        grade = 'not recorded yet. Your numerical score has to be between 0 and 100.'
        print(f'Your grade is {grade}')

if grade != 'F':
    if score % 10 >= 6:
        grade = grade + '+'
    elif score % 10 <= 4:
        grade = grade + '-'
print(f'Your grade is {grade}')

# todo: fix with Matthew's suggestions
# done