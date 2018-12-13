def reverse(x):
    y = []
    for char in x:
        y.append(char)
        z = y[::-1]
    return z


word = input('give me a word, lets check if it is a palindrome or not\n')
original_word = []
for char in word:
    original_word.append(char)
print('word reversed')
print(reverse(word))
if original_word[::] == (reverse(word[::])):
    print('this is a palindrome')
else:
    print('not a palindrome')



