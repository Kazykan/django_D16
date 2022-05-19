from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BaseRegisterForm


class IndexView(TemplateView):
    """Стандартная страница заглушка - временно"""
    template_name = 'board/index.html'


class BaseRegisterView(CreateView):
    """Регистрация пользователей"""
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
