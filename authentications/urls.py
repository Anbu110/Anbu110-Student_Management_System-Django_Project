from django.urls import path
from .views import *

urlpatterns = [
    path('',LoginPage, name='login' ),
    path('logout/',logoutPage,name='logout'),
    
    path('signup/',SignupPage ,name='signup')
]
