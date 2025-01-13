from django.urls import path
from core.views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Std_reg, name='student-reg'),
    path('student-login/', Std_login, name='student-login'),
    path('profile/', Profile, name='profile'),
]