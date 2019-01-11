import random
class Emoticon_gen:

    def __init__(self, eyes, nose, mouth):
        self.eyes = random.choice(eye_list)
        self.nose = random.choice(nose_list)
        self.mouth = random.choice(mouth_list)

    def emoji(self):
        return self.eyes + self.nose + self.mouth


eye_list = [':', ';', 'x']
nose_list = ['^', '*', '+']
mouth_list = [')', '(', 'o']
emoticon = Emoticon_gen(eye_list, nose_list, mouth_list)
print(emoticon.emoji())

