from random import randint

from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.core.mail import mail_managers

from .models import Post, Reply, Author


@receiver(post_save, sender=User)
def notify_managers_user(sender, instance, created, **kwargs):
    """Отслеживание регистрации/создания пользователя связывание его
    с 'Author' доб. в группу base, генерация 4-х значного кода и отправка его на почту - отправка не реализованна"""
    if created:
        author = Author.objects.create(authorUser=instance)
        author.code_generation()
        add_user_to_group(instance, 'base')
        subject = f'Подтвердите аккаунт {instance.username} - код подтверждения {author.codeUser}'
        print(subject)


def add_user_to_group(user, group):
    """Добавление пользователя в группу"""
    basic_group = Group.objects.get(name=group)
    basic_group.user_set.add(user)
