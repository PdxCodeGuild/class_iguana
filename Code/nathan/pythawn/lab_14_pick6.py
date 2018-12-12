import random

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
          57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
          84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

winning_numbers = []

num = random.choice(digits)
winning_numbers.append(num)
num2 = random.choice(digits)
winning_numbers.append(num2)
num3 = random.choice(digits)
winning_numbers.append(num3)
num4 = random.choice(digits)
winning_numbers.append(num4)
num5 = random.choice(digits)
winning_numbers.append(num5)
num6 = random.choice(digits)
winning_numbers.append(num6)

winning_numbers[0:6] = sorted(winning_numbers[0:6])
print(winning_numbers)

ticket_number = []

number = random.choice(digits)
ticket_number.append(number)
number2 = random.choice(digits)
ticket_number.append(number2)
number3 = random.choice(digits)
ticket_number.append(number3)
number4 = random.choice(digits)
ticket_number.append(number4)
number5 = random.choice(digits)
ticket_number.append(number5)
number6 = random.choice(digits)
ticket_number.append(number6)

ticket_number[0:6] = sorted(ticket_number[0:6])
print(ticket_number)

prize_money = 0
prize_money2 = 0
prize_money3 = 0
prize_money4 = 0
prize_money5 = 0
prize_money6 = 0
if ticket_number[0] != winning_numbers[0]:
    prize_money += 0
    print(prize_money)
elif ticket_number[0] == winning_numbers[0:5]:
    prize_money += 4
    print(prize_money)
if ticket_number[1] != winning_numbers[1]:
    prize_money2 += 0
    print(prize_money2)
elif ticket_number[1] == winning_numbers[1]:
    prize_money2 += 4
    print(prize_money2)
if ticket_number[2] != winning_numbers[2]:
    prize_money3 += 0
    print(prize_money3)
elif ticket_number[2] == winning_numbers[2]:
    prize_money3 += 4
    print(prize_money3)
if ticket_number[3] != winning_numbers[3]:
    prize_money4 += 0
    print(prize_money4)
elif ticket_number[3] == winning_numbers[3]:
    prize_money4 += 4
    print(prize_money4)
if ticket_number[4] != winning_numbers[4]:
    prize_money5 += 0
    print(prize_money5)
elif ticket_number[4] == winning_numbers[4]:
    prize_money5 += 4
    print(prize_money5)
if ticket_number[5] != winning_numbers[5]:
    prize_money6 += 0
    print(prize_money6)
elif ticket_number[5] == winning_numbers[5]:
    prize_money6 += 4
    print(prize_money6)

over_all_prize = 0
if int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 0:
    over_all_prize += 0
    print(over_all_prize)
elif int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 4:
    over_all_prize += 4
    print(over_all_prize)
elif int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 8:
    over_all_prize += 7
    print(over_all_prize)
elif int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 12:
    over_all_prize += 100
    print(over_all_prize)
elif int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 16:
    over_all_prize += 50000
    print(over_all_prize)
elif int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 20:
    over_all_prize = 1000000
    print(over_all_prize)
elif int(prize_money) + int(prize_money2) + int(prize_money3) + int(prize_money4) + int(prize_money5) + int(prize_money6) == 0:
    over_all_prize = 25000000
    print(over_all_prize)






