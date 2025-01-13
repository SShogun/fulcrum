from django.db import models
from phonenumber_field.modelfields import *
from django.contrib.auth.hashers import make_password
# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, default='') 
    password = models.CharField(max_length=128, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneNumberField()

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'