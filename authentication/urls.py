from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("profile/", EditProfileView.as_view(), name="profile"),
    path("signup/", SingUpFormView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path("change_password/", views.change_password_with_old_password, name="change_pass"),
    path("set_password/", views.change_password_without_old_password, name="set_pass"),
    # path('create_post/',CreatePostView.as_view(),name='create_post'),
    path("create_post/", views.createPost, name="create_post"),
    path("userpost/", UserPostView.as_view(), name="userpost"),
    path("delete_post/<int:pk>/", DeletePostView.as_view(), name="delete_post"),
    path("delete_review/<int:pk>/", DeleteReviewView.as_view(), name="delete_review"),
    path("reviews/<int:pk>/", ReviewView.as_view(), name="reviews"),
    path("add_reviews/<int:pk>/", AddReviewView.as_view(), name="add_reviews"),
    # path("add_reviews/<int:pk>/",views.addReview, name="add_reviews"),
    path("post_like/<int:pk>/", views.likePost, name="post_like"),
    path("edit_profile/",ProfileView.as_view(), name="edit_profile"),
    path("view_profile/",ViewProfile.as_view(), name="view_profile"),
]
