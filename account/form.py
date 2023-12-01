from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#MODULES FORMS
class CreateUserForm(UserCreationForm):
    
    email = forms.EmailField(required=True , label='Enter Email address',
                              widget=forms.EmailInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'email'
                                     
                                  })),
    first_name = forms.CharField(required=True , label='Enter First Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
    last_name = forms.CharField(required=True , label='Enter last Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    username = forms.CharField(required=True , label='Enter Username',
                                widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
  
 
   
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['first_name','last_name', 'username','email','password1','password2'] 
        
        
        
class CreateProfileForm(ModelForm):
    city = forms.CharField(required=True , label='Enter City', 
                            widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    phoneNumber=forms.IntegerField( label='Enter Phone Number', required=True,                                )
    address = forms.CharField(label='Enter Address', required=False)
   
    
    class Meta:
        model = NetworkProfile
        fields = ['city','phoneNumber','address','accountNumber']
   

#SPECIFIC FORMS  
    
  