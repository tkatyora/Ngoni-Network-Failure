from django.urls import path
from . import views
from Accounts import views as view

urlpatterns = [
    #Django Modules
    path('',views.home, name = 'home'),
    path('about', views.about , name = 'about'),
    path('signIn',view.signin , name='sign_in'),
    path('signUp',view.signup , name='sign_up'),
    path('logout',view.signout , name ='logout'),  

    #SPECIFIC URLS
]


