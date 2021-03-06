"""EmployeeDetails URL Configuration

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

from app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('save_details/',views.save_details,name='save_details'),
    path('login/',views.login,name='login'),
    path('login_check/',views.login_check,name='login_check'),
    path('user/<int:pk>',views.user,name='user'),


    #path('update/',views.update,name='update'),
    path('getdetails_from_db/',views.getdetails_from_db,name='getdetails_from_db'),
    path('update_details/',views.update_details,name='update_details'),
    path('delete/',views.delete,name='delete'),
]
