from django.apps import AppConfig

class EventAppConfig(AppConfig):
    name = 'apps.events'
    label = 'events'
    verbose_name = 'Events'

    def ready(self):
        import apps.events.signals
default_app_config = 'apps.events.EventAppConfig'