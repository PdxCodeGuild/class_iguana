

from django.urls import  path

from . import views

app_name = 'guess_the_number'
urlpatterns = [
    path('', views.index, name='index')
]
