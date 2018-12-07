





# how to validate user input

# direction = input('what direction do you want to move in? ').lower()
# if direction in ['left', 'l', 'west', 'w']:
#     # move left
# elif direction in ['right', 'r', 'east', 'e']:
#     # move right
# else:
#     print('command not recognized')



# def get_number(message):
#     while True:
#         num = input(message)
#         try:
#             num = int(num)
#             break
#         except TypeError:
#             print('please enter a number')
#     return num


# age = get_number('enter your age: ')
# print(age)






import random

def is_even(a):
    return a % 2 == 0

# nums = []
# for i in range(100):
#     nums.append(random.randint(0,99))
# print(nums)


# nums = [i for i in range(100)]
# nums = [random.randint(0,99) for i in range(100)]
# print(nums)
# nums = [num for num in nums if is_even(num)]
# print(nums)


# names = ['joe', 'marcy', 'julianna', 'ted']
# names_to_ages = {random.choice(names):random.randint(5,80) for i in range(10)}
# print(names_to_ages)

# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# nums = [2**i for i in range(10)]
# print(nums)

# nums = []
# for i in range(10):
#     nums.append(2**i)
# print(nums)


def get_even_numbers(nums):
    evens = []

    for num in nums:
        if is_even(num):
            evens.append(num) 

    return evens





print(get_even_numbers([1,2,3,4]))
# List containing 2 and 4


def opposite(a, b):
    # if a < 0:
    #     if b < 0:
    #         return False
    #     return True
    # else:
    #     if b < 0:
    #         return True
    #     return False
    # return (a > 0 and b < 0) or (a < 0 and b > 0)
    return a * b < 0

print(opposite(-1, -1))

# print(is_even(4))




def near_100(num):
    return num >= 90 and num <= 110
    # return num in range(90, 111)
    # return abs(100-num) <= 10


print(near_100(95)) # true
print(near_100(5)) # false




def maximum_of_three(a, b, c):
    # nums = [a, b, c]
    # nums.sort()
    # return nums[-1]
    
    # return max(a, b, c)


    # if a > b:
    #     if a > c:
    #         return a
    #     else:
    #         return c
    # else:
    #     if b > c:
    #         return b
    #     else:
    #         return c
    


    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c



# print(maximum_of_three(5, 6, 7)) # 7
# print(maximum_of_three(-5, 110, 0)) # 110



def double_letters(s):
    output = ''
    for letter in s:
        output += letter*2
    return output

    # output = []
    # for letter in s:
    #     output.append(letter + letter)
    # return ''.join(output)

    # return ''.join([letter + letter for letter in s])



print(double_letters('hello')) # 'hheelllloo'



def missing_char(word):
    output = []
    for i in range(len(word)):
        output.append(word[:i] + word[i+1:])
    return output


print(missing_char('kitten')) # ['#itten', 'k#tten', 'ki#ten', 'kit#en', 'kitt#n', 'kitte#']


def latest_letter(word):
    return max(word)

    # letter_list = list(word)
    # letter_list.sort()
    # return letter_list[-1]

    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # highest_index = -1
    # for char in word:
    #     index = alphabet.find(char)
    #     if index > highest_index:
    #         highest_index = index
    # return alphabet[highest_index]

    # furthest_letter = word[0]
    # for char in word:
    #     if char > furthest_letter:
    #         furthest_letter = char
    # return furthest_letter


# import string
# print(list(sorted(string.printable)))

print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v