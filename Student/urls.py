from django.urls import path
from .views import *

urlpatterns = [
    path('students_add/',StudentAdd.as_view()),
    path('students/',AllStudents.as_view() ,name="all_students"),
    
    path('delete/<int:id>',DeleteStudent.as_view() ,name="delete_student"),
    path('update/<int:id>',UpdateStudent.as_view(), name='update_student'),
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    
]
