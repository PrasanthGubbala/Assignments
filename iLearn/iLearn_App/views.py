from django.contrib import messages
from django.shortcuts import render, redirect
from iLearn_App.models import TecherRegistration,StudentRegistration
from iLearn_App.models import ParentRegistration,ScheduleClass,StudentInfo
from datetime import datetime
from django.core.mail import send_mail
from iLearn import settings as se


#lecture module
def main(request):
    return render(request,'main.html')

def lecture(request):
    return render(request,'lecture/lecture.html')


def lecture_register(request):
    return render(request, 'lecture/lecture_register.html')


def save_lecture_details(request):
    name = request.POST.get('t1')
    age = request.POST.get('t2')
    gender = request.POST.get('t3')
    designation = request.POST.get('t4')
    contact = request.POST.get('t5')
    email = request.POST.get('t6')
    password = request.POST.get('t7')
    c_password = request.POST.get('t8')
    if password == c_password:
        tr = TecherRegistration(name=name,age=age,gender=gender,designation=designation,contact=contact,email=email,password=password,status='deactivate')
        tr.save()
        res = TecherRegistration.objects.all()
        all = list(res)
        lec = all[-1]
        send_mail('Remainding!',
                  'You are successfully registered into iLearn Portal! your ID number is '+str(lec.id)+' , now you can login into iLearn portal.',
                  se.EMAIL_HOST_USER,
                  [lec.email]
                  )
        messages.success(request,'Successfully Registered! Your ID is sent to your registered email.')
        return redirect('lecture')
    else:
        messages.error(request,'please enter same password in both fields')
        return redirect('lecture_register')


def lecture_login_check(request):
    if request.method == "POST":
        id = request.POST.get('t1')
        password = request.POST.get('t2')
        try:
            res = TecherRegistration.objects.get(id=id,password=password)
            if res.status == 'activate':
                request.session["lecture_status"] = True
                request.session["lecture_id"] = res.id
                return redirect('lecture_home')
            else:
                messages.error(request,'your account need to be activate by admin')
                return redirect('lecture')

        except TecherRegistration.DoesNotExist:
            messages.error(request,'Login details are Invalid')
            return redirect('lecture')
    else:
        request.session["lecture_status"] = False
        return render(request, "lecture/lecture.html", {"error": "Lecture Logout Successfully"})

def lecture_home(request):
    return render(request,'lecture/lecture_home.html')


def schedule_class(request):
    id = request.session['lecture_id']
    return render(request,'lecture/schedule_class.html',{'id':id})

def save_class_details(request):
    subject = request.POST.get('t1')
    l_id = request.POST.get('t2')
    time = request.POST.get('t3')
    status = request.POST.get('t4')
    lecture = TecherRegistration.objects.get(id=l_id)
    ScheduleClass(subject=subject,lecture=lecture,time=time,status=status).save()
    messages.success(request,'Successfully Class Scheduled')
    return redirect('schedule_class')

def lecture_profile(request):
    id = request.session['lecture_id']
    res = TecherRegistration.objects.get(id=id)
    return render(request,'lecture/lecture_profile.html',{'data':res})

def take_attendence(request):
    return render(request,'lecture/take_attendence.html')

def save_attendence(request):
    t1 = request.POST.get('t1')
    t2 = request.POST.get('t2')
    date = request.POST.get('t3')
    try:
        s_id = StudentRegistration.objects.get(id=t1)
        cl_id = ScheduleClass.objects.get(id=t2)
        StudentInfo(id=s_id.id,class_id=cl_id.id,date=date).save()
        messages.success(request,'Attendence Saved')
        return redirect('take_attendence')
    except:
        messages.error(request,'Details are invalid! please try again')
        return redirect('take_attendence')








#student module
def student(request):
    return render(request,'students/student.html')

def student_register(request):
    return render(request, 'students/student_register.html')

def save_student_details(request):
    nm = request.POST.get('t1')
    dob = request.POST.get('t2')
    gen = request.POST.get('t3')
    con = request.POST.get('t4')
    p_id = request.POST.get('t5')
    em = request.POST.get('t6')
    ps = request.POST.get('t7')
    ps2 = request.POST.get('t8')
    res = ParentRegistration.objects.get(id=p_id)
    if ps == ps2:
        StudentRegistration(name=nm,dob=dob,gender=gen,contact=con,parent=res,email=em,password=ps,status='activate').save()
        res = StudentRegistration.objects.all()
        all = list(res)
        std = all[-1]
        send_mail('Remainding!',
                  'You are successfully registered into iLearn Portal! your ID number is '+ str(std.id) +' , now you can login into iLearn portal.',
                  se.EMAIL_HOST_USER,
                  [std.email]
                  )
        messages.success(request, 'Registered Successfully! Your ID is sent to your registered email.')
        return redirect('student')
    else:
        messages.error(request, 'please give same password in both fields')
        return redirect('student_register')

def student_login_check(request):
    if request.method == "POST":
        id = request.POST.get('t1')
        password = request.POST.get('t2')
        try:
            res = StudentRegistration.objects.get(id=id,password=password)
            if res.status == 'activate':
                request.session["student_status"] = True
                request.session["student_id"] = res.id
                return redirect('student_home')
            else:
                messages.error(request,'your account need to be activate by admin')
                return redirect('student')

        except StudentRegistration.DoesNotExist:
            messages.error(request,'Login details are Invalid')
            return redirect('student')
    else:
        request.session["student_status"] = False
        return render(request, "students/student.html", {"error": "Lecture Logout Successfully"})


def student_home(request):
    return render(request, 'students/student_home.html')


def student_attendence(request):
    id = request.session["student_id"]
    res = StudentInfo.objects.filter(id=id)
    return render(request,'students/student_attendence.html',{'data':res})


def student_profile(request):
    id = request.session["student_id"]
    res = StudentRegistration.objects.get(id=id)
    return render(request, 'students/student_profile.html', {'data': res})

def biomedical_course(request):
    return render(request,'students/biomedical_course.html')







#parent module
def parent(request):
    return render(request, 'parents/parent.html')


def parent_register(request):
    return render(request, 'parents/parent_register.html')


def save_parent_details(request):
    nm = request.POST.get('t1')
    rel = request.POST.get('t2')
    con = request.POST.get('t3')
    em = request.POST.get('t4')
    ps = request.POST.get('t5')
    ps2 = request.POST.get('t6')
    if ps == ps2:
        ParentRegistration(name=nm,relation=rel,contact=con,email=em,password=ps,status='activate').save()
        res = ParentRegistration.objects.all()
        all = list(res)
        parnt = all[-1]
        send_mail('Remainding!',
                  'You are successfully registered into iLearn Portal! your ID number is ' + str(
                      parnt.id) + ' , now you can login into iLearn portal.',
                  se.EMAIL_HOST_USER,
                  [parnt.email]
                  )
        messages.success(request,'Registered Successfully! Your ID is sent to your registered email.')
        return redirect('parent')
    else:
        messages.error(request,'please give same password in both fields')
        return redirect('parent_register')

def parent_login_check(request):
    if request.method == "POST":
        id = request.POST.get('t1')
        password = request.POST.get('t2')
        try:
            res = ParentRegistration.objects.get(id=id,password=password)
            if res.status == 'activate':
                request.session["parent_status"] = True
                request.session["parent_id"] = res.id
                return redirect('parent_home')
            else:
                messages.error(request,'your account need to be activate by admin')
                return redirect('parent')

        except ParentRegistration.DoesNotExist:
            messages.error(request,'Login details are Invalid')
            return redirect('parent')
    else:
        request.session["parent_status"] = False
        return render(request, "parents/parent.html", {"error": "Lecture Logout Successfully"})

def parent_home(request):
    return render(request,'parents/parent_home.html')

def parent_profile(request):
    id = request.session["parent_id"]
    res = ParentRegistration.objects.get(id=id)
    return render(request,'parents/parent_profile.html',{'data':res})

def student_progress(request):
    id = request.session["parent_id"]
    res = ParentRegistration.objects.get(id=id)
    s_id = StudentRegistration.objects.get(parent=res.id)
    s_if = StudentInfo.objects.filter(id=s_id.id)
    cls = []
    date = []
    for x in s_if:
        cls.append(x.class_id)
        d = x.date.strftime("%d/%m/%Y")
        date.append(d)
    return render(request,'parents/student_progress.html',{'cless':cls,'date':date})

