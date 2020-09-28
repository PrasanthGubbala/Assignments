from django.contrib import messages
from django.shortcuts import render,redirect
from .models import EmployeeDetails,Admin
from django.core.mail import send_mail
from EmployeeDetails2 import settings
import random

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
            total = users.count()
            return render(request, 'admin_dashboard.html',{'users':users,'total':total})
        except Admin.DoesNotExist:
            messages.error(request, 'Given Details Are Invalid')
            return redirect('admin')
    else:
        request.session['admin_status'] = False
        return render(request,'admin_login.html',{'message':'Loged Out Successfully'})

def change_to_active(request):
    b1 = request.POST.get('b1')
    user = EmployeeDetails.objects.get(username=b1)
    user.status = 'active'
    user.save()
    users = EmployeeDetails.objects.all()
    total = users.count()
    return render(request,'admin_dashboard.html',{'users':users,'total':total})

def change_to_deactive(request):
    b2 = request.POST.get('b2')
    user = EmployeeDetails.objects.get(username=b2)
    user.status = 'deactive'
    user.save()
    users = EmployeeDetails.objects.all()
    total = users.count()
    return render(request, 'admin_dashboard.html', {'users': users,'total':total})

def change_to_delete(request):
    try:
        b3 = request.POST.get('b3')
        user = EmployeeDetails.objects.get(username=b3)
        user.delete()
        users = EmployeeDetails.objects.all()
        total = users.count()
        return render(request, 'admin_dashboard.html', {'users': users,'total':total})
    except EmployeeDetails.DoesNotExist:
        return render(request,'admin_dashboard.html',{'message':'No Details Are Available'})


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
        send_mail("Verification Email!",
                  "You are signup into the 'Employee Management Tool! you have an account on EMT' now you can signin into EMT",
                   settings.EMAIL_HOST_USER,
                  [email]
                  )
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
            if res.status == 'active':
                request.session['app_status'] = True
                request.session['app_username'] = res.username
                return redirect('user', pk=res.username)
            else:
                messages.error(request, 'Admin Not yet Approved')
                return redirect('welcome')
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

def change_password(request):
    p1 = request.POST.get('p1')
    p2 = request.POST.get('p2')
    un = request.POST.get('un')
    if p1 == p2:
        user = EmployeeDetails.objects.get(username=un)
        user.password = p1
        user.save()
        res = EmployeeDetails.objects.all()
        return render(request, 'user.html', {'user': res,'message':'Password Changed Successfully'})
    else:
        messages.error(request,'Please Enter Same Input In Both Fields')
        return redirect('user',pk=request.session['app_username'])


def forgot_password(request):
    return render(request,'forgot_password.html')

rno = 0
def send_otp_to_email(request):
    global rno
    e1 = request.POST.get('e1')
    try:
        user = EmployeeDetails.objects.get(email=e1)
        rnum = random.randint(100000,999999)
        rno = rnum
        send_mail('Security Authentication',
                  'You want to change your Password! so you must and should do the authentication then only you will get your password! You need to confirm this One Time Password in youe EMT..OTP:'+ str(rnum) +'.',
                  settings.EMAIL_HOST_USER,
                  [e1]
                  )
        return render(request,'check_otp.html',{'user':user.username})

    except EmployeeDetails.DoesNotExist:
        messages.error(request,'Entered Details Are Does Not Exist! Please Sign Up')
        return redirect('signup')

def submit_otp(request):
    user = request.POST.get('user')
    otp = request.POST.get('otp')
    if rno == int(otp):
        return render(request,'set_new_password.html',{'user':user})
    else:
        messages.error(request,'Given OTP is Invalid! Please Try Again,')
        return redirect('forgot_password')

def save_new_password(request):
    p1 = request.POST.get('p1')
    p2 = request.POST.get('p2')
    user = request.POST.get('user')
    if p1 == p2:
        user_detail = EmployeeDetails.objects.get(username=user)
        user_detail.password = p1
        user_detail.save()
        messages.success(request,'Password Changed Successfully')
        return redirect('signin')
    else:
        messages.error(request, "did'nt match password! you are trying to insert different password")
        return render(request,'set_new_password.html',{'user':user})