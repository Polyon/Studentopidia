from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from SPT07.models import std_registration
from Student_Dashboard.models import *
from Student_Dashboard.forms import *
from mentor_dashboard.models import *

# Create your views here.

# Function for go to user dashboard ->
@login_required(login_url='/signin') 
def dashboard(request):
    username= request.session.get('user_id')
    if username is not None:
        user= User.objects.get(username= username)
        if user.is_active:
            student= std_registration.objects.get(email= user.username)
            profile= Profile.objects.get(name= student)
            qualification= Qualification.objects.filter(name= profile).all()
            semester= Semester.objects.get(name= profile)
            skill= Skills.objects.filter(name= profile).all()
            project= Project.objects.filter(name= profile).all()
            hobby= Hobby.objects.get(name= profile)
            notice= Notice.objects.filter(name= profile).all()
            return render(request, 'student_dashboard.html', {'student': student, 'profile': profile, 'qualification': qualification, 'semester': semester, 'skill': skill, 'project': project, 'hobby': hobby, 'notice': notice})
        else:
            return redirect("/signin")
    else:
        return redirect("/")

# Function for update profile data ->
def updateProfile(request):
    user_temp= std_registration.objects.get(email= request.session.get('user_id'))
    user= Profile.objects.get(name= user_temp)
    if request.method=='POST':
        if request.POST.get('name'):
            form= Profile_form(request.POST, instance=user)
            if form.is_valid:
                form.save()
                message= 'Your profile update successfully.'
                Notice(name= user, notice= message).save()
                # messages.success(request, "Your profile update successfully.")
            else:
                pass
        else:
            form= Profile_picture(request.POST, request.FILES, instance=user)
            if form.is_valid:
                form.save()
                # print('success')
            else:
                # print('error')
                pass
    else:
        message= 'Your profile update unsuccessfull. Check your data and retry.'
        Notice(name= user, notice= message).save()
        # messages.warning(request, "Your profile update unsuccessfull.")
    return redirect("/student/")

# Function for update qualification details ->
def updateQualification(request):
    user_temp= std_registration.objects.get(email= request.session.get('user_id'))
    user= Profile.objects.get(name= user_temp)
    if request.method == 'POST':
        data= Qualification.objects.filter(name= user).all()
        if data.filter(level= "").exists() or data.filter(level="None").exists():
            target= data.get(level= "None")
            form= Qualification_form(request.POST, instance= target)
            if form.is_valid:
                form.save()
                message= 'SUCESSFULL! Edited qualification details.'
                Notice(name= user, notice= message).save()
                # messages.success(request, "SUCESSFULL! Edited qualification details.")
            else:
                message= 'Error! please check your inputs!'
                Notice(name= user, notice= message).save()
                # messages.warning(request, "Error! please check your inputs!")
                pass
        elif data.filter(level= request.POST.get('level')).exists():
            target= data.get(level= request.POST.get('level'))
            form= Qualification_form(request.POST, instance= target)
            if form.is_valid:
                form.save()
                message= 'SUCESSFULL! Edited qualification details.'
                Notice(name= user, notice= message).save()
                # messages.success(request, "SUCESSFULL! Edited qualification details.")
            else:
                message= 'Error! please check your inputs!'
                Notice(name= user, notice= message).save()
                # messages.warning(request, "Error! please check your inputs!")
                pass
        elif data.filter(passingYear= request.POST.get('passingYear')).exists():
            target= data.get(passingYear= request.POST.get('passingYear'))
            form= Qualification_form(request.POST, instance= target)
            if form.is_valid:
                form.save()
                message= 'SUCESSFULL! Edited qualification details.'
                Notice(name= user, notice= message).save()
                # messages.success(request, "SUCESSFULL! Edited qualification details.")
            else:
                message= 'Error! please check your inputs!'
                Notice(name= user, notice= message).save()
                # messages.warning(request, "Error! please check your inputs!")
                pass
        else:
            name= user
            level= request.POST.get('level')
            board= request.POST.get('board')
            year= request.POST.get('year')
            marks= request.POST.get('marks')
            Qualification(name= name, level= level, board= board, passingYear= year, mark= marks).save()
            message= 'SUCESSFULL! Added qualification details.'
            Notice(name= user, notice= message).save()
            # messages.success(request, "SUCESSFULL! Added a new qualification details.")
    return redirect("/student/")

# Function for update semester data ->
def semester(request):
    user_temp= std_registration.objects.get(email= request.session.get('user_id'))
    user= Profile.objects.get(name= user_temp)
    if request.method=='POST':
        data= Semester.objects.get(name= user)
        form= Semester_form(request.POST, instance= data)
        if form.is_valid:
            form.save()
            message= 'SUCESSFULL! Data update successfully.'
            Notice(name= user, notice= message).save()
            # messages.success(request, 'SUCCESSFUL! Data update successfully.')
        else:
            pass
    return redirect("/student/")

# Function for update skill data ->
def skill(request):
    user_temp= std_registration.objects.get(email= request.session.get('user_id'))
    user= Profile.objects.get(name= user_temp)
    mentor= Mentor_profile.objects.get(name= user.name.mentor)
    if request.method=='POST':
        Verification(name= mentor, student= user, skill= request.POST.get('skill'), level= request.POST.get('level')).save()
        message= 'Your entry sended to your mentor successfully! After verifing by your mentor it will be visible to your dashboard.'
        Notice(name= user, notice= message).save()
        # messages.success(request, 'Your entry sended to your mentor successfully! After verifing by your mentor it will be visible to your dashboard.')
    return redirect("/student/")

# Function for update project data ->
def project(request):
    user_temp= std_registration.objects.get(email= request.session.get('user_id'))
    user= Profile.objects.get(name= user_temp)
    if request.method=='POST':
        data= Project.objects.filter(name= user).all()
        if data.filter(id= request.POST.get('id')).exists():
            target= data.get(id= request.POST.get('id'))
            form= Project_form(request.POST, instance= target)
            if form.is_valid:
                form.save()
                message= 'Project details updated successfully.'
                Notice(name= user, notice= message).save()
            else:
                message= 'Project details updating unsuccessfull.'
                Notice(name= user, notice= message).save()
                pass
        else:
            name= user
            project= request.POST.get('project')
            Project(name= user, project= project).save()
            message= 'Project details updated successfully.'
            Notice(name= user, notice= message).save()
    return redirect("/student/")

# Function for update hobbies ->
def hobby(request):
    user_temp= std_registration.objects.get(email= request.session.get('user_id'))
    user= Profile.objects.get(name= user_temp)
    if request.method=='POST':
        data= Hobby.objects.get(name= user)
        form= Hobby_form(request.POST, instance= data)
        if form.is_valid:
            form.save()
            message= 'Hobbies updated successfully.'
            Notice(name= user, notice= message).save()
        else:
            message= 'Hobbies updating unsuccessfull.'
            Notice(name= user, notice= message).save()
            pass
    return redirect("/student/")

# For delete readed notification ->
def notice(request, id):
    Notice.objects.filter(id= id).delete()
    return redirect("/student/")