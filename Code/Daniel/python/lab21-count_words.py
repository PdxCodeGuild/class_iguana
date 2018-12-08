import re
import math


book = open('brothers_karamazov.txt', encoding='utf-8')

edited_book = [] 
for word in book:
    word = (re.sub('[^a-zA-Z0-9 ]', '', word).lower())

    if ' ' in word:
        word_list = word.split(' ')
        edited_book += word_list
    else:
        edited_book.append(word)


clean_book = []
for i, item in enumerate(edited_book):
        if item != '':
            clean_book.append(item)

book.close()

counter = {}
for word in clean_book:
    if word in counter:
        counter[word] += 1 
    else:
        counter[word] = 1

words = list(counter.items())
words.sort(key=lambda tup: tup[1], reverse=True)

top_ten = []
for i in range(min(10, len(words))):  
    top_ten.append(words[i])




# num_combos = int(math.factorial(len(top_ten))/(2*math.factorial(len(top_ten)-2)))
combo_counter = {}
for i in range(len(top_ten)):
    for k in range(len(top_ten)):
        for j, word in enumerate(clean_book):
            # if i == 0:
            if i == k:
                continue
            combo1 = top_ten[i][0] + top_ten[k][0] 
            #     combo2 = ''
            # elif i == len(top_ten) - 1:
            #     combo1 = ''
            #     combo2 = top_ten[i][0] + top_ten[i-1][0]
            # else:
            #     combo1 = top_ten[i][0] + top_ten[i+1][0] 
            #     combo2 = top_ten[i][0] + top_ten[i-1][0]

            wombo_combo = word + clean_book[j+1]
            if wombo_combo == combo1 or wombo_combo == combo2:
                if 


        


