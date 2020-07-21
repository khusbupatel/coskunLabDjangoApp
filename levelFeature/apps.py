from django.apps import AppConfig


class LevelFeatureConfig(AppConfig):
    name = 'levelFeature'

    def ready(self):
        from . import updater
        updater.start()


