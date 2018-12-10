#number list
numb = [1, 2, 3, 4, 5, 6]
#variable##sum of list##divided by length of list
average = (sum(numb)) / len(numb)
print(average) #printing average of number list

#nextversion

numb2 = []
while True: #continuous loop building list until string done is typed
    num = (input('give me a number or type done'))
    if num != 'done':
        numb2.append(int(num))  #adding each number input to string with .append
        average2 = (sum(numb2)) / len(numb2)  #sum of built list divided by length of list
    elif num == 'done':
        print(average2)#printing average
        break
















