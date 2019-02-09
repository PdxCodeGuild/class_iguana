from django.db import models


class Game(models.Model):
    target = models.IntegerField()
    upper_bound = models.IntegerField()
    won = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'Target: {self.target}, Upper Bound: {self.upper_bound}, Won: {self.won}'

    def state(self):
        return 'pending' if self.won is None else 'won' if self.won else 'lost'

    def int_guesses(self):
        return [guess.guess for guess in self.guesses.order_by('guess')]

    def guessed_numbers(self):
        return self.upper_bound//2 - self.guesses.count()


class GameGuess(models.Model):
    guess = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='guesses')

    def __str__(self):
        return str(self.game) + ' - ' + str(self.guess)
