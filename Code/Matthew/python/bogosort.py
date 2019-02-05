
# import random

# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-1):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#
# nums = [random.randint(0,99) for i in range(100)]

# print(nums)
# bubble_sort(nums)
# print(nums)

import random
import time



def random_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(0, 99))
    return nums

def shuffle_nums(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)
        nums[i], nums[j] = nums[j], nums[i]

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False

    return True


def percent_sorted(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            count += 1
    return count/(len(nums)-1)

def get_time():
    return int(round(time.time() * 1000))



def bogosort(nums):
    counter = 0
    start_time = get_time()


    while not is_sorted(nums):
        shuffle_nums(nums)
        counter += 1

    end_time = get_time()
    time_taken = end_time - start_time
    # print(f'total time taken: {time_taken/1000} seconds')
    # print(f'time per step:    {time_taken/1000/counter} second')
    print(f'bogosort: {counter}')



def bogosort_optimized(nums):
    ps = percent_sorted(nums)
    counter = 0

    # while abs(ps-1.0) > 0.00001:
    while ps != 1.0:
        counter += 1
        nums_temp = nums.copy()
        shuffle_nums(nums_temp)
        pst = percent_sorted(nums_temp)
        if pst > ps:
            nums = nums_temp
            ps = pst
    print(f'bogosort_optimized: {counter}')
    return nums


def sqrt_optimized(x):
    z = 0
    counter = 0
    while z*z != x:
        z = int(random.random()*x)
        counter += 1
    print(f'sqrt_optimized: {counter}')
    return z

print(sqrt_optimized(64))



seed = get_time()
n_values = 8

print(f'seed: {seed}')
print()

random.seed(seed)
nums = random_list(n_values)
print(nums)
bogosort(nums)
print(nums)

random.seed(seed)
nums = random_list(n_values)
print(nums)
nums = bogosort_optimized(nums)
print(nums)














# nums = random_list(5)
# print(nums)
# input('...')
# bogosort(nums)
# print(nums)









# def get_time():
#     return int(round(time.time() * 1000))

# nums = random_list(12)
# print(nums)
# input('>')
# bogosort(nums)
# print(nums)
# nums = [1, 2, 3, 4]
# print(nums)
# print(is_sorted(nums))
# shuffle_nums(nums)
# print(nums)
# print(is_sorted(nums))












