from django.db import models
from SPT07.models import std_registration

# Create your models here.

# Create Student's profile->
class Profile(models.Model):
    id= models.IntegerField("ID").primary_key
    img= models.ImageField("Profile", upload_to= "Picture", blank= True, null= True, default= "Picture/user.jpg")
    name= models.ForeignKey(std_registration, on_delete= models.CASCADE, verbose_name="Name")
    year= models.IntegerField("Year", blank= True, null=True)
    sem= models.IntegerField("Semester", blank= True, null=True)
    contect= models.BigIntegerField("Contect", blank= True, null=True)
    
    # Set objects name:
    def __str__(self):
        return self.name.fname+" "+self.name.lname
    
# Create table for qualification details->
class Qualification(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Profile, on_delete= models.CASCADE, verbose_name="Name")
    level= models.CharField("Level", max_length=20, blank= True, default="None")
    board= models.CharField("Board / University", max_length=10, blank= True, default="None")
    passingYear= models.IntegerField("Year of Passing", blank= True, null=True)
    mark= models.FloatField("Percentage", max_length=3, blank= True, null=True)

    # Set objects name:
    def __str__(self):
        return self.name

# Create table for semester details->
class Semester(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Profile, on_delete= models.CASCADE, verbose_name="Name")
    sem_1= models.FloatField("Semester_1", max_length=3, blank= True, null=True)
    sem_2= models.FloatField("Semester_2", max_length=3, blank= True, null=True)
    sem_3= models.FloatField("Semester_3", max_length=3, blank= True, null=True)
    sem_4= models.FloatField("Semester_4", max_length=3, blank= True, null=True)
    sem_5= models.FloatField("Semester_5", max_length=3, blank= True, null=True)
    sem_6= models.FloatField("Semester_6", max_length=3, blank= True, null=True)
    sem_7= models.FloatField("Semester_7", max_length=3, blank= True, null=True)
    sem_8= models.FloatField("Semester_8", max_length=3, blank= True, null=True)

    # Set objects name:
    def __str__(self):
        return self.name

# Create skill table->
class Skills(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Name")
    skill= models.CharField("Skill Name", max_length=100, blank=True, default="None")
    level= models.IntegerField("Skill level", default=0)

    # Set objects name:
    def __str__(self):
        return str(self.name)

# Create projects list->
class Project(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Name")
    project= models.TextField("Project", max_length=500, blank= True, default="None")

    # Set objects name:
    def __str__(self):
        return str(self.name)

# Create hobby list->
class Hobby(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Name")
    hobbies= models.TextField("Hobbies", max_length=400, blank= True)

    # Set objects name:
    def __str__(self):
        return self.name

# Create a notice board->
class Notice(models.Model):
    id= models.IntegerField("ID").primary_key
    name= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Name')
    notice= models.TextField("Notice", max_length=200, blank=True)