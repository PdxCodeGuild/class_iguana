#lab_10_average_numbers_v2.py

#create list and append with integers from input calls
#input returns strings, need to convert to int

nums = []
new_num = ''
while new_num != 'done':
    new_num = input('Please enter a number, or type \'done\': ')
    # new_num = int(new_num)
    nums.append(new_num)
nums.pop(-1) #I don't know how else to avoid 'done' getting included in the list. so I'm just removing it via pop
nums = [int(i) for i in nums]# I looked this one up
ave = sum(nums)//len(nums)

# print(nums)
print(f'The average of your numbers is {ave}')




# dog_string = 5
# while dog_string != 'dog': #If the answer isn't correct, repeat with "True"
#     dog_string = input("Please type dog >")

# while True:
#     cat_string = input("Please type cat >")
#     if cat_string == 'cat':
#         break
#
# dog_string = 5
# while dog_string != 'dog': #If the answer isn't correct, repeat with "True"
#     dog_string = input("Please type dog >")






    # a = sum(nums)
    # print(a)
    # # nums = []
    # # nums.append(7)
    # # print(nums)
    #
    # average = a / len(nums)
    # print(average)



