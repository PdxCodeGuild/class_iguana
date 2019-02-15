#Lab_17 anagram


# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.
#
# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:
#
# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
# >>> enter the first word: anagram
# >>> enter the second word: nag a ram
# >>> 'anagram' and 'nag a ram' are anagrams

def check_anagram(word1, word2):
    word1.lower()
    word2.lower()
    word1.strip()
    word2.strip()
    word1 = sorted(word1)
    word2 = sorted(word2)
    word1 = list(word1)
    word2 = list(word2)
    # print(word1, word2)
    return word1 == word2
    # if word1!= word2:
    #     return False
    # else:
    #     return True


user_input_1 = input('What is the first word?  ')
user_input_2 = input('What is the second word?  ')

print(check_anagram(user_input_1, user_input_2))
