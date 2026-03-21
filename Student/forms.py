# from django.forms import ModelForm
from django import forms
from .models import *

class Student_Form(forms.ModelForm):
    
    class Meta:
        model=StudentModel
        fields='__all__'
        
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Age':forms.NumberInput(attrs={'class':'form-control'}),
            'Department': forms.Select(attrs={'class':'form-control'}), 
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Join_Date':forms.DateInput(attrs={'class':'form-control'}),

            
        }
        