from django.shortcuts import render
from account.models import *
from django.contrib.auth.decorators import login_required
import csv
import pandas as pd
import matplotlib.pyplot as plt
# Create your views here.
users = NetworkProfile.objects.all().filter()
@login_required(login_url='sign_in')
def dashboard(request):
    content ={}
    content ={
        'networkuser':users
   
    }  
    return render(request , 'Portal/mainDashboard.html',content)
@login_required(login_url='sign_in')
def NetworkPrediction(request):
    newdata_set = pd.read_csv('prediction.csv')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Network Prediction')
    newdata_set.plot(color='red', linestyle='--')
    prediction =plt.show()
    # with open(prediction, 'r') as f:
    #     reader = csv.reader(f)
    #     data = reader
    content ={}
    content ={
        'predictions':prediction
   
    }  
    return render(request , 'Portal/Prediction.html',content)
