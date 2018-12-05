#lab5_magicball.py
import random
#create list of possible responses

response_list = ['It is certain', 'It is decidedly so','Without a doubt','Yes - definitely', 'As I see it, yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Don\'t count on it.','My reply is no','My sources say no.','Outlook not so good.','Very doubtful.']

#create user name for greeting and ask ask input question

user_name = input("Please enter your name:\n")
question = input(f'Hello {user_name}, what "yes-or-no" question would you like to ask 8-ball?\n')
answer = random.choice(response_list)
print(answer)
next_question = 'done'
next_question = input('press any key + Enter to ask another question, or if you are finished, type "done"\n')
while next_question != 'done':
    next_question = input('What is your next question?')
    next_answer = random.choice(response_list)
    print(next_answer)
    if next_question == 'done':
        print(f'Thanks for playing {user_name}. Bye')



# if one_more not in user_choice:
#     one_more = input('Type "continue" to ask another question, or if you are finished, type "done"\n')
# elif one_more == 'continue':
#     one_more = input(f'{user_name}, what "yes-or-no" question would you like to ask 8-ball?\n')
# elif one_more == 'done':
#



#user_choice = ['continue', 'done']