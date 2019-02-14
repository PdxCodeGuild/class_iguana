from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('home/', views.home_view),
    path('posh/', views.posh_view),
    path('contact/', views.contact_view),
    path('about/', views.about_view),
    path('product/', views.product_detail_view),
]
