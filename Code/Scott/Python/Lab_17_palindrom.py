#Lab_17 palindrome



def check_palindrome(string):
    if string == string[::-1]:
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is not a palindrome')



string = input('Enter a word please... ')
check_palindrome(string)










# # user_word = word
# def check_palindrome(user_word):
#     for i in range(len(user_word)//2):
#         if user_word[0] != user_word[-1]:
#             continue
#             print(f'{user_word} is not a palindrome')
#         else:
#             print(f'{user_word} is a palindrome')
#
# user_word = input('Enter a word          please          ')
# print(check_palindrome(user_word))


