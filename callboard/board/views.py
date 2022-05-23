from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .models import Reply, Post, Author
from .forms import AuthenticationForm
from .signals import add_user_to_group


class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    """Не работало перенаправление при ошибке доступа 403, переназначение функции"""
    login_url = reverse_lazy('author_authentication')

    def handle_no_permission(self):
        return redirect(self.get_login_url())


class ProfileView(RedirectPermissionRequiredMixin, ListView):
    """Личная страница с откликами на посты"""
    model = Reply
    template_name = 'board/profile.html'
    context_object_name = 'reply'
    permission_required = ('board.view_reply', 'board.add_reply', 'board.delete_reply', 'board.change_reply')


class PostView(ListView):
    """Посты пользователей"""
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Отдельный пост"""
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'


@login_required
def authentication(request):
    """Страница верификации пользователя с помощью 4-х значного кода
    Добавление его в группу registered_user и установки галочки status"""
    if request.method == 'POST':
        code = request.POST.get('codeAuthor')
        if int(code) == int(Author.objects.get(authorUser=request.user).codeUser):
            Author.objects.get(authorUser=request.user).check_status()
            add_user_to_group(request.user, 'registered_user')
            return redirect('author_authentication')
        else:
            return redirect('author_authentication')
    else:
        status = Author.objects.get(authorUser=request.user).status
        userform = AuthenticationForm()
        return render(request, 'account/authentication.html', {'form': userform, 'status': status})


@login_required
def resend_code_author(request):
    """Страница генерации и отправки кода проверки пользователя"""
    Author.objects.get(authorUser=request.user).code_generation()
    return redirect('author_authentication')
