from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import Game, GameGuess

import random


def index(request):
    games = Game.objects.filter(won__isnull=True)
    completed_games = Game.objects.filter(won__isnull=False)
    context = {'games': games, 'completed_games': completed_games}
    return render(request, 'guess_the_number/index.html', context)


def game(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {'game': game}
    return render(request, 'guess_the_number/game.html', context)

def guess(request, game_id):
    guess = int(request.POST['guess'])
    game = Game.objects.get(id=game_id)
    if guess < 1 or guess > game.upper_bound:
        return HttpResponseRedirect(reverse('guess_the_number:game', args=(game.id,)))
    if game.guesses.filter(guess=guess).exists():
        return HttpResponseRedirect(reverse('guess_the_number:game', args=(game.id,)))
    game_guess = GameGuess(guess=request.POST['guess'], game=game)
    game_guess.save()
    if guess == game.target:
        game.won = True
        game.save()
    elif game.guesses.count() >= game.upper_bound//2:
        game.won = False
        game.save()
    return HttpResponseRedirect(reverse('guess_the_number:game', args=(game.id,)))


def newgame(request):
    upper_bound = int(request.POST['upper_bound'])
    game = Game(upper_bound=upper_bound, won=None, target=random.randint(1, upper_bound))
    game.save()
    return HttpResponseRedirect(reverse('guess_the_number:game', args=(game.id,)))
