



# len is 4
#  0  1  2  3
# [a, b, c, d]

# len is 5
#  0  1  2  3  4
# [a, b, c, d, e]



def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if lstLen % 2 == 1:
        return [sortedLst[index]]
    return [sortedLst[index], sortedLst[index + 1]]

num_list = []
num = ''
while True:
    num = input('Give me a number or type \'done\'\n>')
    if num == 'done':
        break
    num_list.append(int(num))
print(f'your numbers are {num_list}')
average = sum(num_list) / len(num_list)
print(f'the average of those is {average}')
print(sorted(num_list))
num_list = sorted(num_list)
print(len(num_list))
print(len(num_list) % 2)

print(len(num_list) / 2)
# if len(num_list) % 2 == 1:
#     print(len(num_list)// 2)
n = len(num_list)
# if n < 1:
#     return None
# if len(num_list) % 2 == 1:
#     print(sorted(num_list) / 2)
print(median(num_list))

# median = list[len(num_list)] // 2
# print(median)



