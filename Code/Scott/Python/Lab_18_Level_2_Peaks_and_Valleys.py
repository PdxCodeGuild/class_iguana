# Lab 18 level 2 - peaks and valleys
#with the printed Xs



#the tallest is 9 (10 - number?)

# key_number = 9
# x_string = ''
# for number in data:
#     x_value = number - key_number
#     if x_value <= 0:
#         spot = 'X'
#     else:
#         spot = ' '
#     x_string += spot
# print(x_string)
#
# #find a value equation that results in print X
# print(max(data))

def draw(data):
    largest = max(data)
    for i in range(largest, 0, -1):
        row = ''
        for j in range(len(data)):
            if i <= data[j]:
                row += 'X'
            else:
                row += ' '
        print(row)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


draw(data)
