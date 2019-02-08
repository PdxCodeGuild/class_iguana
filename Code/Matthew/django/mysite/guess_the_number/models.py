from django.db import models

class GameGuess(models.Model):
    guess = models.IntegerField()

    def __str__(self):
        return str(self.guess)

    


    # o
    # o_clone = exec(repr(o))
    def __repr__(self):
        return f'GameGuess(guess={self.guess})'
