from django.apps import AppConfig


class CodingProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coding_profile'

    def ready(self):
        import coding_profile.signals
