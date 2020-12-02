from django.contrib import messages
from django.shortcuts import render, redirect

from bb_app.models import User


def main(request):
    return render(request,'main.html')

def register(request):
    return render(request,'register.html')

def save_details(request):
    name = request.POST.get('t1')
    age = request.POST.get('t2')
    gender = request.POST.get('t3')
    contact = request.POST.get('t4')
    password = request.POST.get('t5')
    password2 = request.POST.get('t6')
    if  password == password2:
        User(name=name,age=age,gender=gender,contact=contact,amount=100.00,password=password).save()
        messages.success(request,'Account is Successfully Created')
        return redirect('login')
    else:
        messages.error(request,'Password Mismatch')
        return redirect('login')

def login(request):
    return render(request,'login.html')

def login_check(request):
    if request.method == 'POST':
        an = request.POST.get('t1')
        ps = request.POST.get('t2')
        try:
            User.objects.get(number=an,password=ps)
            request.session['user_status'] = True
            request.session['user_num'] = an
            return redirect('user')
        except User.DoesNotExist:
            messages.error(request,'User details are does not exist')
            return redirect('login')
    else:
        request.session['user_status'] = False
        messages.error(request,'Logout Successfully')
        return redirect('login')

def user(request):
    an = request.session['user_num']
    return render(request,'user.html',{'user':User.objects.get(number=an)})


def account(request):
    an = request.session['user_num']
    return render(request,'account.html', {'user': User.objects.get(number=an)})

def transfer_money(request):
    rn = request.POST.get('t1')
    amt = request.POST.get('t2')
    an = request.session['user_num']
    user = User.objects.get(number=an)
    if amt < user.amount:
        reciever = User.objects.get(number=rn)
        reciever.amount = reciever.amount + amt
        messages.success(request,'amount transfered successfully')
        return redirect('user')
    else:
        messages.error(request,'insuffisient amount in your acount')
        return redirect('user')

