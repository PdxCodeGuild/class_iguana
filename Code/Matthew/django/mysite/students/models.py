from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class LabSection(models.Model):
    name = models.CharField(max_length=200)
    index = models.IntegerField()

    def __str__(self):
        return f'{self.index} {self.name}'

    def get_ordered_labs(self):
        return self.lab_set.order_by('index')

class Lab(models.Model):
    name = models.CharField(max_length=200)
    section = models.ForeignKey(LabSection, on_delete=models.PROTECT)
    index = models.IntegerField()

    def __str__(self):
        return f'{self.section.name} - Lab {self.index} {self.name}'

class StudentLab(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.PROTECT)
    grade = models.BooleanField()

    def __str__(self):
        return f'{self.student} {self.lab} {self.grade}'

    def get_grade(self):
        return 'pass' if self.grade else 'fail'
