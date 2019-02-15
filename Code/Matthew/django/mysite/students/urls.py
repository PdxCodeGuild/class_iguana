

from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('student_index/', views.student_index, name='student_index'),
]
