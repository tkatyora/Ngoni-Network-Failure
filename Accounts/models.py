from django.db import models
from django.contrib.auth.models import User,AbstractUser


class Profile(models.Model):
      
    #MODULES FILEDS
        user = models.OneToOneField(User, verbose_name="Personal Infomation", on_delete=models.CASCADE,null=True)
        phoneNumber = models.CharField(max_length=100,null=True)
        city = models.CharField(max_length=100,null=True,default='Not Selected')
        address = models.CharField(max_length=50, null= True,blank=True) 
        accountNumber = models.CharField(max_length=200,null=True)    
       
class NetworkProfile(models.Model):
    network = [('VSAT','VSAT'),('Fibre','Fibre')]
    service = [('VPN','VPN'),('Internet','Internet')]
    profile = models.OneToOneField('Profile', verbose_name="Personal Infomation", on_delete=models.CASCADE,null=True)
    networkAdmin = models.BooleanField(default=False,null=True,blank=False)
    customer = models.BooleanField(default=False,null=True,blank=False)
    capacity = models.CharField(max_length=200,null=True,blank=False)
    IPAddress = models.CharField(max_length=100,null= True,blank=False)
    Network  =models.CharField(max_length=100,null= True,blank=False,choices=network)
    Service =models.CharField(max_length=100,null= True,blank=False,choices=service)
    profilePicture = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 

    @property
    def ImageUrl(self):
        try:
            url = self.profilePicture.url
        except:
            url = ''
            
        return url
    def __str__(self):
            return f"Network For : {(self.Network)} "
     
