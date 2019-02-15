from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('products/', views.products_view, name='product'),
    path('contact/', views.contact_view, name='contact'),
    path('cart/', views.cart_view, name='cart'),
]
