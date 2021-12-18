from django.apps import AppConfig


class AlphaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alpha'
    def ready(self):
        print("Staring Scheduler..")
        from .scheduler import scheduler
        scheduler.start()