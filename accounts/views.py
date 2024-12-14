from django.shortcuts import render

# Create your views here.
 
def login(request):
    return render(request,'account/login.html')

def singup(request):
    return render(request,'account/singup.html')


def logout(request):
    pass