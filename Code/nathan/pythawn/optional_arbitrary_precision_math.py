def long_divide(number_list, divided_by):
    new_list = []
    for i in range(len(number_list)):
        i /= divided_by
        new_list.append(i)
    return new_list


number = '656565'
number_list = []
for i in number:
    number_list.append(i)
    number_list = int(number_list)

print(number_list)

divided_by = int(input('what would you like to divide by'))

test = long_divide(number_list, divided_by)
print(test)






