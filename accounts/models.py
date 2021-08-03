#p2c-21-105

from django.db import models
from django.contrib.auth.models import User
class Extende_user(models.Model):
    phone_number = models.CharField(max_length=10)
    college= models.CharField(max_length=50)
    user=  models.OneToOneField(User,on_delete=models.CASCADE)

class signup_user(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.CharField(max_length=70, default="")
   Address= models.CharField(max_length=100, default="")
   username= models.CharField(max_length=100, default="")
   phone_no= models.CharField(max_length=12, default="")
   collage_name= models.CharField(max_length=100, default="")
   Branch= models.CharField(max_length=100, default="")
   password=models.CharField(max_length=100, default="")
   image=models.ImageField(upload_to="profile_pic/" , default="" ,height_field=None, width_field=None)
   
   def __str__(self):
        return self.email 



# Create your models here.


# Create your models here.
