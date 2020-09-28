"""EmployeeManagement URL Configuration

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
#admin operations
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/',views.admin,name='admin'),
    path('admin_login_check/',views.admin_login_check,name='admin_login_check'),
    path('change_to_active/',views.change_to_active,name='change_to_active'),
    path('change_to_deactive/',views.change_to_deactive,name='change_to_deactive'),
    path('change_to_delete/',views.change_to_delete,name='change_to_delete'),

 ]

#user operations
urlpatterns +=[
    path('',views.welcome,name='welcome'),
    path('signup/',views.signup,name='signup'),
    path('save_details/',views.save_details,name='save_details'),
    path('signin/',views.signin,name='signin'),
    path('signin_check/',views.signin_check,name='signin_check'),
    path('user/<str:pk>',views.user,name='user'),
    path('change_password/',views.change_password,name='change_password'),

#forgot password
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('send_otp_to_email/',views.send_otp_to_email,name='send_otp_to_email'),
    path('submit_otp/',views.submit_otp,name='submit_otp'),
    path('save_new_password/',views.save_new_password,name='save_new_password'),

]
