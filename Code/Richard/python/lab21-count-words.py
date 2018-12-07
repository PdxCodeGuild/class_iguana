"""
author: Richard Sherman
2018-12-06
lab21-count-words.py, counts words in a text and lists frequencies of word-occurrence
"""

import re

ulysses_txt = open("ulysses.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", ulysses_txt)
num_dict = {}
for i in words:
    num_dict[i] = num_dict.get(i, 0) + 1
# print(num_dict)
# list_from_num_dict = list(num_dict.keys())
items = list(num_dict.items())
items.sort(key = lambda tup: tup[1], reverse = True)
print(items[0:10])
