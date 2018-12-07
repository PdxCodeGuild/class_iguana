"""
author: Richard Sherman
2018-12-06
lab21-count-words.py, counts words in a text and lists frequencies of word-occurrence
"""
# make a list of the words, put their counts in a dict, sort to get the most frequent
# note: change to use -with- when opening files

import re
import string

# version 1, using regexp

ulysses_txt = open("ulysses.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", ulysses_txt)
word_dict = {}
for i in words:
    word_dict[i] = word_dict.get(i, 0) + 1
print(word_dict)
# list_from_word_dict = list(word_dict.keys())
items = list(word_dict.items())
#print(items)
items.sort(key = lambda tup: tup[1], reverse = True)
print(f'\n\nThe most frequent words, with their frequencies, are:\n{items[0:10]}')

# version 2, collecting word pairs

word_pairs = []
for i in range(len(words)-1):
    word_pairs.append((words[i], words[i+1]))
word_pair_dict = {}
for i in word_pairs:
    word_pair_dict[i] = word_pair_dict.get(i, 0) + 1
# print(word_pair_dict)
# list_from_word_dict = list(word_dict.keys())
items = list(word_pair_dict.items())
#print(items)
items.sort(key = lambda tup: tup[1], reverse = True)
print(f'\n\nThe most frequent word pairs, with their frequencies, are:\n{items[0:10]}')



# version 0, without regexp:    # note: don't understand why the results differ from those with regexp

ulysses_txt = open("ulysses.txt").read().lower()
ulysses_txt = ulysses_txt.replace(string.punctuation, '')
ulysses_txt = ulysses_txt.replace(string.digits, '')
words = ulysses_txt.split(' ')
word_dict = {}
for i in words:
    word_dict[i] = word_dict.get(i, 0) + 1
# print(word_dict)
# list_from_word_dict = list(word_dict.keys())
items = list(word_dict.items())
#print(items)
items.sort(key = lambda tup: tup[1], reverse = True)
print(f'\n\nThe most frequent words, with their frequencies, are:\n{items[0:10]}')