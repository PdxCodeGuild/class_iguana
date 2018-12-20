#Lab 21 Count Words version 2

#Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
import string

with open('Grimm.txt', encoding = "utf-8") as f:
    contents = f.read().lower().strip().split()

for word in contents:
    word = word.strip()

#create a variable that represents pairs?
pair_tup_list = []

for i in range(len(contents) -1):
    pair_tup = (contents[i], contents[i + 1])
    pair_tup_list.append(pair_tup)

count_word_dict = {}
for pair_tup in pair_tup_list:
    if pair_tup in count_word_dict:
        count_word_dict[pair_tup] += 1
    else:
        count_word_dict[pair_tup] = 1
# print(pair_tup_list)
# print(count_word_dict)

pairs = list(count_word_dict.items())
pairs.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(pairs))):
    print(pairs[i])

