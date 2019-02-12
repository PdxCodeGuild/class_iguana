from django.shortcuts import render
from todo_list.models import TodoList

# Create your views here.

def index(request):
    todo_items = TodoList.objects.all()

    context = {
        'todo_items': todo_items
    }
    return render(request, 'index.html', context=context)