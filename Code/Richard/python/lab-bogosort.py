"""
author: Richard Sherman
2018-12-08
lab-bogosort.py, an inefficient sorting algorithm
"""

def random_list(n):
    import random
    random_list = []
    for i in range(n):
        random_list.append(random.randint(0, 100))
    return(random_list)

def shuffle(nums):
    import random
    for i in nums:
        new_index = random.randint(0, 199)
        i = nums[i]
        j = nums[new_index]
        nums[i] = j
        nums[new_index] = i
    return(nums)

def is_sorted(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] <= nums[i+1]:
            i += 1
        else:
            return False
    print(random_list)
    return True

def bogosort(nums):
    is_sorted(nums) == False
    while is_sorted(nums) == False:
        random_list(200)
        shuffle(random_list)
        is_sorted(random_list)
