from django.apps import AppConfig


class TrackerapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TrackerApi'
    
    def ready(self):
        import TrackerApi.signals
