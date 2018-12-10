"""
author: Richard Sherman
2018-12-09
lab-sock-sorter.py, use dictionaries to inquire about sock pairing
"""

import random

sock_types = ('ankle', 'calf', 'crew', 'thigh')
sock_types_100 = sock_types * 100
sock_list = random.sample(sock_types_100, 100)
print(sock_list)

sock_dict = {}
for i in sock_list:
    sock_dict[i] = sock_dict.get(i, 0) + 1
print(sock_dict)

# from collections import Counter
# socks_count = Counter(sock_list)
# print(socks_count)

for k in sock_dict:
    print(f'Sock type "{k}" has {sock_dict[k] // 2} pairs and {sock_dict[k] % 2} loners.')

sock_colors = ['black', 'white', 'blue']
sock_types_colors = [(t, c) for t in sock_types for c in sock_colors]
# print(sock_types_colors)

sock_list_colors = []
for i in range(1000):
    sock_list_colors.append(random.choice(sock_types_colors))
sock_type_color_dict = {}
for i in sock_list_colors:
    sock_type_color_dict[i] = sock_type_color_dict.get(i, 0) + 1
print(sock_type_color_dict)

for k in sock_type_color_dict:
    print(f'Sock type "{k}" has {sock_type_color_dict[k] // 2} pairs and {sock_type_color_dict[k] % 2} loners.')
