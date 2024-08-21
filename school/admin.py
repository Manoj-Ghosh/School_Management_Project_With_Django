from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student, Class, Grade, Attendance

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(Attendance)
