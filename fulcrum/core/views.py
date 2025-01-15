from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import *
from functools import *
from django.shortcuts import get_object_or_404
# Create your views here.

def Home(request):
    return render(request, 'home.html')

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
    return render(request, 'student/studentReg.html')

def teacher_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('teacher_id'):
            messages.error(request, 'Please login first!')
            return redirect('teacher-login')
        return view_func(request, *args, **kwargs)
    return wrapper

def Std_login(request):
    if request.method != 'POST':
        return render(request, 'student/studentLogin.html')
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
    return render(request, 'student/studentLogin.html')

def Profile(request):
    if student_id := request.session.get('student_id'):
        student = Student.objects.get(student_id=student_id)
        return render(request, 'student/profile.html', {'student': student})
    return redirect('student-login')

def courseEnroll(request):
    if not request.session.get('student_id'):
        messages.error(request, 'Please login first!')
        return redirect('student-login')
    
    student_id = request.session.get('student_id')
    student = Student.objects.get(student_id=student_id)
    courses = Course.objects.all()
    
    context = {
        'student': student,
        'courses': courses,
    }
    return render(request, 'courses/courseEnroll.html', context)

from django.shortcuts import get_object_or_404

def enroll_course(request, course_id):
    if not request.session.get('student_id'):
        messages.error(request, 'Please login first!')
        return redirect('student-login')
    
    student_id = request.session.get('student_id')
    student = get_object_or_404(Student, student_id=student_id)
    course = get_object_or_404(Course, id=course_id)
    
    if course.enrolled.filter(student_id=student_id).exists():
        course.enrolled.remove(student)
        messages.success(request, f'You have successfully unenrolled from {course.name}!')
    else:
        course.enrolled.add(student)
        messages.success(request, f'You have successfully enrolled in {course.name}!')
    
    return redirect('course-enroll')

@teacher_login_required
def TeacherProfile(request):
    if teacher_id := request.session.get('teacher_id'):
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        return render(request, 'teacher/teacherProfile.html', {'teacher': teacher})
    return redirect('teacher-login')

def TeacherReg(request):
    if request.method == 'POST':
        data = request.POST
        teacher = Teacher.objects.create(
            teacher_id=data.get('teacher_id'),
            password=make_password(data.get('password'))  # Ensure password is hashed
        )
        messages.success(request, 'Registration successful!')
        return redirect('teacher-login')
    return render(request, 'teacher/teacherReg.html')

def TeacherLogin(request):
    if request.method == 'POST':
        data = request.POST
        teacher_id = data.get('teacher_id')
        password = data.get('password')
        
        try:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
            # Debug prints
            print(f"Input password: {password}")
            print(f"Stored hashed password: {teacher.password}")
            print(f"Password check result: {check_password(password, teacher.password)}")
            
            if check_password(password, teacher.password):
                request.session['teacher_id'] = teacher_id
                return redirect('teacher-profile')
            else:
                messages.error(request, 'Invalid password!')
        except Teacher.DoesNotExist:
            messages.error(request, 'Teacher ID not found!')
            
    return render(request, 'teacher/teacherLogin.html')

def CourseList(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courseList.html', context)


@teacher_login_required
def addCourse(request):
    if request.method == 'POST':
        data = request.POST
        teacher_id = request.session.get('teacher_id')
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        course = Course.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            faculty=teacher
        )
        messages.success(request, 'Course created successfully!')
        return redirect('courses')
    return render(request, 'courses/addCourse.html')