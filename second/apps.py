from django.apps import AppConfig


class SecondConfig(AppConfig):
    name = 'second'

    def ready(self):
        import second.signals