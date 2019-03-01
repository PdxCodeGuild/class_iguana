from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_template, name='login'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('savepost/', views.savepost, name='savepost'),
    path('logout/', views.logout_user, name='logout'),
    
]