from django.contrib.auth.models import Group ,User
from django.db.models.signals import post_save
from .models import Profile
import random
from . import views
from django.dispatch  import receiver

num = random.randrange(11,99)
num2 = random.randrange(100,900)
accountCode = f'NS{num}ACS{num2}'

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,*args,**kwargs):
    if created:
        # group = Group.objects.get('Farmers')
        # instance.group.add(group)
        profile = Profile.objects.create(
            user=instance,
            accountcode= accountCode   
        )
        profile.save

        
        
#post_save.connect(create_profile, sender=User)  another way of not using the receiver decorator