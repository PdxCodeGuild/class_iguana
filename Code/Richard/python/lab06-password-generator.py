"""Author: Richard Sherman
2018-12-03
lab06-password-generator.py, generates random passwords with some conditions"""

import random
import string

print('This program generates passwords for you. Let me ask you a couple of questions.')
n = int(input('First, how long (how many characters) do you want your password to be? '))
print('OK, great. I can do that.')
print('A good password usually includes some uppercase letters and some lowercase letters. It\'s also good to have some numbers.')
ups = int(input('How many uppercase letters would you like to have? '))
nums = int(input('How many numbers would you like to have? '))

lowers = []
i = 1
while i <= (n - ups - nums):
    lowers.append(random.choice(string.ascii_lowercase))
    i += 1

uppers = []
i = 1
while i <= ups:
    uppers.append(random.choice(string.ascii_uppercase))
    i += 1

numbers = []
i = 1
while i <= nums:
    numbers.append(random.choice(string.digits))
    i += 1
l = lowers + uppers + numbers
# print(lowers, uppers, numbers)
# print(l)
random.shuffle(l)
password = ''.join(l)

print(f'Your password is {password}. Keep it in a safe place!')
