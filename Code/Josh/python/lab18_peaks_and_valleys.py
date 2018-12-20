# number_list = (input('what\'s your number data? separate each number with a comma\n>>'))

# number_list = number_list.split(',')
number_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# print(number_list)
number_list = [int(i) for i in number_list]
# print(number_list)
combined_list = []
peak =[]
valley =[]
#checking for peaks
for i in range(len(number_list)):
    if i == 0 or i == len(number_list)-1:
        continue
    if number_list[i + 1] < number_list[i] and number_list[i - 1] < number_list[i]:
        peak.append(number_list[i])
        combined_list.append(int(i))
for i in range(len(number_list[1:])):
    if number_list[i +1] > number_list[i] and number_list[i -1] > number_list[i]:
        valley.append(number_list[i])
        combined_list.append(int(i))
for height in range(10, -1, -1):
    for j in range(len(number_list)):
        if j == 0 or j == len(number_list)-1:
            continue
       # if int(number_list[j +1]) > int(number_list[j]) and int(number_list[j -1]) > int(number_list[j]) and int(number_list[j]) < height:
       #     print('0', end='')
        if int(number_list[j]) >= height:
           print('x', end='')
       # elif: int(number_list[j]) <
        else:
           print(' ', end='')
    print()

combined_list.sort()
print(peak)
print(valley)
print(combined_list)
for i in (combined_list):
    print(number_list[i])








