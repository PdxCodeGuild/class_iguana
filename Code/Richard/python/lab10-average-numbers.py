"""Author: Richard Sherman
2018-12-04
lab10-average-numbers.py, takes averages, medians, modes"""

#note: version 4 (modes) is incomplete

#version 1
print("Calculating a running sum and average of a randomly generated list:\n")
import random
l = []
length = 10
i = 1
while i <= length:
    l.append(random.randint(0,100))
    i += 1

total = l[0]
i = 1
while i < len(l) - 1:
    sum_i = total + l[i]
    total = sum_i
    avg_i = sum_i / len(l[0:i+1])
    print(f"sum is {sum_i}")
    print(f"avg is {avg_i}")
    i += 1

#version 2 (user input)
print('\n')
list_of_nums = []
num = ''
while True:
    num = input('enter a number or done: ')
    if num == 'done':
        break
    list_of_nums.append(int(num))
    i += 1
print(f'\nThe average is {sum(list_of_nums) / len(list_of_nums)}')

#version 3 (median)
print('\nFirst, an example of finding the median with a randomly generated list of even-numbered length:')
l = []
length = 20
i = 1
while i <= length:
    l.append(random.randint(0, 100))
    i += 1
l.sort()

if len(l) % 2 == 0:
    l_median = [l[len(l)//2-1], l[len(l)//2]]
else:
    l_median = l[len(l)//2]
print(f'\nThe median of the list l is {l_median}')

print('\nSecond, an example of finding the median with a randomly generated list of odd-numbered length:')
l = []
length = 21
i = 1
while i <= length:
    l.append(random.randint(0,100))
    i += 1
l.sort()

if len(l) % 2 == 0:
    l_median = [l[len(l)//2-1], l[len(l)//2]]
else:
    l_median = l[len(l)//2]
print(f'\nThe median of the list l is {l_median}')

#version 4, modes : I don't understand dictionaries well enough
l = []
length = 1000
i = 1
while i <= length:
    l.append(random.randint(0,100))
    i += 1

word_dict = {}
for i in l:
    word_dict.get(i, 0) + 1
print(word_dict)