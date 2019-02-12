from django.contrib import admin

from .models import Student, StudentLab, Lab, LabSection

admin.site.register(Student)
admin.site.register(StudentLab)
admin.site.register(Lab)
admin.site.register(LabSection)
