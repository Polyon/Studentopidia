from django.shortcuts import render, HttpResponse, redirect
from .models import std_registration, mntr_registration
from .forms import *
from Student_Dashboard.models import *
from mentor_dashboard.models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    activation={'home':"active", 'student':"", 'about':"", 'contact':""}
    return render(request, "index.html", activation)

def student(request):
    activation={'home':"", 'student':"active", 'about':"", 'contact':""}
    data= std_registration.objects.all()
    student_profile= Profile.objects.all()
    qualification=[]
    semester=[]
    skill=[]
    project=[]
    hobby=[]
    for profile in student_profile:
        qualification.append(Qualification.objects.filter(name= profile).all())
        semester.append(Semester.objects.get(name= profile))
        skill.append(Skills.objects.filter(name= profile).all())
        project.append(Project.objects.filter(name= profile).all())
        hobby.append(Hobby.objects.get(name= profile))
    lenght= range(len(student_profile))
    return render(request, "student.html", {'activation':activation, 'data':data, 'profile': student_profile, 'qualification': qualification, 'semester': semester, 'skill': skill, 'project': project, 'hobby': hobby, 'range': lenght})

def about(request):
    activation={'home':"", 'student':"", 'about':"active", 'contact':""}
    if(request.POST):
        num1= int(request.POST.get('num1'))
        num2= int(request.POST.get('num2'))
        res= num1+num2
        return render(request,"about.html",{'result':res, 'about':"active"})
    else:
        return render(request, "about.html", activation)

def contact(request):
    activation={'home':"", 'student':"", 'about':"", 'contact':"active"}
    return render(request, "contact.html", activation)

def reg(request):
    if request.method=='POST':
        if request.POST.get('mentor'):
            email= request.POST.get('email')
            password= request.POST.get('password')
            if User.objects.filter(email=email).exists():
                if User.objects.filter(password=password).exists():
                    messages.info(request,"Your entered email id is already exits. Please enter unique email id.")
                    messages.info(request,"Your entered password is too common. Please enter unique password.")
                else:
                    messages.info(request,"Your entered email id is already exits. Please enter unique email id.")
                return redirect('/signup')
            else:
                fname= request.POST.get('fname')
                lname= request.POST.get('lname')
                mentor= request.POST.get('mentor')
                reg_no= request.POST.get('reg_no')
                roll_no= request.POST.get('roll_no')
                std_registration(fname= fname, lname= lname, email= email, mentor= mntr_registration.objects.get(fname=mentor), reg_no= reg_no, roll_no= roll_no, password= password).save()
                Student= std_registration.objects.get(email= email)
                profile= Profile(name= Student)
                profile.save()
                Qualification(name= profile).save()
                Semester(name= profile).save()
                Skills(name= profile).save()
                Project(name= profile).save()
                Hobby(name= profile).save()
                user= User.objects.create_user(username= email, first_name= fname, last_name= lname, email= email, password= password)
                user.save()
                messages.info(request, "Your account created successfully. Now you can login.")
                return redirect('/signin')
        elif request.POST.get('dept'):
            email= request.POST.get('email')
            password= request.POST.get('password')
            if User.objects.filter(email=email).exists():
                if User.objects.filter(password=password).exists():
                    messages.info(request,"Your entered email id is already exits. Please enter unique email id.")
                    messages.info(request,"Your entered password is too common. Please enter unique password.")
                else:
                    messages.info(request,"Your entered email id is already exits. Please enter unique email id.")
                return redirect('/signup')
            else:
                fname= request.POST.get('fname')
                lname= request.POST.get('lname')
                contact= request.POST.get('phone')
                department= request.POST.get('dept')
                mntr_registration(fname= fname, lname= lname, email= email, department= department, contact= contact, password= password).save()
                mentor= mntr_registration.objects.get(email= email)
                Mentor_profile(name= mentor).save()
                user= User.objects.create_user(username= email, first_name= fname, last_name= lname, email= email, password= password)
                user.save()
                messages.info(request, "Your account created successfully. Now you can login.")
                return redirect('/signin')
    else:
        mentor= mntr_registration.objects.all()
        return render(request,"reg.html",{'mentor': mentor})

def user_login(request):
    if request.method=='POST':
        if request.POST.get('sEmail'):
            username= request.POST.get('sEmail')
            password= request.POST.get('sPassword')
            user= auth.authenticate(request, username= username, password= password)
            if user is not None:
                auth.login(request, user)
                request.session['user_id']= username
                return redirect('student/')
            else:
                messages.warning(request, "Invalid username or password")
                return redirect('/signin')
        elif request.POST.get('fEmail'):
            username= request.POST.get('fEmail')
            password= request.POST.get('fPassword')
            user= auth.authenticate(request, username= username, password= password)
            if user is not None:
                auth.login(request, user)
                request.session['mentor_id']= username
                return redirect('mentor/')
            else:
                messages.warning(request, "Invalid username or password")
                return redirect('/signin')
        elif request.POST.get('cEmail'):
            username= request.POST.get('cEmail')
            password= request.POST.get('cPassword')
            user= auth.authenticate(request, username= username, password= password)
            if user is not None:
                auth.login(request, user)
                request.session['cdc_id']= username
                return redirect('cdc/')
            else:
                messages.warning(request, "Invalid username or password!!")
                return redirect('/signin')
    else:
        return render(request,"login.html")

def getPassword(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        if std_registration.objects.filter(email= email).exists():
            user= std_registration.objects.get(email= email)
            password= user.password
        elif mntr_registration.objects.filter(email= email).exists():
            user= std_registration.objects.get(email= email)
            password= user.password
        else:
            messages.warning(request, "User not found!!")
        message= 'Your password is '+ password
        send_mail('Forgot Password - Studentopidia', message, settings.EMAIL_HOST_USER, [email])
    return redirect('/signin')

def user_logout(request):
    logout(request)
    del request.session
    return redirect("/")

