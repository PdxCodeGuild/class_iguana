from django.db import models

# priority? high, medium, low
# multiple lists?

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} - {"done" if self.completed else "not done"}'
