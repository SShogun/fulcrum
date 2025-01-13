from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import *
# Create your views here.
def Std_reg(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data.get('first_name')
        lastname = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        student_id = data.get('student_id')
        
        if not Student.objects.filter(email=email).exists() and not Student.objects.filter(phone=phone).exists():
            student = Student.objects.create(
                student_id = student_id,
                first_name = firstname,
                last_name = lastname,
                email = email,
                password = make_password(password)
            )
            return render(request, 'studentReg.html', {'message': 'Registration successful!'})
        else:
            messages.error(request, 'Email or phone number already exists!')
            return render(request, 'studentReg.html')
    
    return render(request, 'studentReg.html')