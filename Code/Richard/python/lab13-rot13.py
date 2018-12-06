"""
author: Richard Sherman
2018-12-05
lab13-rot13.py, implements a rot-13 encoding and a general rotation coding
assumes input is ascii characters, digits and punctuation are unchanged
"""

import string

def encode(s,dict):
    s_out_list = []
    for i in s:
        s_i = dict[i]
        s_out_list.append(s_i)
    s_out = ''.join(s_out_list)
    print(f'\n{s_out}')
    return s_out

ltr_lo_in = string.ascii_lowercase
ltr_lo_out = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]

ltr_up_in = string.ascii_uppercase
ltr_up_out = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]

ltr_in = ltr_lo_in + ltr_up_in + string.digits + string.punctuation
ltr_out = ltr_lo_out + ltr_up_out + string.digits + string.punctuation

rot13_dict = dict(zip(ltr_in, ltr_out))
print(rot13_dict)


print('I\'ve learned a new trick. I can translate a message into a code so secret that only Caesar will be able to crack it. Are you ready to try it out?')
s = input('Type something in, and I\'ll show you the secret code:  ')

encode(s, rot13_dict)

print('\nNow, perhaps you want a code so secret that not even Caesar can crack it.')
print('For that, you\'ll have to enter a number between 1 and 26 (inclusive): that\'s the key to the secret code.')
key = int(input('Please enter your key:  '))
s = input('Okay, now type in the message you want encoded:  ')


ltr_lo_in = string.ascii_lowercase
ltr_lo_out = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]

ltr_up_in = string.ascii_uppercase
ltr_up_out = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]

ltr_in = ltr_lo_in + ltr_up_in + string.digits + string.punctuation
ltr_out = ltr_lo_out + ltr_up_out + string.digits + string.punctuation

encode_dict = dict(zip(ltr_in, ltr_out))
decode_dict = dict(zip(ltr_out, ltr_in))

encode(s, encode_dict)

print('\nIf you type "decode" and then the encoded message, you\'ll get the original message back.')
print('\nBut I\'ll save you the trouble. Let me decode the message for you.')
print('I\'ll show you the coded message, then the decoded original.')

encode(encode(s, encode_dict), decode_dict)


