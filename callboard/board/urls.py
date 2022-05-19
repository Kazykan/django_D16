from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from .views import IndexView, BaseRegisterView

urlpatterns = [
    path('', IndexView.as_view()),  # временно для проверки работы
    path('login/',
         LoginView.as_view(template_name='board/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='board/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='board/signup.html'),
         name='signup'),
]
