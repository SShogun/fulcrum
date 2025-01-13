from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import *
# Create your views here.
def Std_reg(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        if not Student.objects.filter(email=email).exists():
            student = Student.objects.create(
                student_id=data.get('student_id'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                password=make_password(data.get('password'))
            )
            messages.success(request, 'Registration successful!')
            return redirect('student-login')
    return render(request, 'studentReg.html')

def Std_login(request):
    if request.method != 'POST':
        return render(request, 'studentLogin.html')
    data = request.POST
    student_id = data.get('student_id')
    password = data.get('password')

    if Student.objects.filter(student_id=student_id).exists():
        student = Student.objects.get(student_id=student_id)
        if check_password(password, student.password):
            request.session['student_id'] = student_id
            return redirect('profile')
        messages.error(request, 'Invalid password!')
    else:
        messages.error(request, 'Student ID not found!')
    return render(request, 'studentLogin.html')

def Profile(request):
    if student_id := request.session.get('student_id'):
        student = Student.objects.get(student_id=student_id)
        return render(request, 'profile.html', {'student': student})
    return redirect('student-login')