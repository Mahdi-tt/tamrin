from django.shortcuts import render
from blog.models import post
from django.utils import timezone
# Create your views here.
def blog_single(request):
    now = timezone.now()
    posts = post.objects.filter(status=1,publish_date__lte=now)
    context = {'post': posts}
    return render(request,'blog/blog-single.html',context)

def blog_home(request):
    now = timezone.now()
    posts = post.objects.filter(status=1,publish_date__lte=now)
    context = {'post': posts}
    return render(request,'blog/blog_home.html',context)