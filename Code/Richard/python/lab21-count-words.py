"""
author: Richard Sherman
2018-12-06
lab21-count-words.py, counts words in a text and lists frequencies of word-occurrence
"""

import re

ulysses_txt = open("ulysses.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", ulysses_txt)
word_dict = {}
for i in words:
    word_dict[i] = word_dict.get(i, 0) + 1
# print(word_dict)
# list_from_word_dict = list(word_dict.keys())
items = list(word_dict.items())
items.sort(key = lambda tup: tup[1], reverse = True)
print(items[0:10])

# version 2: no idea how to collect word-pairs