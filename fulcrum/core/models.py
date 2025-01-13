from django.db import models
from phonenumber_field.modelfields import *
from django.contrib.auth.hashers import make_password
# Create your models here.

class BaseModel(models.Model):
    password = models.CharField(max_length=128, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    class Meta:
        abstract = True
class Student(BaseModel):
    student_id = models.CharField(max_length=20, unique=True, default='') 
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True, default='') 
    password = models.CharField(max_length=128, default='')
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="")
    faculty = models.ForeignKey(Teacher, on_delete=models.CASCADE)