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
import string
book = 'the_turn_of_the_screw.txt'
with open(book, 'r', encoding='utf-8') as f:
    sentences = f.read().lower().split('.')
for i in range(len(sentences)):
    for char in string.punctuation:
        sentences[i] = sentences[i].replace(char, '')
    sentences[i] = sentences[i].replace('\n', '')
with open(book, 'r', encoding='utf-8') as f:
    words = f.read().lower().split()
for i in range(len(words)):
    for char in string.punctuation:
        words[i] = words[i].replace(char, '')
    words[i] = words[i].replace('\n', '')
word_count = 0
char_count = 0
sentence_count = 0
for sen in sentences:
    sentence_count += 1
for word in words:
    word_count += 1
    for char in word:
        char_count += 1
ARI = 4.71 * round(char_count/word_count)+0.5 * round(word_count/sentence_count)-21.43


print(word_count)
print(char_count)
print(sentence_count)
print(ARI)


ARI = round(ARI)
print(f'The ARI for {book} is {ARI} This corresponds to a {ari_scale[ARI]["grade_level"]}level of difficulty that is suitable for an average person {ari_scale[ARI]["ages"]} years old')
