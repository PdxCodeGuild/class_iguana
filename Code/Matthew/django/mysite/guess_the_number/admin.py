from django.contrib import admin


from .models import Game, GameGuess

admin.site.register(Game)
admin.site.register(GameGuess)
