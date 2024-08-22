from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('classes/', views.classes, name='classes'),
    path('grades/', views.grades, name='grades'),
    path('attendance/', views.attendance, name='attendance'),
    
]
