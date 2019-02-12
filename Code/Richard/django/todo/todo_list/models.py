from django.db import models

# Create your models here.
class TodoList(models.Model):
    todo_item = models.CharField(max_length=200)
    
    def __str__(self):
        return self.todo_item