from django.shortcuts import render
from account.models import *
# Create your views here.
users = NetworkProfile.objects.all().filter()
def dashboard(request):
    content ={}
    content ={
        'networkuser':users
   
    }  
    return render(request , 'Portal/mainDashboard.html',content)
