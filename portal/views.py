from django.shortcuts import render

# Create your views here.
def dashboard(request):
    content ={}
    content ={
   
    }  
    return render(request , 'Portal/Maindashboard.html',content)
