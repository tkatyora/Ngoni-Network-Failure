from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from Accounts.models import *
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate,login,logout
from .form import *

#DJANGO MODULES
# Create your views here.
AllProfile = Profile.objects.all()
alluser = User.objects.all() 



@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request , username = username , password = password)
        if User is not None:
            login(request, User)
            messages.success(request, 'Log  Successfully')
            return redirect('dashboard') 
        else:
            messages.warning(request, 'Invalid Username and  Paasword')
            return redirect('sign_in')
                      
    return render(request, 'Accounts/Usernamelogin.html' )
@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        if userForm.is_valid():
            user = userForm.save()
            username = userForm.cleaned_data.get('username')
            message = 'Account for',{username},'have been succesfully created'
            messages.success(request,message )
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request,'User Form Is Not Valid' )
            return redirect('sign_up')           
    else:
        userForm = CreateUserForm()
        
    content={}
    content = {
        'form' : userForm , }
    return render(request, 'Accounts/Usernameregester.html' , content)


@login_required(login_url='sign_in') 
def signout(request):
    logout(request)
    messages.success(request, 'Log Out successfully')
    return redirect('sign_in')

@login_required(login_url='sign_in') 
def profile(request):
    content ={}
    content ={
        'profile':AllProfile,
        'users': alluser
    }
    return render(request , 'profile.html',content)


@login_required(login_url='sign_in') 
def updateProfile(request,pk):
    profileToBeUpdated = Profile.objects.get(id = pk) 
    userToBeUpdated = User.objects.get(id = pk) 
    if request.method == 'POST':
        form = CreateProfileForm(request.POST ,instance =profileToBeUpdated )
        userform = CreateUserForm(request.POST ,instance =userToBeUpdated )
        if form.is_valid():
            form.save()
            if userform.is_valid():
                userform.save()
                messages.success(request,'Profile Updated Succesfully')
                return redirect('profile') 
            else:
                messages.warning(request, 'Error Encountered In Updating Profile2')
                #return redirect('dashboard') 
        else:
            messages.warning(request, 'Error Encountered In Updating Profile1')
            #return redirect('dashboard')
    else:
        form = CreateProfileForm(instance=profileToBeUpdated)
        userform = CreateUserForm(instance=userToBeUpdated)
        
    content ={}
    content ={
        'form' : form,
        'userform' : userform,
        'profile':AllProfile,
        'users':alluser
    }
    
    
    return render(request,  'updateProfile.html', content)

@login_required(login_url='sign_in')   
def deleteProfile(request,pk):
    deletedProfile = Profile.objects.get(id=pk)
    if request.method =='POST':
        request.user.delete()
        #deletedProfile.delete()
        ##print(user)
        message = messages.success(request, 'Account Succusefully Deleted')
        return redirect('sign_in')
    else:
       message =  messages.warning(request, 'Failled to delete Account')
        
    content={}
    content ={
        'deletedProfile':AllProfile
    }
    return render(request,'deleteProfile.html',content)

