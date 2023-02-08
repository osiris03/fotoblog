from django.db import models
from django.conf import settings 

# Create your models here.

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True )

class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, blank = True, on_delete = models.SET_NULL)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, blank= True)
    date_created = models.BooleanField(default = False)

