"""
Program gets two inputs from the user. First input is checked to see if it is a palindrome. 
Second input is compared to the first to see if they are anagrams of each other.
Inputs accept special characters so that phrases may be used. 
Ex: A man, a plan, a canal, Panama!  >> is a palindrome   source: https://en.wikipedia.org/wiki/Palindrome
"""

import re


# Strips a string of special characters and white space and converts to lower case
def get_stripped(string):
    string = re.sub('[^a-zA-Z0-9]', '', string).lower()
    return string

# Reverses input and calls get_stripped() for original input and reversed copy. 
# Compares strings and prints results. Returns stripped original input for use in check_anagram()
def check_palindrome(string):
    reverse_str = string[::-1]
    reverse_str = get_stripped(reverse_str)
    string = get_stripped(string)

    if reverse_str == string:
        print('String is a palindrome')
    else:
        print('String is not a palindrome')
    
    return string

    

# Calls get_stripped() on second input and sorts it. Compares that to the sorted/stripped original input. Prints results
def check_anagram(string2, stripped):
    string2 = sorted(get_stripped(string2))

    if sorted(stripped) == string2:
        print('It\'s an anagram!\n')
    else:
        print('It\'s not an anagram.\n')
    


string = input('\nEnter a word/phrase: ')
stripped = check_palindrome(string)
string2 = input(f'\nEnter another word or phrase to see if it is an anagram of "' + string + '": ')
check_anagram(string2, stripped)

 
