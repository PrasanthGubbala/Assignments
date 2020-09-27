from django.contrib import messages
from django.shortcuts import render,redirect
from .models import EmployeeDetails,Admin

#admin phase
def admin(request):
    return render(request,'admin_login.html')

def admin_login_check(request):
    if request.method == 'POST':
        un = request.POST.get('s1')
        ps = request.POST.get('s2')
        try:
            res = Admin.objects.get(username=un, password=ps)
            request.session['admin_status']=True
            request.session['admin_username'] = res.username
            users = EmployeeDetails.objects.all()
            return render(request, 'admin_dashboard.html',{'users':users})
        except Admin.DoesNotExist:
            messages.error(request, 'Given Details Are Invalid')
            return redirect('admin')
    else:
        request.session['admin_status'] = False
        return render(request,'admin_login.html',{'message':'Loged Out Successfully'})




#user phase
def welcome(request):
    return render(request,'welcome.html')

def signup(request):
    return render(request,'signup.html')

def save_details(request):
    name = request.POST.get('e1')
    email = request.POST.get('e2')
    username = request.POST.get('e3')
    password = request.POST.get('e4')
    try:
        EmployeeDetails(name=name, email=email, username=username, password=password).save()
        messages.success(request, 'You Are Successfully Registered! Now You Can Sign-In')
        return redirect('signin')
    except:
        messages.error(request,'Entered Data Is Matching With Existing Data! Please SignUp With Another Creadentials.')
        return redirect('signup')

def signin(request):
    return render(request,'signin.html')

def signin_check(request):
    if request.method == "POST":
        un = request.POST.get('s1')
        ps = request.POST.get('s2')
        try:
            res = EmployeeDetails.objects.get(username=un, password=ps)
            request.session['app_status'] = True
            request.session['app_username'] = res.username
            return redirect('user', pk=res.username)
        except EmployeeDetails.DoesNotExist:
            messages.error(request, 'Invalid Username or Password')
            return redirect('signin')
    else:
        request.session["app_status"] = False
        messages.error(request, 'Logedout Successfully!')
        return render(request, "signin.html")

def user(request,pk):
    res = EmployeeDetails.objects.get(username=pk)
    return render(request,'user.html',{'user':res})