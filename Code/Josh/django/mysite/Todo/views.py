from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todoitem
from django.views import generic

def index(request):
    todo_items = Todoitem.objects.filter(completed=False)
    completed_items = Todoitem.objects.filter(completed=True)
    context = {'title':"The todo list!!",
                'todo_items': todo_items,
                'completed_items': completed_items,
                'title2':"Finished tasked list"}
    return render(request, 'Todo/index.html', context)

def savetodo(request):
    todo_text = request.POST['todo_text'] # taking the todo_text from the index.html when the form is submitted and passing it into the function and setting it as the same name as it is on the index.html page
    todo_item = Todoitem(text=todo_text, completed=False) # taking the var from above passing it into the model class Todoitem and setting it to the var todo_item 
    todo_item.save() #saving the variable created
    return HttpResponseRedirect(reverse('todo_app:index')) 

def completedtodo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = Todoitem.objects.get(pk=todo_item_id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))

def deletetodo(request):
    print('\n' * 10, request.POST)
    delete_item_id = request.POST['delete_item_id']
    delete_item = Todoitem.objects.get(pk=delete_item_id)
    print(f'---------deletetod ran-----------------')
    delete_item.delete()
    return HttpResponseRedirect(reverse('todo_app:index'))