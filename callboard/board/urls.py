from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from .views import ProfileView, PostView, authentication, PostDetail, resend_code_author

urlpatterns = [
    path('post',  PostView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetail.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('authentication/', authentication, name='author_authentication'),
    path('authentication/resend_code', resend_code_author, name='resend_code_author'),
]
