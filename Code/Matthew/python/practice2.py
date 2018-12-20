

def count_letter(letter, word):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2


# if not found ====================
# list.index raises an exception
# string.find returns -1


def count_hi(word):
    starting_search_location = 0
    counter = 0
    while True:
        found_index = word.find('hi', starting_search_location)
        if found_index == -1:
            break
        counter += 1
        starting_search_location = found_index + 2

    # print(word.find('hi', 0))
    # print(word.find('hi', 7))
    # print(word.find('hi', 18))
    # print(word.find('hi', 26))

    return counter
print(count_hi('hburyhikkskhiueivnhihihihiddjcjhi'))

def count_hi2(word):
    counter = 0
    for i in range(len(word)-1):
        if word[i] == 'h' and word[i+1] == 'i':
            counter += 1
    return counter




def count_occurrences(word, text):
    starting_search_location = 0
    counter = 0
    while True:
        found_index = text.find(word, starting_search_location)
        if found_index == -1:
            break
        counter += 1
        starting_search_location = found_index + len(word)
    return counter



def count_occurrences2(word, text):
    counter = 0
    for i in range(len(text)-len(word)+1):
        if word == text[i:i+len(word)]:
            counter += 1
        # print(f'{counter} {text[i:i+len(word)]}')
    return counter


def count_occurrences3(word, text):
    counter = 0
    for i in range(len(text)-len(word)+1):
        word_found = True
        for j in range(len(word)):
            if word[j] != text[i+j]:
                word_found = False
                break
        if word_found:
            counter += 1
    return counter



def cat_dog(text):
    # # find the number of occurrences of 'cat' in text
    # cat_count = count_occurrences('cat', text)
    #
    # # find the number of occurrences of 'dog' in text
    # dog_count = count_occurrences('dog', text)
    #
    # # if they're equal, return True, otherwise return False
    # if cat_count == dog_count:
    #     return True
    # else:
    #     return False

    return count_occurrences('cat', text) == count_occurrences('dog', text)





# print(cat_dog('catdo')) # False
# print(cat_dog('catdogcatdog')) # True

# print(count_hi2('11111hi3984u3985hi739845hi')) # 3
# print(count_occurrences2('hi', '11111hi3984u3985hi739845hi')) # 3
# print(count_occurrences2('hello', '11111hi398hello739845hhelloi')) # 3









