from django.apps import AppConfig


class BloggerConfig(AppConfig):
    name = 'blogger'
    
    def ready(self):
        import blogger.signals
