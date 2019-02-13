from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# from django.utils import timezone
# question = Question(question_text='how\'s your day going?', pub_date=timezone.now())
# question.save()
#
# choice1 = Choice(question=question, choice_text='great')
# choice2 = Choice(question=question, choice_text='terrible', votes=3)
#
# choice1.save()
# choice2.save()
