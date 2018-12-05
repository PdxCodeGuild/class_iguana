import random

magic_answers = ['head west', 'no', 'maybe', 'yes', 'indefinitely yes', 'subjectively no', 'subjectively yes', 'objectively no', 'ask again', 'hard pass']

user_input = input('ask me something,\n go ahead ask anything...')
magic_answer = random.choice(magic_answers)
print(magic_answer)
print('\n*dont worry, someone loves you my friend*')


