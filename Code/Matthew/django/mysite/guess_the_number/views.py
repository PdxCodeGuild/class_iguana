from django.shortcuts import render

from django.http import HttpResponse

from .models import GameGuess

def index(request):
    message = ''
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        game_guess = GameGuess(guess=guess)
        game_guess.save()
        message = 'you guessed: ' + str(guess)


    guesses = GameGuess.objects.order_by('guess')
    # guesses = GameGuess.objects.all()
    # guesses = [guess.guess for guess in guesses]
    # guesses.sort()
    # guesses.sort(key=lambda g: g.guess)
    context = {'guesses': guesses, 'message': message}
    return render(request, 'guess_the_number/index.html', context)
