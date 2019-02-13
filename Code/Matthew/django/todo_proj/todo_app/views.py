from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.filter(completed=False)
    completed_todo_items = TodoItem.objects.filter(completed=True)
    context = {'title': 'hello world!',
                'todo_items': todo_items,
                'completed_todo_items': completed_todo_items}
    return render(request, 'todo_app/index.html', context)

def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))

def completetodo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))
