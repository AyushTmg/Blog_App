from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.conf import settings
from .models import Post,PostImage,Review,Profile

class UserRegister(UserCreationForm):
    class Meta:
        model=User
        fields=settings.SIGN_UP_FIELDS 

class EditUserProfile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description',]

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['description']





class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['image','gender','bio','phone_number','location','gender']