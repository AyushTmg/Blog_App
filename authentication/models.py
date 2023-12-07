from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    like=models.ManyToManyField(User,related_name='like')
    is_liked=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class PostImage(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='image')
    image=models.ImageField(null=True,blank=True,upload_to='user/')


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='review')
    description=models.TextField() 
    date=models.DateField(auto_now_add=True)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
    image= models.ImageField( null=True, blank=True ,upload_to='profile/')
    bio = models.TextField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
