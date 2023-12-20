from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard , name ='dashboard'),  
    path('networkPrediction',views.NetworkPrediction , name ='Prediction'),  
    path('networkPerfomance',views.NetworkPerfomance , name ='Perfomance'),  
   
]


