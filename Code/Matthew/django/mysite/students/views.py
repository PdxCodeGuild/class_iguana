from django.shortcuts import render
from django.http import HttpResponse

from .models import Student, LabSection, StudentLab

def index(request):
    students = Student.objects.order_by('name')


    rows = []
    for section in LabSection.objects.order_by('index'):
        for lab in section.lab_set.order_by('index'):
            row = {
                'section_name': section.name,
                'lab_name': f'Lab {lab.index} {lab.name}',
                'lab_grades': []
            }
            for student in students:
                grade = '<span style="color:blue">?</span>'
                # go find a studentlab for this student and lab
                if StudentLab.objects.filter(student=student, lab=lab).exists():
                    grade = StudentLab.objects.get(student=student, lab=lab).grade
                    grade = '<span style="color:green">✓</span>' if grade else '<span style="color:red">✗</span>'
                row['lab_grades'].append(grade)
            rows.append(row)


    print(rows)

    return render(request, 'students/index.html', {'students': students, 'rows': rows})
