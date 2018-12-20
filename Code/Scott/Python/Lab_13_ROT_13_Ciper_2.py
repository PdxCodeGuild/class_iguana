#Lab_13_ROT_13_Cipher

#This time, prompt the user for how much they want the rotation to be.

import string
# alpha_string = string.printable # acquire the larger alphabet as a string
alpha_string = string.ascii_letters # acquire the larger alphabet as a string

user_word = input('Please enter a word.')
                                          # user_word_list = list(user_word) #Not necessary. I'm changing the word into a list.
rot_count = int(input('How many characters would you like the encryption/rotation to be?'))
rot_cipher_string = alpha_string[rot_count:] + alpha_string[:rot_count]
# rot_cipher_string = alpha_string[13:] + alpha_string[:13]

print(alpha_string)
print(rot_cipher_string)

code_word = ''
for char in user_word: # this is to collect the indexes of the characters in the given word as they would show in the rot 13 alphabet
    char_index = alpha_string.find(char) # rot_cipher_list.index(element) will return the index of given element. so the idea is to loop over all the elements of the word and collect the indexes
    # print(rot_cipher_list[char_index])
    if char_index == -1:
        code_word += char
    else:
        code_word += rot_cipher_string[char_index]

print(code_word)
# exit()




