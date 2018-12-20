def check_palindrome():
    word = input('Check and see if your word is a palindrome, give me a word\n>>').lower()
    word_list = []
    for i in word:
        word_list.append(i)
    reversed_word_list = word_list[::-1]
    if reversed_word_list == word_list:
        return True
    else:
        return False

# print(f'{check_palindrome()} this word is a palindrome')

def check_anagram():
    word = input('What\'s your word?\n>>').lower()
    anagram_word = input('give another word and I\'ll check if they are anagrams\n>>').lower()
    word_list = []
    anagram_list = []
    for i in word:
        word_list.append(i)
    for i in anagram_word:
        anagram_list.append(i)
    if sorted(word_list) == sorted(anagram_list):
        return True
    else:
        return False

print(check_anagram())

