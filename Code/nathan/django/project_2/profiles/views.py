from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def index(request):
    return render(request, 'profiles/test.html', {'titles': 'hey there', 'TodoItem': TodoItem})

def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()
    print(request.POST)
    return HttpResponseRedirect(reverse('profiles:index'))
