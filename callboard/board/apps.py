from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

    def ready(self):
        """Настройка для работы файла signal.py так же поправлен INSTALLED_APPS 'board.apps.BoardConfig'"""
        import board.signals
