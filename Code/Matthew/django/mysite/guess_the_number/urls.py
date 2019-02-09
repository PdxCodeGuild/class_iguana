

from django.urls import  path

from . import views

app_name = 'guess_the_number'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.game, name='game'),
    path('<int:game_id>/guess', views.guess, name='guess'),
    path('newgame/', views.newgame, name='newgame'),
]
