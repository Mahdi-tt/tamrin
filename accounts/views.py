from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
 
def login(request):
    return render(request,'account/login.html')

def singup(request):
    return render(request,'account/singup.html')

@login_required
def logout(request):
     logout(request)