from django import forms
from .models import *

class Profile_form(forms.ModelForm):
    class Meta:
        model= Mentor_profile
        fields= ['sec1','sec2']

class Profile_pic(forms.ModelForm):
    class Meta:
        model= Mentor_profile
        fields= ['img']