"""
author: Richard Sherman
2015-12-05
lab17-palindrome-anagram.py, checks to see if a string is a palindrome and if two words are anagrams of each other
"""
print('This program checks to see if a word is a palindrome. You can type in a string, and I\'ll tell you if it\'s a palindrome.')
s = input('Please type in your string:  ')
if s == s[::-1]:
    print(f'{s} is a palindrome')
#    print(f'\t{s}\n\t{s[::-1]}') # this does not work. how do I print the reversed string?
else:
    print(f'{s} is not a palindrome')

print('\nThis program checks to see if two words are anagrams of each other.')
s1 = input('Please enter a string:  ')
s2 = input('Please enter another string:  ')
t1 = sorted(s1)
t2 = sorted(s2)
if t1 == t2:
    print(f'{s1} is an anagram of {s2}.')
else:
    print(f'{s1} is not an anagram of {s2}.')