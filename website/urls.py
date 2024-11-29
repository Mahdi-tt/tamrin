from django.urls import path 
from website.views import index , contact, listblog


app_name = 'website'

urlpatterns = [
    path('', index ,name='index'),
    path('contact/', contact ,name='contact'),
    path('blog/', listblog ,name='listblog'), 
]
