from django.db import models


class StudentModel(models.Model):
    
    DEPARTMENT_CHOICES = [
        ('CSE', 'CSE'),
        ('IT', 'IT'),
        ('ECE', 'ECE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
        ('EEE', 'EEE'),
        
        
    ]
    Name=models.CharField(max_length=100,null=True)
    Age=models.IntegerField()
    Department=models.CharField(max_length=100, null=True ,choices=DEPARTMENT_CHOICES)
    Email=models.EmailField()
    Join_Date=models.DateField()
    