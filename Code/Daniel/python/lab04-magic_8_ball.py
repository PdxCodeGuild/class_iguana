import random

predictions = []
cont = True

f = open('predictions.txt', 'r')
for i in f:
    fixed_pred = i.replace("\n", "")
    predictions.append(fixed_pred)
f.close()

print('Welcome to the Magic 8 Ball Sim. Enter "done" to quit.')

while cont == True:
    question = input('Please ask a question: ')

    if question == "done":
       cont = False 
    else:
        print(random.choice(predictions))