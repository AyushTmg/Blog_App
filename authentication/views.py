from typing import Any
from django import http
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from  .models import *
from .forms import *
from django.contrib  import messages
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout,update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView,FormView,DetailView
from django.urls import reverse_lazy,reverse
from django.views import View
from django.forms import formset_factory
from django.http import HttpResponseRedirect


    
class HomeView(TemplateView):
     template_name="authentication/home.html"
     
     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            context=super().get_context_data(**kwargs)
            posts = Post.objects.all()
            user=self.request.user
            context['user']=user
            context['posts']=posts
            return context
     

     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')



class EditProfileView(UpdateView):
    model=User
    form_class=EditUserProfile
    template_name="authentication/profile.html"
    success_url=reverse_lazy('home')

    def get_object(self): 
        return self.request.user
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        messages.success(self.request,"Successfully Updated")
        return super().post(request, *args, **kwargs)
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')

class SingUpFormView(FormView):
    template_name='authentication/signup.html'
    form_class=UserRegister
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class LoginView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(self.request, user)
            messages.success(self.request, "Logged in Successfully")
            return super().form_valid(form)
        else:
            form.add_error(None,'')
            return self.form_invalid(form) 


    

def logout(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            auth_logout(request)
            return redirect('login')    
        return render(request,"authentication/logout.html")
    else:
        return redirect('login')
    

def change_password_with_old_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request, 'Your password has been changed successfully.')
                return redirect('home') 
            else:
                messages.error(request, 'Please correct the errors below.')

        else:
            form = PasswordChangeForm(request.user)
        
        return render(request, 'authentication/change_pass.html', {'forms': form})
    else:
        return redirect('login')
    

def change_password_without_old_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            print(form)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request, 'Your password has been changed successfully.')
                return redirect('home') 
            else:
                messages.error(request, 'Please correct the errors below.')

        else:
            form = SetPasswordForm(request.user)
        
        return render(request, 'authentication/set_pass.html', {'forms': form})
    else:
        return redirect('login')
    

class DeletePostView(DeleteView):
    model=Post
    template_name='authentication/delete_post.html'
    success_url=reverse_lazy("home")

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')
         
class DeleteReviewView(DeleteView):
    model=Review
    template_name='authentication/delete_post.html'
    success_url=reverse_lazy("home")

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')

      

def createPost(request):
    if request.user.is_authenticated:
        ImageFormset=formset_factory(PostImageForm,extra=3)

        if request.method=='POST':
            post_form = PostForm(request.POST)
            formset=ImageFormset(request.POST, request.FILES)

            if post_form.is_valid() and formset.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user 
                post.save()

                for form in formset:
                    if form.cleaned_data:
                        image = form.save(commit=False)
                        image.post = post
                        image.save()
                return redirect('home') 

        else:
            post_form = PostForm()
            formset = ImageFormset()
        return render(request, 'authentication/create_post.html', {'post_form': post_form, 'formset': formset})
    else:
        return redirect('login')


 



class UserPostView(ListView):
    template_name='authentication/userpost.html'
    context_object_name = 'posts'   
    
    def get_queryset(self) -> QuerySet[Any]:
        user_id=self.request.user.id
        return Post.objects.filter(user_id=user_id)
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')

class AddReviewView(CreateView):
    model=Review
    form_class=ReviewForm
    template_name='authentication/create_review.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get('pk')
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('reviews', kwargs={'pk': pk})
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')
    


class ReviewView(TemplateView):
    template_name="authentication/reviews.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        reviews=Review.objects.filter(post_id=self.kwargs.get('pk'))
        context['post_id']=self.kwargs.get('pk')
        context['reviews']=reviews
        user=self.request.user
        context['user']=user
        return context  
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')
    
def likePost(request,pk):
    if request.user.is_authenticated:
        post=Post.objects.get(id=pk)
        
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            post.is_liked=False
        else:
            post.like.add(request.user)
            post.is_liked=True
        post.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        return redirect('login')
    
class ProfileView(UpdateView):
    form_class=ProfileForm
    template_name="authentication/edit_profile.html"
    success_url=reverse_lazy('view_profile')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        messages.success(self.request,"Successfully Updated")
        return super().post(request, *args, **kwargs)
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')
    

class ViewProfile(TemplateView):
    template_name="authentication/view_profile.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] =self.request.user
        try:
            context["user_profile"] =self.request.user.profile
        except Exception as e:
            print(e)
        return context
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
         if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
         else:
            return redirect('login')
    
