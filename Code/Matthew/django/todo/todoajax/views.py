from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import TodoItem

import json

def index(request):
    return render(request, 'todoajax/index.html', {})


def get_todos(request):
    data = {'todo_items': []}
    todo_items = TodoItem.objects.all()
    for todo_item in todo_items:
        data['todo_items'].append({'text': todo_item.text, 'completed': todo_item.completed})
    return JsonResponse(data)

def save_todo(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()
    return HttpResponse('ok')
