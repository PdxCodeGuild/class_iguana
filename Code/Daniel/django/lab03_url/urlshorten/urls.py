from django.urls import path
from . import views

app_name = 'urlshorten'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('redirect/<str:code>/', views.redirect_url, name='redirect'),
]