"""
author: Richard Sherman
2018-12-05
lab20-credit-card-validation.py, checks to see if a credit card number is valid.
"""

import random
import string

def check_cc_num(cc_num):

    check_num = cc_num[-1]
    cc_num_2 = cc_num[:-1]
    cc_num_3 = cc_num_2[::-1]
    i = 1
    while i < len(cc_num_3) - 1:
        cc_num_3[i] *= 2
        i += 2
    for i in range(len(cc_num_3)):
        if cc_num_3[i] > 9:
            cc_num_3[i] -= 9
    cc_num_3_sum = sum(cc_num_3)
    final_num = str(cc_num_3_sum)[1]

    return final_num == check_num



card_num = []
for i in range(16):
    card_num.append(random.randint(0,9))
print(card_num)
print(check_cc_num(card_num))

