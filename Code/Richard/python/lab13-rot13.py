"""
author: Richard Sherman
2018-12-05
lab13-rot13.py, implements a rot-13 encoding
"""

import string

def rot13(s,tab):
    x = s.translate(tab)
    print(x)


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
