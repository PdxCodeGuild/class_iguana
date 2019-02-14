#Lab 22 ARI Scale

#4.71 * (characters/words) + .5 * (words/sentences) -21.43

#1st need #characters, # words
#next need # sentences

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

with open('Plat_Republic.txt', encoding = "utf-8") as f:
    contents = f.read().lower()

# for word in contents:
words = contents.strip().split()
word_count = len(words)
# print(words)
# print(word_count)

characters = contents.strip()
characters = list(characters)
character_count = len(characters)

sentences = contents.strip().split('\n')
sentence_count = len(sentences)

ari_score = round(4.71 * (character_count/word_count) + .5 * (word_count/sentence_count) - 21.43)
if ari_score > 14:
    ari_score = 14

print(f'The ARI for {f.name} is {ari_score}. \n The corresponding grade-level for this score ')
print(f"is {ari_scale[ari_score]['grade_level']} that is suitable for an average person {ari_scale[ari_score]['ages']}")



