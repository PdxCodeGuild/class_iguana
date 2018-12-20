#median

# def find_median(numbers):
#     numbers.sort()
#     for i in numbers:

nums = []
while True:
    new_num = input('Please enter a number, or type \'done\': ')
    if new_num == 'done':
        break
    nums.append(int(new_num))
nums.sort()
# print(nums[2:3])


# len is 4
#  0  1  2  3
# [a, b, c, d]

if len(nums) % 2 == 0: #test for whether thsi is an even set of numbers.
    median_index = len(nums)//2 - 1 #if its an even set of numbers this will result in the first medien index (ie, 6//2 = 3. But need to account for index 0, so 'go back' by 1 (-1)
    median_index2 = median_index + 1 #with the first median index identified, just add 1 to get the second.
    # print(median_index, median_index2) #added this to verify I was printing the write index
    print(f'The medians of this set are {nums[median_index]} and {nums[median_index2 ]}')
else: #anything else will be an odd set of numbers
    median_index = len(nums) // 2 # this works because index starts at 0
    # median_index = median_index -1
    # print(median_index) # verifying that I am getting the right index
    print(f'The median is {nums[median_index]}')


