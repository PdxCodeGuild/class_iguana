"""
author: Richard Sherman
2018-12-05
lab13-rot13.py, implements a rot-13 encoding
"""

import string

def rot13(s,tab):
    x = s.translate(tab)
    print(x)
    return x

def encode(s, tab):
    x = s.translate(e_tab)
    print(x)
    return x

def decode(s, tab):
    x = s.translate(d_tab)
    print(x)
    return x


low_1 = string.ascii_lowercase[:13]
low_2 = string.ascii_lowercase[13:]
up_1 = string.ascii_uppercase[:13]
up_2= string.ascii_uppercase[13:]
in_table = low_1 + up_1
out_table = low_2 + up_2
tab = str.maketrans(in_table, out_table)

print('I\'ve learned a new trick. I can translate a message into a code so secret that only Caesar will be able to crack it. Are you ready to try it out?')
s = input('Type something in, and I\'ll show you the secret code:  ')

rot13(s, tab)

print('=\nNow, perhaps you want a code so secret that not even Caesar can crack it.')
print('For that, you\'ll have to enter a number: that\'s the key to the secret code.')
key = input('Please enter your key:  ')

e_low_1 = string.ascii_lowercase[:key]
e_low_2 = string.ascii_lowercase[key:]
e_up_1 = string.ascii_uppercase[:key]
e_up_2 = string.ascii_uppercase[key:]

d_low_1 = string.ascii_lowercase[key:]
d_low_2 = string.ascii_lowercase[:key]
d_up_1 = string.ascii_uppercase[key:]
d_up_2 = string.ascii_uppercase[:key]
in_e_table = e_low_1 + e_up_1
out_e_table = e_low_2 + e_up_2
in_d_table = d_low_1 + d_up_1
out_d_table = d_low_2 + d_up_2
e_tab = str.maketrans(in_e_table, out_e_table)
d_tab = str.maketrans(in_d_table, out_d_table)
