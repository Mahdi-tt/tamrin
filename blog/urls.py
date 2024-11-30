from django.urls import path 
from .views import blog_single ,blog_home
app_name='blog'

urlpatterns = [
    path('', blog_home,name='blog_home'),
    path('blog', blog_single,name='blog_single'),
   
]