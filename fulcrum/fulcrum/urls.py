from django.urls import path
from core.views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Std_reg, name='student-reg'),
    path('student-login/', Std_login, name='student-login'),
    path('profile/', Profile, name='profile'),
    path('teacher-login/', TeacherLogin, name='teacher-login'),
    path('teacher-reg/', TeacherReg, name='teacher-reg'),
    path('teacher-profile/', TeacherProfile, name='teacher-profile'),
]