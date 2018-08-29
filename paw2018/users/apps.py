from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "paw2018.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
