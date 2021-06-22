from django.shortcuts import render, redirect
from Student_Dashboard.models import *
from mentor_dashboard.models import *
from SPT07.models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/signin') 
def dashboard(request):
    student= Profile.objects.all()
    skill= Skills.objects.all()
    project= Project.objects.all()
    mentor= Mentor_profile.objects.all()
    Mentor= mntr_registration.objects.all()
    total_student= len(student)
    skill_set=[]
    skill_student= []
    analysis= []
    student_data=[]
    student_projects=[]
    student_skill=[]
    a= 0
    b= 0
    c= 0
    d= 0
    y= 0
    for student in student:
        if student.year == 1:
            a = a+1
        elif student.year == 2:
            b = b+1
        elif student.year == 3:
            c = c+1
        elif student.year == 4:
            d = d+1
    for skill in skill:
        if skill.skill in skill_set:
            pass
        else:
            skill_set.append(skill.skill)
    for skill in skill_set:
        x= len(Skills.objects.filter(skill= skill).all())
        skill_student.append(x)
        y= y+x
    for i in skill_student:
        analysis.append(int((i/y)*100))
    for mentor in Mentor:
        studentG= std_registration.objects.filter(mentor= mentor).all()
        student_list=[]
        for std in studentG:
            student_list.append(Profile.objects.get(name= std))
        for stdP in student_list:
            student_skill.append(Skills.objects.filter(name= stdP).all())
            student_projects.append(Project.objects.filter(name= stdP).all())
        student_data.append(student_list)
    year1= (a/total_student)*100
    year2= (b/total_student)*100
    year3= (c/total_student)*100
    year4= (d/total_student)*100
    data= {'mentor': Mentor, 'student_data': student_data, 'student_skill': student_skill, 'student_project': student_projects, 'range': range(1,len(Mentor))}
    student_stats= {'total': total_student, 'year_1': year1, 'year_2': year2, 'year_3': year3, 'year_4': year4, 'a': a, 'b': b, 'c': c, 'd': d}
    student_skill= {'skill': skill_set, 'students': skill_student, 'report': analysis, 'range': range(8)}
    return render(request, 'cdc.html',{'student_report': student_stats, 'skill': student_skill, 'data': data})