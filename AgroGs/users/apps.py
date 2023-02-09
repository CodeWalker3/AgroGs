from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "AgroGs.users"
    def ready(self):
        import AgroGs.users.signals