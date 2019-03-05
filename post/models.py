from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

#from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title=models.CharField(blank=False,max_length=20)
    body=models.TextField(blank=True)
    slug=models.SlugField(null=True)
    image=models.ImageField(null=True,blank=True,width_field='width_field',height_field='height_field')
    width_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):

        #return reverse('posts:detail', kwrgs={"id": self.id} )
        return "/posts/%s/%s/" %(self.id,self.slug)


    class Meta:
        ordering=['-timestamp', '-updated']

class Contact(models.Model):
    name=models.CharField(max_length=20,blank=False)
    email=models.EmailField(blank=False)
    comments=models.TextField(max_length=200)

    def __str__(self):
        return self.name