
# try:
#     def thing
#     x = 10
# except SyntaxError:
#     print('syntax error')



import string

def get_number():
    # n = int(input('enter a number: '))
    # return n

    # n = input('enter a number: ').lower()
    # for char in string.ascii_lowercase:
    #     if char in n:
    #         print('that\'s not a number!')
    #         break

    while True:
        try:
            n = int(input('enter a number: '))
            return n
        except ValueError:
            print('that\'s not a number!')


# print(get_number())


# fruits = ['apples', 'bananas', 'pears']
# if 'kiwi' in fruits:
#     fruits.index('kiwi')




# fruits = ['apples', 'bananas', 'pears']
# for i in range(4):
#     try:
#         print(fruits[i])
#     except:
#         pass



# try:
#     1/0
# except ZeroDivisionError:
#     print('error tried to divide by 0')
# print('some other code')




# text = open('file.txt').read()


# with open('../../1 Python/data/apothecary.txt', 'r', encoding='utf-8') as f:
#     lines = f.read().split('\n')
# print(lines)




import requests


books = [{'title': 'The Apothecary by ??',
         'url': 'https://www.gutenberg.org/files/58490/58490-0.txt'},
        {'title': 'The Journal of the American-Irish Historical Society (Vol. II) by Various',
         'url': 'https://www.gutenberg.org/files/58485/58485-0.txt'}]

print('Which book would you like to see?')
for i in range(len(books)):
    print(f'{i+1}. ' + books[i]['title'])
book_id = int(input('> ')) - 1

response = requests.get(books[book_id]['url'])
text = response.text
lines = text.split('\n')
lines = [line.strip('\r') for line in lines]
print(lines)

