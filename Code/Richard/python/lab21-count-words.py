"""
author: Richard Sherman
2018-12-06
lab21-count-words.py, counts words in a text and lists frequencies of word-occurrence
"""

# note: change to use -with- when opening files

import re
import string   # unnecessary

# version 1, using regexp
ulysses_txt = open("ulysses.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", ulysses_txt)
word_dict = {}
for i in words:
    word_dict[i] = word_dict.get(i, 0) + 1  # just barely understand .get method on dictionary
print(word_dict)
# list_from_word_dict = list(word_dict.keys())
items = list(word_dict.items())
#print(items)
items.sort(key = lambda tup: tup[1], reverse = True)    # don't really understand this
print(f'\n\n--->{items[0:10]}')

# version 2: no idea how to collect word-pairs

# version 0, without regexp:    # note: don't understand why the results differ from those with regexp

ulysses_txt = open("ulysses.txt").read().lower()
ulysses_txt = ulysses_txt.replace(string.punctuation, '')
ulysses_txt = ulysses_txt.replace(string.digits, '')
words = ulysses_txt.split(' ')
word_dict = {}
for i in words:
    word_dict[i] = word_dict.get(i, 0) + 1
print(word_dict)
# list_from_word_dict = list(word_dict.keys())
items = list(word_dict.items())
#print(items)
items.sort(key = lambda tup: tup[1], reverse = True)
print(f'\n\n--->{items[0:10]}')