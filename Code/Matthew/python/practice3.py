
import random


def reverse1(nums):
    nums = nums[::-1]
    return nums

def reverse2(nums):
    nums.reverse()
    return nums

def reverse3(nums):
    return reversed(nums)

def reverse4(nums):
    output = []
    for num in nums:
        output.insert(0, num)
        print(f'{num} {nums}')
        print(f'{output}')
        print()
    return output


# len is 6
#     0         1          2         3            4            5
# ['apples', 'bananas', 'pears', 'oranges', 'pomegranate', 'grapes']
#              i     j
# first swap:  0 and 5 (6-1-0) len(fruits) - i - 1
# second swap: 1 and 4 (6-1-1)
# third swap:  2 and 3 (6-1-2)


def reverse5(nums):
    for i in range(len(nums)//2):
        j = len(nums) - i - 1 # figure out the other index to swap with
        nums[i], nums[j] = nums[j], nums[i] # swap
    return nums





# for num in reversed(nums)
# for num in sorted(nums)


# nums = [random.randint(0,99) for i in range(10)]
# nums.sort()
# print(nums)
#
# nums = reverse5(nums)
# print(nums)




# [6, 7, 9, 10, 15, 16]
# [6, 7, 9]

def extract_less_than_ten(nums):
    output = []
    for num in nums:
        if num < 10:
            output.append(num)
    return output
    # return [num for num in nums if num < 10]




# nums = [random.randint(0,20) for i in range(10)]
# print(nums)
# print(extract_less_than_ten(nums))



def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):  # i+1 to prevent backtracking
            # print(f'looking at {i} and {j}')
            # if i == j:
            #     continue
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return None



print(find_pair([5, 6, 2, 3], 7)) # [5, 2] or [2, 5]


