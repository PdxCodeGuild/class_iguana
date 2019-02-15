#Lab 21 Count Words

#Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
import string

with open('Grimm.txt', encoding = "utf-8") as f:
    contents = f.read().lower().strip().split()


# for word in contents:
#     word = word.strip()

for i in range(len(contents)):
    contents[i] = contents[i].strip()
# print(contents)
print(len(contents))


word_dict = {}
for word in contents:   #loop/iterate
    if word in word_dict:     #condition = checking if the word is in the dictionary. ok to have this first, thats what confused me.
        word_dict[word] += 1  #to add to a dictionary, its dict_name[key] = value
    else:
        word_dict[word] = 1
# print(word_dict)

# print(len(word_dict))


words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])












#for card in card_deck:
# product_to_price['banana'] = 0.25
    # if card[0] == 'A':
    #     card_dict.update({card : 11})
 # f = open('filename.txt')  # open the file
# contents = f.read()  # read the contents
# print(contents)

# f = open('Grimm.txt', encoding = "utf-8")
# contents = f.read()

#with open('../../1 Python/data/apothecary.txt', 'r', encoding='utf-8') as f:
#     lines = f.read().split('\n')
# print(lines)