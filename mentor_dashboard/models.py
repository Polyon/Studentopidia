from django.db import models
from SPT07.models import mntr_registration
from Student_Dashboard.models import Profile

# Create your models here.
class Mentor_profile(models.Model):
    id= models.IntegerField("ID").primary_key
    img= models.ImageField("Profile", upload_to= 'Mentor_Profile', default= "Mentor_Profile/user.jpg")
    name= models.ForeignKey(mntr_registration, verbose_name="Name", on_delete=models.CASCADE)
    sec1= models.CharField("Section A", max_length=50, default="")
    sec2= models.CharField("Section B", max_length=50, default="")
    def __str__(self):
        return self.name.fname+" "+self.name.lname

class Verification(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Mentor_profile, verbose_name="Name", on_delete=models.CASCADE)
    student= models.ForeignKey(Profile, on_delete= models.CASCADE, verbose_name="Student")
    skill= models.CharField("Skill known", max_length=30, default="None")
    level= models.IntegerField("Level", blank= True, null= True)
    def __str__(self):
        return self.name.name.fname+" "+self.name.name.lname