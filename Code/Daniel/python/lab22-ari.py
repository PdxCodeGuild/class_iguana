import re

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

file_name = 'brothers_karamazov.txt'
# f = open(file_name, encoding='utf-8')


# text = ''
# char = 0
# for word in f:                          # Replacing any new lines and creating a large string to work with
#     word = word.replace('\n', ' ')      
#     text += word
    
# while '  ' in text:                     # Replacing all repeat spaces
#     text = text.replace('  ', ' ')

with open(file_name, encoding='utf-8') as file:
    text = file.read()

char = len(re.findall('[a-zA-Z0-9]', text))
num_words = len(re.findall(' ', text))
num_sent = len(re.findall('([.!?]\s+[A-Z\"“])|([.!?](\"|”)\s+[A-Z])', text))




# num_words = len(text.split(' '))        # Getting the number of words by splitting on a space
# num_sent = 0
# for character in text:                                                  
#     if character == '.' or character == '?' or character == '!':        # Get number of sentences by spliting on '?', '!', or '.'
#         num_sent += 1
#     if character.isalpha() == True or character.isdigit() == True:      # Get number of characters 
#         char += 1


score = int(-(-(char / num_words * 4.17 + num_words / num_sent * 0.5 - 21.43) // 1))    # Calculate score and round up

if score == 9 or score == 12:   # Account for grammatical differences in grade return string
    a = 'an'
else:
    a = 'a'

score_dict = ari_scale.get(score)
grade = score_dict.get('grade_level')
age = score_dict.get('ages')

print(f'\nThe ARI for {file_name} is {score}\nThis corresponds to {a} {grade} level of difficulty\n' +
      f'that is suitable for an average person {age} years old.\n')

