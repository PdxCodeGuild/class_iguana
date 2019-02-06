from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.index),
    path('savetodo/', views.savetodo, name='savetodo')
]