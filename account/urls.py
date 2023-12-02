from django.urls import path
from . import views

urlpatterns = [
    path('UserProfile',views.profile , name ='profile'),
    path('updateProfile/<int:pk>', views.updateProfile,name ='updateProfile'),
    path('deleteProfile/<int:pk>', views.deleteProfile,name ='deleteProfile'),
    path('addClient',views.newClient,name='create_client')
]
# <i class="fa-regular fa-address-card"></i>