from django.shortcuts import render
from .models import Author, Book


def index(request):
    books = Book.objects.prefetch_related('author')
    return render(request, 'library/index.html', {'books':books})

def signup(request):
    return render(request, 'library/signup.html')