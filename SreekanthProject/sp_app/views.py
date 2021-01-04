from django.contrib import messages
from django.shortcuts import render, redirect
# from sp_app.forms import SignupForm
from django.core.mail import send_mail
from SreekanthProject import settings as se

from sp_app.forms import ProjectForm


def home(request):
    return render(request,'home.html')

def technologies(request):
    return render(request, 'technologies.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    # form = SignupForm()
    return render(request,'signup.html')

def project(request):
    form = ProjectForm()
    return render(request,'project.html',{'form':form})


def save_project_details(request):
    form = ProjectForm(request.POST)
    # print(form['email'].value())
    if form.is_valid():
        form.save()
        title = form['title'].value()
        technology = form['technology'].value()
        describe = form['describe'].value()
        duration = form['duration'].value()
        affordable_amount = form['affordable_amount'].value()
        email = form['email'].value()
        contact = form['contact'].value()
        country = form['country'].value()

        message = 'Title: '+title +'\n' \
                  + 'Technology: '+technology+ '\n' \
                  +'Description: '+describe+'\n'\
                  +'Duration: '+duration+'\n'\
                  +'Amount: '+affordable_amount+'\n'\
                  +'Email Id: '+email+'\n'\
                  +'Contact: '+contact+'\n'\
                  +'Country: '+country

        send_mail(title,
                  message,
                  se.EMAIL_HOST_USER,
                  ['ivsrikanth279@gmail.com']
                  )
        messages.success(request,'Uploaded Successfully, You Will Get Acknowledge As Soon As Possible, Thanks For The Consunt.')
        return redirect('project')

    else:
        messages.error(request,'Details are not uploaded successfully! Please try again, Thank You')
        return redirect('project')