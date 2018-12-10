"""Author: Richard Sherman
2018-12-03
magic-8-ball.py, simulates the 'magic 8-ball' game"""

import random

predictions = ['That is a good question.',
               'People ask me that question all the time.',
               'Further investigation is needed.',
               'You ask difficult questions!',
               'Not every question has a good answer.',
               'I\'ll have to get back to you on that.',
               'An answer to that question could be very helpful.',
               'To answer that question, I would have to break a confidence.\nAs an honorable person, I would never do that.',
               ]
print('Welcome to the Magic 8-ball, where your questions are answered.\nYou can ask me anything, but most people want to know about the future.')
print('If you want to stop, just type "done" without quotation marks')

question = input('Please ask me a question: ')
print(f"\n{random.choice(predictions)}")