from django.shortcuts import render, reverse, redirect
from .models import Author, Book
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import User_Form, Login_Form


def index(request):
    books = Book.objects.prefetch_related('author')
    return render(request, 'library/index.html', {'books':books})


def signup(request):
    form = User_Form()
    return render(request, 'library/signup.html', {'form': form})


def profile(request):
    return render(request, 'library/profile.html')


def login(request):
    form = Login_Form()
    return render(request, 'library/login.html', {'form': form})


def newuser(request):
    username = request.POST['username']
    password = request.POST['password']


    user = User.objects.create_user(username, '', password)
    user.save()
    return HttpResponseRedirect(reverse('library:index'))