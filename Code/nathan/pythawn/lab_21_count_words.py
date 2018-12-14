word_list = []
word_list = open('huckleberry.txt').read().split()

for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()

repeat_words = []
for i in range(len(word_list)):
    if word_list[i] == word_list[i]:
        repeat_words.append(word_list[i])
print(repeat_words)
