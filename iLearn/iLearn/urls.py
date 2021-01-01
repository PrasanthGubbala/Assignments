"""iLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from iLearn_App import views

#admin and lecture modules
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.main,name='main'),


    path('lecture/',views.lecture,name='lecture'),
    path('lecture_register/',views.lecture_register,name='lecture_register'),
    path('save_lecture_details/',views.save_lecture_details,name='save_lecture_details'),
    path('lecture_login_check/',views.lecture_login_check,name='lecture_login_check'),
    path('lecture_home/',views.lecture_home,name='lecture_home'),
    path('schedule_class/',views.schedule_class,name='schedule_class'),
    path('save_class_details/',views.save_class_details,name='save_class_details'),
    path('lecture_profile/',views.lecture_profile,name='lecture_profile'),
    path('take_attendence/',views.take_attendence,name='take_attendence'),
    path('save_attendence/',views.save_attendence,name='save_attendence'),
]

#student module
urlpatterns += [
    path('student/',views.student,name='student'),
    path('student_register/',views.student_register,name='student_register'),
    path('save_student_details/',views.save_student_details,name='save_student_details'),
    path('student_login_check/',views.student_login_check,name='student_login_check'),
    path('student_home/',views.student_home,name='student_home'),
    path('student_attendence/',views.student_attendence,name='student_attendence'),
    path('student_profile/',views.student_profile,name='student_profile'),
    path('biomedical_course/',views.biomedical_course,name='biomedical_course'),
]

#parent module
urlpatterns += [
    path('parent/',views.parent,name='parent'),
    path('parent_register/',views.parent_register,name='parent_register'),
    path('save_parent_details/',views.save_parent_details,name='save_parent_details'),
    path('parent_login_check/',views.parent_login_check,name='parent_login_check'),
    path('parent_home/',views.parent_home,name='parent_home'),
    path('parent_profile/',views.parent_profile,name='parent_profile'),
    path('student_progress/',views.student_progress,name='student_progress'),
]