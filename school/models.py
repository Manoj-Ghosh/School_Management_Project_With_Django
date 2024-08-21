from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_model = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.class_model}: {self.grade}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present/Absent

    def __str__(self):
        return f"{self.student} - {self.date}: {self.status}"
