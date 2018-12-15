import string

word_list = []
repeat_words = []
word_list = open('huckleberry.txt').read().split()

for i in range(len(word_list)):
    word_list[i] = word_list[i].strip(string.punctuation)

for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()

for i in range(len(word_list)):
    if word_list[i] == word_list[i]:
        repeat_words.append(word_list[i])
print(repeat_words)
