from django.db import models

# Create your models here.

# Mentor registration data
class mntr_registration(models.Model):
    id= models.AutoField("ID").primary_key
    fname= models.CharField("First_name", max_length= 50)
    lname= models.CharField("Last_name", max_length= 50)
    email= models.EmailField("Email", max_length= 254)
    contact= models.BigIntegerField("Contact_No")
    department= models.CharField("Department", max_length= 50)
    password= models.CharField("Password", max_length= 20)
    #Set object name
    def __str__(self):
        return self.fname+" "+self.lname
    
# Student registration data
class std_registration(models.Model):
    id= models.AutoField("ID").primary_key
    fname= models.CharField("First_name", max_length= 50)
    lname= models.CharField("Last_name", max_length= 50)
    email= models.EmailField("Email", max_length= 254)
    mentor= models.ForeignKey(mntr_registration, on_delete= models.CASCADE, verbose_name="Mentor") # for connect two tables
    reg_no= models.BigIntegerField("University Reg. No.")
    roll_no= models.BigIntegerField("University Roll No.")
    password= models.CharField("Password", max_length= 20)
    # Set object name.
    def __str__(self):
        return (self.fname+" "+self.lname)
