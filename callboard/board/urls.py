from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from .views import ProfileView, PostView

urlpatterns = [
    path('',  PostView.as_view(), name='posts'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
