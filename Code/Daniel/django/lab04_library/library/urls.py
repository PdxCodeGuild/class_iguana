from django.urls import path
from . import views


app_name='library'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('newuser/', views.newuser, name='newuser'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]