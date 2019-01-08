"""
author: Richard Sherman
2018-12-08
lab22-ari.py, computes the automated readability index of a text
"""
import re

# use a copy of James Joyce's Ulysses, downloaded from http://www.gutenberg.org
ulysses_txt = open("ulysses.txt").read().lower()

# count characters, words, and sentences to use in calculating ARI
chars = re.findall(r"\w", ulysses_txt)
words = re.findall(r"\b[\w-]+\b", ulysses_txt)
sentences = re.findall(r"[^.]* \w+ [^.]*\.", ulysses_txt)

chars_words = len(chars) / len(words)
words_sentences = len(words) / len(sentences)

ari = int(4.71 * chars_words + 0.5 * words_sentences - 21.43)
# print(ari)

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


print('--------------------------------------------------------\n')
print(f'The ARI for ulysses.txt is {ari}.\n')
print(f'This corresponds to a {ari_scale[ari]["grade_level"]} level of difficulty\nthat is suitable for an average person {ari_scale[ari]["ages"]} years old.')
print('\nIt also suggests that these regression coefficients were drawn from a very peculiar sample, since \nmost fifth graders cannot read James Joyce\'s Ulysses with any meaningful degree of comprehension.')
print('Or perhaps this was just something dreamed up by an Education Ph.D. that needs rethinking.')
print('\n--------------------------------------------------------')
