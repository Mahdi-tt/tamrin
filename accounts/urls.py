from django.urls import path 
from .views import *
app_name='account'

urlpatterns = [
    path('login/',login_user,name='login'),
    path('singup/',singup,name='singup'),
    path('logout/',logout,name='logout'),
    ]