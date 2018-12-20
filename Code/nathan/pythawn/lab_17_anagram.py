def anagram(a):
    a = list(a)  #putting input into list
    a = (sorted(a))  #sorting list into alphabetical order
    return a

#asking for two words
word = input('give me a word')
word1 = input('give me another word')

if (anagram(word)) == (anagram(word1)):  #checking if both inputs contain the same characters
    print('yup, that is an anagram')
else:
    print('no, they have different letters man')

#my favorite anagram so far bupid stitch