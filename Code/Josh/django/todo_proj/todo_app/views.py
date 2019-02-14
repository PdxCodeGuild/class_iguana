from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo_app/index.html', {'title': 'hello world!', 'todo_items': todo_items})

def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))
    