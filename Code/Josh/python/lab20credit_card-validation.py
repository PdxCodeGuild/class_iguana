data_list = []
data = '4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5'
data = data.split(',')
print(data)
for i in data:
    data_list.append(int(i))
print(data_list)
check_digit = data_list.pop()
print(check_digit)
data_list.reverse()
print(data_list)
for i in range(0, len(data_list), 2):
    data_list[i] *= 2
for i in range(0, len(data_list), 2):
    if data_list[i] > 9:
        data_list[i] -= 9
total = sum(data_list)
print(total)
total = (sum(data_list))%10

print(total)
print(data_list)
if total == check_digit:
    print('valid card')
else:
    print('invalid card')