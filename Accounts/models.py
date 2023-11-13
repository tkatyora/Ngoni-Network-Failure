from django.db import models
from django.contrib.auth.models import User,AbstractUser


class Profile(models.Model):
    #MODULES FILEDS
        Gender = [('male','Male'),('female','Female')]
        user = models.OneToOneField(User, verbose_name="Personal Infomation", on_delete=models.CASCADE,null=True)
        phoneNumber = models.CharField(max_length=100,null=True)
        city = models.CharField(max_length=100,null=True,default='Not Selected')
        address = models.CharField(max_length=50, null= True,blank=True) 
        #profilePicture = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 
        gender = models.CharField( max_length=50 , choices = Gender ,default='Not Seleted' ,null=True)
        accountNumber = models.CharField(max_length=100,null=True)

        
    #SPECIFIC FIELDS


        def __str__(self):
            return f"Information for => Username : {str(self.user.username)} "
         # @property
    # def ImageUrl(self):
    #     try:
    #         url = self.image.url
    #     except:
    #          url = ''
             
    #     return url
