import math

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

word_list = []
char_count = 0
sentence_count = 0
word_list = open('huckleberry.txt').read().split()
#word count
for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()
word_count = (len(word_list))
#character count
for characters in word_list:
    char_count += len(characters)
#sentence count
for characters in word_list:
    if '.' in characters:
        sentence_count += 1
    if '?' in characters:
        sentence_count += 1
    if '!' in characters:
        sentence_count += 1
#ari math
math1 = (char_count / word_count) * 4.17
math2 = (word_count / sentence_count) * 0.5
ari = math1 + math2 - 21.43
ari = math.ceil(ari)
#using ari math to access dictionary
print(ari_scale[ari])








