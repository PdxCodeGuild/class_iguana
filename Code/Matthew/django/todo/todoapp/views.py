from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def index(request):

    todo_items = TodoItem.objects.all()
    context = {
        'todo_items': todo_items,
    }
    return render(request, 'todoapp/index.html', context)


def addtodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))
