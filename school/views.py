from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Student, Class, Grade, Attendance

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def classes(request):
    classes = Class.objects.all()
    return render(request, 'classes.html', {'classes': classes})

def grades(request):
    grades = Grade.objects.all()
    return render(request, 'grades.html', {'grades': grades})

def attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance.html', {'attendance': attendance_records})
