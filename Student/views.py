
from django.shortcuts import render,redirect
from .models import *
from django.views import View
from .forms import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

class StudentAdd(LoginRequiredMixin,View):
    login_url='/'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:   # only admin
            messages.error(request, "You are not allowed to add students")
            return redirect('/students/students/')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        
        context={
            'student_form':Student_Form()
        }
        
        return render(request,'students_add.html',context)
    
    def post(self,request):
          
        student_form=Student_Form(request.POST)
        
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "Student added successfully ")
        
            return redirect('/students/students/')
        
        
        

class AllStudents(LoginRequiredMixin,View):
    
    login_url='/'
    
    def get(self,request):
        
        query = request.GET.get('q')
        dept = request.GET.get('dept')
        
        students = StudentModel.objects.all()
        
        # Search by name
        if query:
            students = students.filter(Name__icontains=query)
        
        #  Filter by department
        if dept:
            students = students.filter(Department=dept)
            
         # PAGINATION 
        paginator = Paginator(students, 5)  # 5 students per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'all_students': page_obj,
            'query': query,
            'dept': dept
        }
        
        return render(request,'students.html',context)
    

class DeleteStudent(LoginRequiredMixin,View):
    
    login_url='/'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, "You are not allowed to delete students")
            return redirect('/students/students/')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id):
        selected_Student=StudentModel.objects.get(id=id)
        selected_Student.delete()
        messages.success(request, "Student deleted successfully ")
        return redirect('/students/students/')
    
class UpdateStudent(LoginRequiredMixin,View):
    
    login_url='/'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, "You are not allowed to update students")
            return redirect('/students/students/')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id):
        select_student=StudentModel.objects.get(id=id)
        
        context={
            'student_form':Student_Form(instance=select_student)
        }        

        return render(request,'students_add.html',context)
    
    def post(self,request,id):
        
        select_student=StudentModel.objects.get(id=id)
        
        student_form=Student_Form(request.POST,instance=select_student)
        
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "Student updated successfully ")
            return redirect('/students/students/')
        
        
        
class DashboardView(LoginRequiredMixin,View):
    login_url='/'

    def get(self, request):
        total_students = StudentModel.objects.count()
        department_data = StudentModel.objects.values('Department').annotate(
        total=Count('id'))
        context = {
            'total_students': total_students,
            'department_data': department_data,
        }

        return render(request, 'dashboard.html', context)