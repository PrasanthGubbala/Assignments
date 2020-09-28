from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Employeedetails
from datetime import datetime

def dashboard(request):
    try:
        res = Employeedetails.objects.all()
        present_year = datetime.now().year
        age = []
        sal = []
        for x in res:
            a = present_year-x.dob.year
            s = x.salary
            age.append(a)
            sal.append(s)


        return render(request,'dashboard.html')
    
    except Employeedetails.DoesNotExist:
        return render(request,'dashboard.html',{'message':'No Details Are Fount In DataBase To Plote The Graph.'})

def register(request):
    return render(request,'register.html')

def save_details(request):
    name = request.POST.get('e1')
    date = request.POST.get('e2')
    location = request.POST.get('e3')
    salary = request.POST.get('e4')
    Employeedetails(name=name,dob=date,location=location,salary=salary).save()
    messages.success(request,'successfully registered')
    return redirect('dashboard')

def update(request):
    return render(request, 'update.html')

def getdetails_from_db(request):
    id = request.POST.get('idno')
    try:
        res = Employeedetails.objects.get(idno=id)
        return render(request,'update_details.html',{'user':res})
    except Employeedetails.DoesNotExist:
        messages.error(request,'Given IDNO is not exist in database! pleace register again')
        return redirect('update')

def update_details(request):
    id = request.POST.get('idno')
    name = request.POST.get('e1')
    date = Employeedetails.objects.get(idno=id).dob
    location = request.POST.get('e3')
    salary = request.POST.get('e4')
    Employeedetails.objects.filter(idno=id).update(name=name,dob=date,location=location,salary=salary)
    messages.success(request,'Details Are Updated Successfully')
    return redirect('update')