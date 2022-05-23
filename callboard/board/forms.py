from django import forms


class AuthenticationForm(forms.Form):
    """Форма для аутентификации пользователя по 4-х значному коду"""
    codeAuthor = forms.IntegerField(label='Введите 4-х значный проверочный код отправленный на почту')
