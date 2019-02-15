#Lab_20_Credit_Card_Validation

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5

# Convert the input string into a list of ints

# credit_card_number = input('Enter the credit card number ')
credit_card_number = '4556737586899855'
credit_card_number = list(credit_card_number)
check_digit = credit_card_number.pop(-1)
credit_card_number.reverse()
for i in range(len(credit_card_number)):
    credit_card_number[i] = int(credit_card_number[i])
for i in range(0, len(credit_card_number), 2):
    credit_card_number[i] *= 2
for i in range(0, len(credit_card_number) - 1):
    if credit_card_number[i] > 9:
        credit_card_number[i] -= 9
total = sum(credit_card_number)
# print(total)
# total = str(total)
# total = list(total)
# for i in range(len(total)):
#     total[i] = int(total[i])
# print(total[1])
if total % 10 == int(check_digit): # just needs second digit of total
    print('Number is Valid')
else:
    print('Sorry. That number is not valid.')



# credit_card_number = int(credit_card_number)

#for i in range(len(Student_Grades)):
    # Student_Grades[i] = int(Student_Grades[i])

#4556737586899855

# credit_card_number.pop(-1)
print(credit_card_number)
print(check_digit)
print(total)