import random
print( 'Welcome to the Magic 8 Ball')
question = input(' What is your question?')
print (question)
responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely']
choice = random.choice(responses)

print(choice)
