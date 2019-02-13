from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home_view),
    path('', views.posh_view),
    path('', views.contact_view),
    path('', views.about_view),
]
