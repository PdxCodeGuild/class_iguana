#median

# def find_median(numbers):
#     numbers.sort()
#     for i in numbers:

nums = []
new_num = ''
while new_num != 'done':
    new_num = input('Please enter a number, or type \'done\': ')
    # new_num = int(new_num)
    nums.append(new_num)
nums.pop(-1) #I don't know how else to avoid 'done' getting included in the list. so I'm just removing it via pop
nums = [int(i) for i in nums]
nums.sort()
# print(nums[2:3])
if len(nums) % 2 == 0: #test for whether thsi is an even set of numbers.
    median_index = len(nums)//2 - 1 #if its an even set of numbers this will result in the first medien index (ie, 6//2 = 3. But need to account for index 0, so 'go back' by 1 (-1)
    median_index2 = median_index + 1 #with the first median index identified, just add 1 to get the second.
    # print(median_index, median_index2) #added this to verify I was printing the write index
    print(nums[median_index:median_index2 + 1])
else: #anything else will be an odd set of numbers
    median_index = len(nums) // 2 + 1 # need plus one because index starts at 0
    print(median_index) # verifying that I am getting the right index
    print(nums[median_index - 1:median_index])


