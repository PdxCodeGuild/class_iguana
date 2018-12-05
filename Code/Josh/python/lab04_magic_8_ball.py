import random

results = ['It is certain', 'It is decidedly so', 'Without a doubt', 'You may rely on it', 'Most likely', 'Yes', 'try again', 'Better not tell you now', 'Don\'t count on it', 'Very doubtful', 'Outlook not so good']

x = input('This is the magic 8 ball program ask me a question and I will give you the answer')
input('What is your question for the all mighty 8 ball? \n')
print(random.choice(results))

while True:
    var1 = input('Ask another question for the all mighty 8 ball if you want to exit type "quit"\n')
    if var1 == 'quit':
        break
    print(random.choice(results))
    print('\n')

