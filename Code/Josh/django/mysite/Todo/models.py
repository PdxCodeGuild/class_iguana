from django.db import models

class Todoitem(models.Model):

    text = models.CharField(max_length=200)
    completed = models.BooleanField()
    def __str__(self):
        return self.text