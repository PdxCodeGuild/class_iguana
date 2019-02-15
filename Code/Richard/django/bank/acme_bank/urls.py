from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/<int:account_id>/', views.account_detail, name='account_detail'),
]
