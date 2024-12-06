from django.contrib import admin
from .models import *
# Register your models here.
class postadmin(admin.ModelAdmin):
    date_hierarchy = "publish_date"
    list_display=('titel','cuntent_view','status','publish_date',)
    list_filter=('status','publish_date')
admin.site.register(categore)
admin.site.register(post,postadmin)