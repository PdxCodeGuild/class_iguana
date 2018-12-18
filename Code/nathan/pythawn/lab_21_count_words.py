import string


def index(tuple_1):
    return tuple_1[1]

#empty list and empty dictionary
word_list = []
word_count = {}
#open book file and fill empty list with books words
word_list = open('huckleberry.txt').read().split()
#take punctuation out of book
for i in range(len(word_list)):
    word_list[i] = word_list[i].strip(string.punctuation)
#lowercase every word in book
for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()
#fill dictionary with words as keys and keep count of how many times words appear
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_list = list(word_count.items())
word_list2 = sorted(word_list, key=index, reverse=True) #reverse and sort list so most common words appear first
print(word_list2[0:10]) #print word dictionary with range of first ten words
