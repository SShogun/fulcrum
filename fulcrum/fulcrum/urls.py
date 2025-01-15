from django.urls import path
from core.views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', Home, name="Home"),
    path('student-reg/', Std_reg, name='student-reg'),
    path('student-login/', Std_login, name='student-login'),
    path('profile/', Profile, name='profile'),
    
    path('teacher-login/', TeacherLogin, name='teacher-login'),
    path('teacher-reg/', TeacherReg, name='teacher-reg'),
    path('teacher-profile/', TeacherProfile, name='teacher-profile'),
    
    path('courses/', CourseList, name='courses'),
    path('add-course/', addCourse, name='add-course'),
    path('course-enroll/', courseEnroll, name='course-enroll'),
    path('enroll-course/<int:course_id>/', enroll_course, name='enroll-course'),
]