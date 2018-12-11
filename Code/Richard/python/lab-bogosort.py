"""
author: Richard Sherman
2018-12-08
lab-bogosort.py, an inefficient sorting algorithm
"""

import random

def random_list(n):

    random_list = []
    for i in range(n):
        random_list.append(random.randint(0, 100))
    return random_list

def shuffle(nums):

    for i in range(len(nums)):
        new_index = random.randint(0, len(nums) - 1)
        orig = nums[i]
        replace = nums[new_index]
        nums[i] = replace
        nums[new_index] = orig

def is_sorted(nums):

    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i+1]:
            return False
        i += 1
    print(random_list)
    return True

def bogosort(nums):

    while is_sorted(nums) == False:
        shuffle(nums)
    return nums


nums = random_list(10)
print(nums)
bogosort(nums)
print(nums)
