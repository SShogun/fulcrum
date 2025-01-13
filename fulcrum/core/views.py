from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def Std_reg(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data.get('first_name')
        lastname = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        
        if not Student.objects.filter(email=email).exists() and not Student.objects.filter(phone=phone).exists():
            student = Student.objects.create(
                first_name = firstname,
                last_name = lastname,
                email = email,
                phone = phone
            )
            return render(request, 'studentReg.html', {'message': 'Registration successful!'})
        else:
            messages.error(request, 'Email or phone number already exists!')
            return render(request, 'studentReg.html')
    
    return render(request, 'studentReg.html')