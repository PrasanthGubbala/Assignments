from django.shortcuts import render,redirect
from .models import Employeedetails

def dashboard(request):
    return render(request,'dashboard.html')


def register(request):
    return render(request,'register.html')


def save_details(request):
    name = request.POST.get('e1')
    date = request.POST.get('e2')
    location = request.POST.get('e3')
    salary = request.POST.get('e4')
    Employeedetails(name=name,dob=date,location=location,salary=salary).save()
    return redirect('dashboard')

def update(request):

    return render(request, 'update.html')

