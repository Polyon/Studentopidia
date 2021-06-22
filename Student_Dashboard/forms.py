from django import forms
from .models import *

# Create a profile update form->
class Profile_form(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['year', 'sem', 'contect']

class Profile_picture(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['img']

# Create a qualification update form->
class Qualification_form(forms.ModelForm):
    class Meta:
        model= Qualification
        fields= ['level','board','passingYear','mark']

# Create semester update form->
class Semester_form(forms.ModelForm):
    class Meta:
        model= Semester
        fields= ['sem_1', 'sem_2', 'sem_3', 'sem_4', 'sem_5', 'sem_6', 'sem_7', 'sem_8']

# Create skill update form->
class Skill_form(forms.ModelForm):
    class Meta:
        model= Skills
        fields= ['skill', 'level']

# Create project update form->
class Project_form(forms.ModelForm):
    class Meta:
        model= Project
        fields= ['project']

# Create Hobby update form->
class Hobby_form(forms.ModelForm):
    class Meta:
        model= Hobby
        fields= ["hobbies"]