from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Reply, Post


class ProfileView(ListView):
    """Профиль пользователя со списком его подписок на категории и если нет подтверждения регистрации отображение ее"""
    model = Reply
    template_name = 'board/profile.html'
    context_object_name = 'reply'


class PostView(ListView):
    """Посты пользователей"""
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'
