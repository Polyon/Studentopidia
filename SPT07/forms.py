from django import forms
from .models import *

# Create registration form for student->
class Student_form(forms.ModelForm):
    class Meta:
        model= std_registration
        fields= "__all__"

# Create mentor sign-up form->
class Mentor_form(forms.ModelForm):
    class Meta:
        model= mntr_registration
        fields= "__all__"