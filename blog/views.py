from django.shortcuts import render

# Create your views here.
def blog_single(request):
    return render(request,'blog/blog-single.html')

def blog_home(request):
    return render(request,'blog/blog_home.html')