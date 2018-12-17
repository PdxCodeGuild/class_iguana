import string


def index(tuple_1):
    return tuple_1[1]


word_list = []
word_count = {}

word_list = open('huckleberry.txt').read().split()

for i in range(len(word_list)):
    word_list[i] = word_list[i].strip(string.punctuation)

for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_list = list(word_count.items())
word_list2 = sorted(word_list, key=index, reverse=True)
print(word_list2[0:10])
