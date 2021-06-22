from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from Student_Dashboard.models import *
from SPT07.models import *


# Create your views here.
@login_required(login_url='/signin') 
def dashboard(request):
    username= request.session.get('mentor_id')
    if username is not None:
        user= User.objects.get(username= username)
        if user.is_active:
            name= mntr_registration.objects.get(email= username)
            mprofile= Mentor_profile.objects.get(name= name)
            verfication= Verification.objects.filter(name= mprofile).all()
            student= std_registration.objects.filter(mentor= name).all()
            student_profile= []
            qualification=[]
            semester=[]
            skill=[]
            project=[]
            hobby=[]
            i=0
            j=0
            for student in student:
                student_profile.append(Profile.objects.get(name= student))
            for profile in student_profile:
                qualification.append(Qualification.objects.filter(name= profile).all())
                semester.append(Semester.objects.get(name= profile))
                skill.append(Skills.objects.filter(name= profile).all())
                project.append(Project.objects.filter(name= profile).all())
                hobby.append(Hobby.objects.get(name= profile))
                if profile.year % 2 == 0:
                    i = i+1
                else:
                    j = j+1
            n= len(student_profile)
            sec1= int((j/n)*100)
            sec2= int((i/n)*100)
            data= {'total': n, 'sec1': sec1, 'sec2': sec2, 'no1': j, 'no2': i}
            return render(request, 'mentor_dashboard.html',{'profile': mprofile, 'verification': verfication, 'data': data, 'student': student_profile, 'qualification': qualification, 'semester': semester, 'skill': skill, 'project': project, 'hobby': hobby})
        else:
            redirect('/signin')
    else:
        redirect('/')

def updateProfile(request):
    user_temp= mntr_registration.objects.get(email= request.session.get('mentor_id'))
    user= Mentor_profile.objects.get(name= user_temp)
    if request.method=='POST':
        if request.POST.get('name'):
            form= Profile_form(request.POST, instance=user)
            if form.is_valid:
                form.save()
                user_temp.contact= request.POST.get('contact')
                user_temp.save()
                messages.success(request, "Your profile update successfully.")
            else:
                pass
        else:
            form= Profile_pic(request.POST, request.FILES, instance=user)
            if form.is_valid:
                form.save()
            else:
                pass
    else:
        messages.warning(request, "Your profile update unsuccessfull.")
    return redirect("/mentor/")

def agree(request, id):
    verified= Verification.objects.get(id= id)
    student= Skills.objects.filter(name= verified.student).all()
    # skill= student.get(skill= verified.skill)
    if student.filter(skill="None").exists():
        skill= student.get(skill= "None")
        skill.skill= verified.skill
        skill.level= verified.level
        skill.save()
        Verification.objects.filter(id= id).delete()
    elif student.filter(skill= verified.skill).exists():
        skill= student.get(skill= verified.skill)
        skill.level= verified.level
        skill.save()
        Verification.objects.filter(id= id).delete()
    else:
        Skills(name= verified.student, skill= verified.skill, level= verified.level).save()
        Verification.objects.filter(id= id).delete()
    message= 'Congratulation! Your entry is accepted by mentor. Now you see the data in your dashboard.'
    Notice(name= verified.student, notice= message).save()
    return redirect('/mentor/')

def decline(request, id):
    Verification.objects.filter(id= id).delete()
    message= 'Sorry! Your entry is decline by mentor.'
    Notice(name= verified.student, notice= message).save()
    return redirect('/mentor/')