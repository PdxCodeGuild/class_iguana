import re


book = open('brothers_karamazov.txt', encoding='utf-8')

# Strip formatting and get book as a list of words
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


# Count the occurance of each word in book
counter = {}
for word in clean_book:
    if word in counter:
        counter[word] += 1 
    else:
        counter[word] = 1

# Convert dict to list and sort in descending order
words = list(counter.items())
words.sort(key=lambda tup: tup[1], reverse=True)

top_ten = []
for i in range(min(10, len(words))):  
    top_ten.append(words[i])



# Loops for each pair of words in the top 10 list. Adds 1 to a dictionary value for that pair if an occurance is found
combo_counter = {}
for i in range(len(top_ten)):
    for k in range(i + 1, len(top_ten)):
        combo1 = top_ten[i][0] + top_ten[k][0]
        combo2 = top_ten[k][0] + top_ten[i][0]

        if i == k:
            continue

        for j in range(len(clean_book)-1):
            wombo_combo = clean_book[j] + clean_book[j+1]
            pair = top_ten[i][0] + ',' + top_ten[k][0]

            if wombo_combo == combo1 or wombo_combo == combo2:
                if pair in combo_counter:
                    combo_counter[pair] += 1
                else:
                    combo_counter[pair] = 1
           
print(top_ten)
print()
print(combo_counter)

        


