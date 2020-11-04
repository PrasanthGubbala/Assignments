from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Employeedetails
from datetime import datetime
from matplotlib import pyplot as plt

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
        # plt.plot(age, sal)
        # plt.xlabel('Ages')
        # plt.ylabel('Salarie')
        # plt.title('Salary Estimation! Salary estimated by using theire ages.')
        # graph = plt.show()
        return render(request,'dashboard.html',{'age':age,'sal':sal})

    except Employeedetails.DoesNotExist:
        return render(request,'dashboard.html',{'message':'No Details Are Fount In DataBase To Plote The Graph.'})

def register(request):
    return render(request,'register.html')

def save_details(request):
    name = request.POST.get('e1')
    date = request.POST.get('e2')
    location = request.POST.get('e3')
    salary = request.POST.get('e4')
    password = request.POST.get('e5')
    try:
        Employeedetails(name=name, dob=date, location=location, salary=salary, password=password).save()
        messages.success(request, 'successfully registered')
        return redirect('dashboard')
    except:
        messages.error(request,'Name field maintaining unique constraint-please go with another name.')
        return redirect('register')

def login(request):
    return render(request,'login.html')

def login_check(request):
    if request.method == "POST":
        un = request.POST.get('l1')
        ps = request.POST.get('l2')
        try:
            res = Employeedetails.objects.get(name=un, password=ps)
            request.session['app_status'] = True
            request.session['app_username'] = res.idno
            return render(request,'user.html',{'user':res})
        except Employeedetails.DoesNotExist:
            messages.error(request, 'Details are Invalid or Doesnot Exist')
            return redirect('login')
    else:
        request.session["app_status"] = False
        return render(request,'login.html',{'message':'Loged Out Successfully'})


# def update(request):
#     return render(request, 'update.html')

def getdetails_from_db(request):
    id = request.GET.get('idno')
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
    password = request.POST.get('e5')
    Employeedetails.objects.filter(idno=id).update(name=name,dob=date,location=location,salary=salary,password=password)
    messages.success(request,'Details Are Updated Successfully')
    return redirect('user',pk=id)


def user(request,pk):
    res = Employeedetails.objects.get(idno=pk)
    return render(request,'user.html',{'user':res})


def delete(request):
    id = request.GET.get('idno')
    res = Employeedetails.objects.get(idno=id)
    res.delete()
    messages.success(request,'Your details are deleted successfully')
    return redirect('login')