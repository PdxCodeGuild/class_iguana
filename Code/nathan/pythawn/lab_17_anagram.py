def anagram(a):
    b = []
    b = list(a)
    b = (sorted(b))
    return b

word = input('give me a word')
word1 = input('give me another word')

if (anagram(word)) == (anagram(word1)):
    print('yup, that is an anagram')
else:
    print('no, they have different letters man')
