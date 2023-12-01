from django.contrib.auth.models import Group ,User
from django.db.models.signals import post_save
from .models import *
import random
import string
from . import views
from django.dispatch  import receiver
 #Generating 2 random numbers
num = random.randrange(11,99)
num2 = random.randrange(100,999)
#Generating 2 alpabhet letters

Alphabet =list(string.ascii_uppercase)
A = random.choice(Alphabet)
B = random.choice(Alphabet)

C = random.choice(Alphabet)
accountNum = f'{A}{B}{C}{num}{num2}'
print(accountNum)

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,*args,**kwargs):
    if created:
        # group = Group.objects.get('Farmers')
        # instance.group.add(group)
        profile = Profile.objects.create(
            user=instance,
            accountNumber= accountNum   
        )
        profile.save

@receiver(post_save, sender=Profile)
def create_profile(sender,instance,created,*args,**kwargs):
    if created:
        # group = Group.objects.get('Farmers')
        # instance.group.add(group)
        networkprofile = NetworkProfile.objects.create(
            profile=instance,
               
        )
        profile.save

        
        
#post_save.connect(create_profile, sender=User)  another way of not using the receiver decorator