from django.db import models

# Create your models here.

class categore(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class post(models.Model):
    titel = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to='blog/',default='default.jpg')
    status = models.BooleanField(default=False)
    cuntent_view=models.IntegerField(default=0)
    categore= models.ManyToManyField(categore)
    publish_date= models.DateTimeField(null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titel