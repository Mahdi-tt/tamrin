from django.shortcuts import render
from blog.models import post ,comment
from django.utils import timezone
from blog.forms import commentforms
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.
def blog_single(request,id):
    if request.method =='POST':
        form = commentforms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'success comment')
        else:
            messages.error(request,form.errors.as_text())

    form = commentforms()
    now = timezone.now()
    posts = get_object_or_404(post,pk=id,status=1,publish_date__lte=now)
    posts.cuntent_view +=1
    posts.save()
    comments = comment.objects.filter(aproved = True) 
    context = {'posts': posts,
               'form':form,
               'comment':comments}
    return render(request,'blog/blog-single.html',context)

def blog_home(request):
    now = timezone.now()
    posts = post.objects.filter(status=1,publish_date__lte=now)
    context = {'post': posts}
    return render(request,'blog/blog_home.html',context)

def search(request):
    now = timezone.now()
    if request.method == 'GET':
        posts= post.objects.filter(status=1,publish_date__lte=now)
        if s:=request.GET.get('search'):
            posts=posts.filter(content__contains=s) or posts.filter(titel__contains=s)

    context = {'post':posts}
    return render(request,'blog/blog_home.html',context)