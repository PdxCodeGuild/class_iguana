from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')
    publish_year = models.IntegerField(validators=[
            MaxValueValidator(int(date.today().strftime("%Y"))),
            MinValueValidator(0)
        ])

    def __str__(self):
        return self.title

    def display_author(self):
        author_str = ''
        for author in self.author.all():
            if (author_str != ''):
                author_str += ', ' + str(author)
            else:
                author_str += str(author)
        return author_str



class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name