from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class  CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, blank=True ,null=True)
    email = models.EmailField(unique=True)
    
class passwrodReset(models.Model):
    user = models.ForeignKey( CustomUser,on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Profile (models.Model):
    user = models.OneToOneField(CustomUser , related_name='profile' , on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=4,null=True, blank=True)
