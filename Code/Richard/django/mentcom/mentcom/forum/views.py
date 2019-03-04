from django.shortcuts import render, get_object_or_404
from .models import Topic, User, Post, Comment
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    topics = Topic.objects.order_by('-published_date')
    context = {
        'topics' : topics
    }
    return render(request, 'forum/index.html', context)


def login_template(request):
    return render(request, 'forum/login.html', {})


def savepost(request):
    post_data = request.POST['post_text']
    topic_id = request.POST['topic_id']
    post = Post(text=post_data, author=request.user, topic_id=topic_id)
    post.save()
    return HttpResponseRedirect(reverse('forum:index'))

def edit_post(request):
    post_data = request.POST['edit_text']
    post_id = request.POST['post_id']
    post = get_object_or_404(Post, pk=post_id)
    post.text = post_data
    post.save()
    return HttpResponseRedirect(reverse('forum:index'))

def delete_post(request):
    post_id = request.POST["post_id"]
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('forum:index'))

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    next = request.POST['next']

    if password != confirm_password:
        return HttpResponseRedirect(reverse('forum:index'))

    user = User.objects.create_user(username, email, password)
    login(request, user)

    if next == '':
        return HttpResponseRedirect(reverse('forum:index'))
    return HttpResponseRedirect(next)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    next = request.POST['next']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next == '':
            return HttpResponseRedirect(reverse('forum:index'))
        return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse('forum:index'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:index'))