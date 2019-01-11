import string
with open('tale_of_two_cities.txt', 'r', encoding='utf-8') as f:
    lines = f.read().lower().split()
    for i in range(len(lines)):
        for char in string.punctuation:
            lines[i] = lines[i].replace(char, '')

    for i in range(len(lines)):
        for char in string.digits:
            lines[i] = lines[i].replace(char, '')
    word_dict = {}
    # lines = ['apple', 'apple', 'banana']
    # word_dict = {}
    # word_dict = {'apple': 1}
    # word_dict = {'apple': 2}
    # word_dict = {'apple': 2, 'banana': 1}
    for word in lines:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items())  # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
# print(word_dict)
