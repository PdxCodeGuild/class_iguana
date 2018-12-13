#Lab_13_ROT_13_Cipher

#Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character,
# add it to an output string. notice that there are 26 letters in the english language,
# so encryption is the same as decryption.
#using the index of the alphabet, at +13 for each letter in the given word.
#get the index of each letter, associated with the

import string
alpha_string = string.ascii_lowercase # acquire the alphabet as a string
alpha_string_list = list(string.ascii_lowercase) # convert the alphabet string to a list
rot_cipher_string = alpha_string[13:] + alpha_string[:13] # acquire rot13 alphabet string by concatinating 13:(the elements after index 13) with :13 (the elements up to index 13).
rot_cipher_list = list(rot_cipher_string) # convert the rot13 string to a list
# print(rot_cipher_list) # confirmed that the list prints correctly - and it is a list (for some reason i'm ending up with a list of single character element lists.

#  0123456
# 'abcdefg'
# 'nopqrst'

user_word = input('Please enter a word.')
user_word_list = list(user_word) #I'm changing the word into a list.
# print(user_word_list) # confirmed that this is in fact a list of sindular string characters
code_word = ''
for i in user_word_list: # this is to collect the indexes of the characters in the given word as they would show in the rot 13 alphabet
    char_index = alpha_string_list.index(i) # rot_cipher_list.index(element) will return the index of given element. so the idea is to loop over all the elements of the word and collect the indexes
    # print(rot_cipher_list[char_index])
    code_word += rot_cipher_list[char_index]

print(code_word)
# exit()

#Everything below was overthink

#append() appends an element to the end
# print(char_index_list) #confirmed this will print the correct list of inceses
# code_word = [] #empty list - the idea is to append to this list the letters that correspond with the indexes I collected, but from the regular aphabet list (alpha_string_list
#
# print(alpha_string_list[9:10])
#
# for num in char_index_list:
#     code_word = alpha_string_list.pop(num)
#     # code_word.append(alpha_string_list[num:num + 1])
#     # print(alpha_string_list[num:num + 1])
#
# print(code_word)

#random_element = password_list.pop(random_index) COPIED FROM PW GENERATOR LAB #this is removing whatever element was randomely seclected on line 47 via
# password = ''
# for i in range(len(password_list)):
#     random_index = random.randint(0, len(password_list)-1) # variable for a randomly selected element (by index). to establish the proper range, use -1 because indexing starts with 0
#     print(password_list) #will show the same list as the one above first time through the loop, then each time missing a randomly selected element
#     # print(random_index)
#     random_element = password_list.pop(random_index) #this is removing whatever element was randomely seclected on line 47 via
#
#     # print(random_element)
#     #print()



# code_word = str(code_word)
# ''.join(code_word)




