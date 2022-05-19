from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Author(models.Model):
    """Пользователи со статусом зарегистрирован или нет подтверждением 4-х значного кода"""
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='photo/img_avatar', blank=True, null=True)
    status = models.BooleanField(default=False)
    codeUser = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser.username}'


class Post(models.Model):
    """Объявления"""
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('dealer', 'Торговцы'),
        ('guildmaster', 'Гилдмастеры'),
        ('questgift', 'Квестгиверы'),
        ('blacksmith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potionmaster', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний')
    )
    header = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    postCategory = models.CharField(max_length=12, choices=TYPE, default='tank')
    timeInCreation = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f'{self.header[:30]}... : {self.text[:60]}'


class Reply(models.Model):
    """Отклики на объявления с вариантами ответов, полож. или удаление"""
    text = models.TextField()
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    timeInCreation = models.DateTimeField(auto_now_add=True)
    commentShow = models.BooleanField(null=True, default=None)
