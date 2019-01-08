
with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

#list of dictionaries
#Name : Gordon Jefferson, Favorite Fruit : Pineapple ...each person their own dictionary
data_list = []
for line in lines:
    line = line.split(',')
    data_list.append(line)


indexes = data_list.pop(0)
# print(indexes)
# print(data_list)
data_dict = {}
data_dict_list = []
for i in range(len(indexes)-1):
    data_dict[indexes[i]] = data_list[i][i]
    data_dict_list.append(data_dict)

print(data_dict_list)
# print(data_lines)

